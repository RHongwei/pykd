// 
// Load debug symbols using DIA
// 

#include "stdafx.h"
#include "dbghelp.h"
#include "dia/diawrapper.h"
#include "win/utils.h"
#include "dbgengine.h"
#include "diacallback.h"

//////////////////////////////////////////////////////////////////////////////////

namespace pykd {

//////////////////////////////////////////////////////////////////////////////////

namespace diaLoad {

//////////////////////////////////////////////////////////////////////////////////

// DIA data source loader
interface IDataProvider
{
    virtual ~IDataProvider() {}
    virtual HRESULT load(__inout IDiaDataSource &DiaDataSource) = 0;
};

//////////////////////////////////////////////////////////////////////////////////

// Load debug symbols using DIA
static SymbolSessionPtr createSession(
    IDataProvider &DataProvider,
    ULONGLONG loadBase
)
{
    HRESULT hres;
    DiaDataSourcePtr dataSource;

    hres = dataSource.CoCreateInstance(__uuidof(DiaSource), NULL, CLSCTX_INPROC_SERVER);

    if ( S_OK != hres )
        throw DiaException("Call ::CoCreateInstance", hres);

    hres = DataProvider.load(*dataSource);
    if ( S_OK != hres )
        throw DiaException("Call IDiaDataSource::loadDataXxx", hres);

    DiaSessionPtr _session;
    hres = dataSource->openSession(&_session);
    if ( S_OK != hres )
        throw DiaException("Call IDiaDataSource::openSession", hres);

    hres = _session->put_loadAddress(loadBase);
    if (S_OK != hres)
        throw DiaException("Call IDiaSession::put_loadAddress", hres);

    DiaSymbolPtr _globalScope;
    hres = _session->get_globalScope(&_globalScope);
    if ( S_OK != hres )
        throw DiaException("Call IDiaSymbol::get_globalScope", hres);

    return SymbolSessionPtr( new DiaSession( _session, _globalScope ) );
}

//////////////////////////////////////////////////////////////////////////////////

// Load debug symbols using symbol file
class DataFromPdb : public IDataProvider {
    std::wstring m_filePath;

public:
    DataFromPdb(__in const std::string &filePath) {
        m_filePath = toWStr(filePath);
    }

    virtual HRESULT load(__inout IDiaDataSource &dataSource) override {
        return dataSource.loadDataFromPdb( m_filePath.c_str() );
    }
};

// Access to executable file over RVA-callback
class ReadExeAtRVACallback : public IDiaReadExeAtRVACallback {
    ULONGLONG m_loadBase;
    int m_nRefCount;
    CComPtr< IDiaLoadCallback2 > m_diaLoadCallback2;

public:
    ReadExeAtRVACallback(
        __in ULONGLONG loadBase,
        __out std::string &openedSymbolFile
    )   : m_loadBase(loadBase), m_nRefCount(1)
        , m_diaLoadCallback2( new DiaLoadCallback2(&openedSymbolFile) ) 
    {
    }

    // IUnknown impl
    ULONG STDMETHODCALLTYPE AddRef() {
        m_nRefCount++;
        return m_nRefCount;
    }
    ULONG STDMETHODCALLTYPE Release() {
        const int nRefCount = (--m_nRefCount);
        if (!nRefCount)
            delete this;
        return nRefCount;
    }
    HRESULT STDMETHODCALLTYPE QueryInterface( REFIID rid, void **ppUnk ) {
        if ( ppUnk == NULL )
            return E_INVALIDARG;

        if (rid == __uuidof(IDiaReadExeAtRVACallback))
        {
            *ppUnk = this;
            return S_OK;
        }

        return m_diaLoadCallback2->QueryInterface(rid, ppUnk);
    }

    // IDiaReadExeAtRVACallback impl
    virtual HRESULT STDMETHODCALLTYPE ReadExecutableAtRVA( 
        /* [in] */ DWORD relativeVirtualAddress,
        /* [in] */ DWORD cbData,
        /* [out] */ DWORD *pcbData,
        /* [size_is][out] */ BYTE *pbData
    ) override {
        return 
            readMemoryImpl(
                m_loadBase + relativeVirtualAddress,
                pbData,
                cbData,
                pcbData);
    }
};

// Load debug symbols using ReadExeAtRVACallback
struct DataForExeByRva : IDataProvider {

    std::string m_openedSymbolFile;

    DataForExeByRva(
        __in ULONGLONG loadBase,
        __in const std::string &executable,
        __in const std::string &symbolSearchPath
    )   : m_loadBase(loadBase)
    {
        m_executable = toWStr(executable);

        if (symbolSearchPath.empty())
            m_symbolSearchPath = toWStr( getSymbolPath() );
        else
            m_symbolSearchPath = toWStr( symbolSearchPath );
    }

    virtual HRESULT load(__inout IDiaDataSource &dataSource) override {
        CComPtr< IUnknown > readExeAtRVACallback(new ReadExeAtRVACallback(m_loadBase, m_openedSymbolFile) );
        return 
            dataSource.loadDataForExe(
                m_executable.c_str(),
                m_symbolSearchPath.c_str(),
                readExeAtRVACallback);
    }

protected:
    ULONGLONG m_loadBase;

    std::wstring m_executable;
    std::wstring m_symbolSearchPath;
};


//////////////////////////////////////////////////////////////////////////////////

}   // namespace diaLoad

//////////////////////////////////////////////////////////////////////////////////

SymbolSessionPtr  loadSymbolFile(const std::string &filePath, ULONGLONG loadBase )
{
    diaLoad::DataFromPdb dataFromPdb(filePath);
    return diaLoad::createSession(dataFromPdb, loadBase);
}

//////////////////////////////////////////////////////////////////////////////////

SymbolSessionPtr loadSymbolFile(
    __in ULONGLONG loadBase,
    __in const std::string &executable,
    __out std::string &loadedSymbolFile,
    __in_opt std::string symbolSearchPath /*= std::string()*/
)
{
    diaLoad::DataForExeByRva dataForExeByRva(loadBase, executable, symbolSearchPath);

    SymbolSessionPtr symSession = diaLoad::createSession(dataForExeByRva, loadBase);
    loadedSymbolFile = dataForExeByRva.m_openedSymbolFile;
    return symSession;
}

//////////////////////////////////////////////////////////////////////////////////

}   // namespace pykd
