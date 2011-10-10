#
#
#

import unittest
import target
import pykd

class BaseTest( unittest.TestCase ):
      
    def testOldSupportedApi( self ):
        """ Branch test: API 0.0.x what must be available """
    
        self.assertTrue( hasattr(pykd, 'addSynSymbol') )
        self.assertTrue( hasattr(pykd, 'attachKernel') )
        self.assertTrue( hasattr(pykd, 'attachProcess') )
        self.assertTrue( hasattr(pykd, 'addr64') )
        self.assertTrue( hasattr(pykd, 'breakin') )
        self.assertTrue( hasattr(pykd, 'compareMemory') )
        self.assertTrue( hasattr(pykd, 'containingRecord') )
        self.assertTrue( hasattr(pykd, 'createSession') )
        self.assertTrue( hasattr(pykd, 'dbgCommand') )
        self.assertTrue( hasattr(pykd, 'dprint') )
        self.assertTrue( hasattr(pykd, 'dprintln') )
        self.assertTrue( hasattr(pykd, 'debuggerPath') )
        self.assertTrue( hasattr(pykd, 'delAllSynSymbols') )
        self.assertTrue( hasattr(pykd, 'delSynSymbol') )
        self.assertTrue( hasattr(pykd, 'delSynSymbolsMask') )
        self.assertTrue( hasattr(pykd, 'expr') )
        self.assertTrue( hasattr(pykd, 'findModule') )
        self.assertTrue( hasattr(pykd, 'findSymbol') )
        self.assertTrue( hasattr(pykd, 'getCurrentProcess') )
        self.assertTrue( hasattr(pykd, 'getCurrentStack') )
        self.assertTrue( hasattr(pykd, 'getImplicitThread') )
        self.assertTrue( hasattr(pykd, 'getOffset') )
        self.assertTrue( hasattr(pykd, 'getPdbFile') )
        self.assertTrue( hasattr(pykd, 'getProcessorMode') )
        self.assertTrue( hasattr(pykd, 'getProcessorType') )
        self.assertTrue( hasattr(pykd, 'getThreadList') )
        self.assertTrue( hasattr(pykd, 'go') )
        self.assertTrue( hasattr(pykd, 'is64bitSystem') )
        self.assertTrue( hasattr(pykd, 'isDumpAnalyzing') )
        self.assertTrue( hasattr(pykd, 'isKernelDebugging') )
        self.assertTrue( hasattr(pykd, 'isValid') )
        self.assertTrue( hasattr(pykd, 'isWindbgExt') )
        self.assertTrue( hasattr(pykd, 'loadAnsiString') )
        self.assertTrue( hasattr(pykd, 'loadBytes') )
        self.assertTrue( hasattr(pykd, 'loadCStr') )
        self.assertTrue( hasattr(pykd, 'loadChars') )
        self.assertTrue( hasattr(pykd, 'loadDWords') )
        self.assertTrue( hasattr(pykd, 'loadDump') )
        self.assertTrue( hasattr(pykd, 'loadLinkedList') )
        self.assertTrue( hasattr(pykd, 'loadModule') )
        self.assertTrue( hasattr(pykd, 'loadPtrs') )
        self.assertTrue( hasattr(pykd, 'loadQWords') )
        self.assertTrue( hasattr(pykd, 'loadSignDWords') )
        self.assertTrue( hasattr(pykd, 'loadSignQWords') )
        self.assertTrue( hasattr(pykd, 'loadSignWords') )
        self.assertTrue( hasattr(pykd, 'loadUnicodeString') )
        self.assertTrue( hasattr(pykd, 'loadWChars') )
        self.assertTrue( hasattr(pykd, 'loadWStr') )
        self.assertTrue( hasattr(pykd, 'loadWords') )
        self.assertTrue( hasattr(pykd, 'locals') )
        self.assertTrue( hasattr(pykd, 'ptrByte') )
        self.assertTrue( hasattr(pykd, 'ptrDWord') )
        self.assertTrue( hasattr(pykd, 'ptrMWord') )
        self.assertTrue( hasattr(pykd, 'ptrPtr') )
        self.assertTrue( hasattr(pykd, 'ptrQWord') )
        self.assertTrue( hasattr(pykd, 'ptrSignByte') )
        self.assertTrue( hasattr(pykd, 'ptrSignDWord') )
        self.assertTrue( hasattr(pykd, 'ptrSignMWord') )
        self.assertTrue( hasattr(pykd, 'ptrSignQWord') )
        self.assertTrue( hasattr(pykd, 'ptrSignWord') )
        self.assertTrue( hasattr(pykd, 'ptrSize') )
        self.assertTrue( hasattr(pykd, 'ptrWord') )
        self.assertTrue( hasattr(pykd, 'rdmsr') )
        self.assertTrue( hasattr(pykd, 'reg') )
        self.assertTrue( hasattr(pykd, 'reloadModule') )
        self.assertTrue( hasattr(pykd, 'setCurrentProcess') )
        self.assertTrue( hasattr(pykd, 'setImplicitThread') )
        self.assertTrue( hasattr(pykd, 'setProcessorMode') )
        self.assertTrue( hasattr(pykd, 'sizeof') )
        self.assertTrue( hasattr(pykd, 'startProcess') )
        self.assertTrue( hasattr(pykd, 'step') )
        self.assertTrue( hasattr(pykd, 'symbolsPath') )
        self.assertTrue( hasattr(pykd, 'trace') )
        self.assertTrue( hasattr(pykd, 'typedVarArray') )
        self.assertTrue( hasattr(pykd, 'typedVarList') )
        self.assertTrue( hasattr(pykd, 'wrmsr') )

        self.assertTrue( hasattr(pykd, 'BaseException') )
        self.assertTrue( hasattr(pykd, 'MemoryException') )
        self.assertTrue( hasattr(pykd, 'TypeException') )
        self.assertTrue( hasattr(pykd, 'WaitEventException') )
        self.assertTrue( hasattr(pykd, 'bp') )
        self.assertTrue( hasattr(pykd, 'cpuReg') )
        self.assertTrue( hasattr(pykd, 'dbgStackFrameClass') )
        self.assertTrue( hasattr(pykd, 'debugEvent') )
        self.assertTrue( hasattr(pykd, 'disasm') )
        self.assertTrue( hasattr(pykd, 'ext') )
        self.assertTrue( hasattr(pykd, 'intBase') )
        self.assertTrue( hasattr(pykd, 'typeInfo') )
        self.assertTrue( hasattr(pykd, 'typedVar') )
        self.assertTrue( hasattr(pykd, 'windbgIn') )
        self.assertTrue( hasattr(pykd, 'windbgOut') )
        
    def testOldRemovedApi( self ):
        """ Branch test: old API 0.0.x what should be removed """
        self.assertFalse( hasattr(pykd, 'dbgModuleClass') )
        
    def testNewAddededApi( self ):
        """ Branch test: new API 0.1.x what must be available """
        self.assertTrue( hasattr(pykd, 'createDbgClient') )
        self.assertTrue( hasattr(pykd, 'diaLoadPdb') )
        
        self.assertTrue( hasattr(pykd, 'DiaException') )
        self.assertTrue( hasattr(pykd, 'DiaScope') )
        self.assertTrue( hasattr(pykd, 'DiaSymbol') )
        self.assertTrue( hasattr(pykd, 'dbgClient') )
        self.assertTrue( hasattr(pykd, 'din') )
        self.assertTrue( hasattr(pykd, 'dout') )
        self.assertTrue( hasattr(pykd, 'module') )
