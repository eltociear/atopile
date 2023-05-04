# Generated from Atopile.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,71,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,
        4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,5,10,
        60,8,10,10,10,12,10,63,9,10,1,11,4,11,66,8,11,11,11,12,11,67,1,11,
        1,11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,
        23,12,1,0,3,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,
        3,0,9,10,13,13,32,32,72,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,
        1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,
        1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,30,
        1,0,0,0,5,37,1,0,0,0,7,39,1,0,0,0,9,41,1,0,0,0,11,45,1,0,0,0,13,
        47,1,0,0,0,15,49,1,0,0,0,17,51,1,0,0,0,19,53,1,0,0,0,21,57,1,0,0,
        0,23,65,1,0,0,0,25,26,5,102,0,0,26,27,5,114,0,0,27,28,5,111,0,0,
        28,29,5,109,0,0,29,2,1,0,0,0,30,31,5,105,0,0,31,32,5,109,0,0,32,
        33,5,112,0,0,33,34,5,111,0,0,34,35,5,114,0,0,35,36,5,116,0,0,36,
        4,1,0,0,0,37,38,5,44,0,0,38,6,1,0,0,0,39,40,5,59,0,0,40,8,1,0,0,
        0,41,42,5,100,0,0,42,43,5,101,0,0,43,44,5,102,0,0,44,10,1,0,0,0,
        45,46,5,40,0,0,46,12,1,0,0,0,47,48,5,41,0,0,48,14,1,0,0,0,49,50,
        5,123,0,0,50,16,1,0,0,0,51,52,5,125,0,0,52,18,1,0,0,0,53,54,5,112,
        0,0,54,55,5,105,0,0,55,56,5,110,0,0,56,20,1,0,0,0,57,61,7,0,0,0,
        58,60,7,1,0,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,
        0,0,0,62,22,1,0,0,0,63,61,1,0,0,0,64,66,7,2,0,0,65,64,1,0,0,0,66,
        67,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,70,6,11,
        0,0,70,24,1,0,0,0,3,0,61,67,1,6,0,0
    ]

class AtopileLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    ID = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'from'", "'import'", "','", "';'", "'def'", "'('", "')'", "'{'", 
            "'}'", "'pin'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "ID", "WS" ]

    grammarFileName = "Atopile.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

