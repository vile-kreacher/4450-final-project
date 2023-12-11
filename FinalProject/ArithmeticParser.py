# Generated from Arithmetic.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,234,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,4,0,48,8,0,11,0,12,0,49,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,60,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,80,8,5,10,5,12,5,83,9,
        5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,95,8,7,1,7,1,7,4,7,
        99,8,7,11,7,12,7,100,1,7,5,7,104,8,7,10,7,12,7,107,9,7,1,7,3,7,110,
        8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,118,8,8,1,8,1,8,4,8,122,8,8,11,8,
        12,8,123,1,9,1,9,1,9,4,9,129,8,9,11,9,12,9,130,1,10,1,10,1,10,1,
        10,1,10,1,10,3,10,139,8,10,1,10,1,10,4,10,143,8,10,11,10,12,10,144,
        1,11,1,11,1,11,1,11,1,11,1,11,4,11,153,8,11,11,11,12,11,154,1,12,
        1,12,1,13,1,13,1,13,5,13,162,8,13,10,13,12,13,165,9,13,1,14,1,14,
        1,14,1,14,3,14,171,8,14,1,15,1,15,1,15,5,15,176,8,15,10,15,12,15,
        179,9,15,1,16,1,16,1,16,5,16,184,8,16,10,16,12,16,187,9,16,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,197,8,17,1,18,1,18,1,19,
        1,19,1,20,1,20,3,20,205,8,20,1,21,1,21,5,21,209,8,21,10,21,12,21,
        212,9,21,1,21,1,21,1,22,1,22,5,22,218,8,22,10,22,12,22,221,9,22,
        1,22,1,22,1,22,5,22,226,8,22,10,22,12,22,229,9,22,1,22,3,22,232,
        8,22,1,22,2,219,227,0,23,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,0,5,1,0,14,15,1,0,32,33,1,0,34,36,1,0,32,
        36,1,0,14,22,242,0,47,1,0,0,0,2,59,1,0,0,0,4,61,1,0,0,0,6,65,1,0,
        0,0,8,70,1,0,0,0,10,76,1,0,0,0,12,84,1,0,0,0,14,88,1,0,0,0,16,111,
        1,0,0,0,18,125,1,0,0,0,20,132,1,0,0,0,22,146,1,0,0,0,24,156,1,0,
        0,0,26,158,1,0,0,0,28,166,1,0,0,0,30,172,1,0,0,0,32,180,1,0,0,0,
        34,196,1,0,0,0,36,198,1,0,0,0,38,200,1,0,0,0,40,204,1,0,0,0,42,206,
        1,0,0,0,44,231,1,0,0,0,46,48,3,2,1,0,47,46,1,0,0,0,48,49,1,0,0,0,
        49,47,1,0,0,0,49,50,1,0,0,0,50,1,1,0,0,0,51,60,3,4,2,0,52,60,3,6,
        3,0,53,60,3,8,4,0,54,60,3,12,6,0,55,60,3,14,7,0,56,60,3,20,10,0,
        57,60,3,22,11,0,58,60,3,40,20,0,59,51,1,0,0,0,59,52,1,0,0,0,59,53,
        1,0,0,0,59,54,1,0,0,0,59,55,1,0,0,0,59,56,1,0,0,0,59,57,1,0,0,0,
        59,58,1,0,0,0,60,3,1,0,0,0,61,62,5,29,0,0,62,63,5,1,0,0,63,64,3,
        30,15,0,64,5,1,0,0,0,65,66,5,29,0,0,66,67,3,36,18,0,67,68,5,1,0,
        0,68,69,3,30,15,0,69,7,1,0,0,0,70,71,5,29,0,0,71,72,5,1,0,0,72,73,
        5,2,0,0,73,74,3,10,5,0,74,75,5,3,0,0,75,9,1,0,0,0,76,81,3,30,15,
        0,77,78,5,4,0,0,78,80,3,30,15,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,
        1,0,0,0,81,82,1,0,0,0,82,11,1,0,0,0,83,81,1,0,0,0,84,85,5,29,0,0,
        85,86,5,1,0,0,86,87,3,30,15,0,87,13,1,0,0,0,88,94,5,5,0,0,89,90,
        5,6,0,0,90,91,3,24,12,0,91,92,5,7,0,0,92,95,1,0,0,0,93,95,3,24,12,
        0,94,89,1,0,0,0,94,93,1,0,0,0,95,96,1,0,0,0,96,98,5,8,0,0,97,99,
        3,2,1,0,98,97,1,0,0,0,99,100,1,0,0,0,100,98,1,0,0,0,100,101,1,0,
        0,0,101,105,1,0,0,0,102,104,3,16,8,0,103,102,1,0,0,0,104,107,1,0,
        0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,109,1,0,0,0,107,105,1,0,
        0,0,108,110,3,18,9,0,109,108,1,0,0,0,109,110,1,0,0,0,110,15,1,0,
        0,0,111,117,5,9,0,0,112,113,5,6,0,0,113,114,3,24,12,0,114,115,5,
        7,0,0,115,118,1,0,0,0,116,118,3,24,12,0,117,112,1,0,0,0,117,116,
        1,0,0,0,118,119,1,0,0,0,119,121,5,8,0,0,120,122,3,2,1,0,121,120,
        1,0,0,0,122,123,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,17,1,
        0,0,0,125,126,5,10,0,0,126,128,5,8,0,0,127,129,3,2,1,0,128,127,1,
        0,0,0,129,130,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,19,1,0,
        0,0,132,138,5,11,0,0,133,134,5,6,0,0,134,135,3,24,12,0,135,136,5,
        7,0,0,136,139,1,0,0,0,137,139,3,24,12,0,138,133,1,0,0,0,138,137,
        1,0,0,0,139,140,1,0,0,0,140,142,5,8,0,0,141,143,3,2,1,0,142,141,
        1,0,0,0,143,144,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,21,1,
        0,0,0,146,147,5,12,0,0,147,148,5,29,0,0,148,149,5,13,0,0,149,150,
        3,30,15,0,150,152,5,8,0,0,151,153,3,2,1,0,152,151,1,0,0,0,153,154,
        1,0,0,0,154,152,1,0,0,0,154,155,1,0,0,0,155,23,1,0,0,0,156,157,3,
        26,13,0,157,25,1,0,0,0,158,163,3,28,14,0,159,160,7,0,0,0,160,162,
        3,28,14,0,161,159,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,
        1,0,0,0,164,27,1,0,0,0,165,163,1,0,0,0,166,170,3,30,15,0,167,168,
        3,38,19,0,168,169,3,30,15,0,169,171,1,0,0,0,170,167,1,0,0,0,170,
        171,1,0,0,0,171,29,1,0,0,0,172,177,3,32,16,0,173,174,7,1,0,0,174,
        176,3,32,16,0,175,173,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,
        178,1,0,0,0,178,31,1,0,0,0,179,177,1,0,0,0,180,185,3,34,17,0,181,
        182,7,2,0,0,182,184,3,34,17,0,183,181,1,0,0,0,184,187,1,0,0,0,185,
        183,1,0,0,0,185,186,1,0,0,0,186,33,1,0,0,0,187,185,1,0,0,0,188,197,
        5,27,0,0,189,197,5,28,0,0,190,197,5,31,0,0,191,197,5,29,0,0,192,
        193,5,6,0,0,193,194,3,30,15,0,194,195,5,7,0,0,195,197,1,0,0,0,196,
        188,1,0,0,0,196,189,1,0,0,0,196,190,1,0,0,0,196,191,1,0,0,0,196,
        192,1,0,0,0,197,35,1,0,0,0,198,199,7,3,0,0,199,37,1,0,0,0,200,201,
        7,4,0,0,201,39,1,0,0,0,202,205,3,42,21,0,203,205,3,44,22,0,204,202,
        1,0,0,0,204,203,1,0,0,0,205,41,1,0,0,0,206,210,5,23,0,0,207,209,
        9,0,0,0,208,207,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,210,211,
        1,0,0,0,211,213,1,0,0,0,212,210,1,0,0,0,213,214,5,24,0,0,214,43,
        1,0,0,0,215,219,5,25,0,0,216,218,9,0,0,0,217,216,1,0,0,0,218,221,
        1,0,0,0,219,220,1,0,0,0,219,217,1,0,0,0,220,222,1,0,0,0,221,219,
        1,0,0,0,222,232,5,25,0,0,223,227,5,26,0,0,224,226,9,0,0,0,225,224,
        1,0,0,0,226,229,1,0,0,0,227,228,1,0,0,0,227,225,1,0,0,0,228,230,
        1,0,0,0,229,227,1,0,0,0,230,232,5,26,0,0,231,215,1,0,0,0,231,223,
        1,0,0,0,232,45,1,0,0,0,23,49,59,81,94,100,105,109,117,123,130,138,
        144,154,163,170,177,185,196,204,210,219,227,231
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'['", "']'", "','", "'if'", "'('", 
                     "')'", "':'", "'elif'", "'else'", "'while'", "'for'", 
                     "'in'", "'and'", "'or'", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'!='", "'not'", "'#'", "'\\n'", "'\"\"\"'", 
                     "'''''", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "FLOAT", 
                      "ID", "WS", "STRING", "ADD", "SUB", "MUL", "DIV", 
                      "MOD" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_arithmetic_operation = 3
    RULE_array_declaration = 4
    RULE_array_elements = 5
    RULE_variable_declaration = 6
    RULE_if_statement = 7
    RULE_elif_statement = 8
    RULE_else_statement = 9
    RULE_while_loop = 10
    RULE_for_loop = 11
    RULE_condition = 12
    RULE_and_condition = 13
    RULE_or_condition = 14
    RULE_expression = 15
    RULE_term = 16
    RULE_factor = 17
    RULE_arith_op = 18
    RULE_relational_op = 19
    RULE_comment = 20
    RULE_single_line_comment = 21
    RULE_multi_line_comment = 22

    ruleNames =  [ "program", "statement", "assignment", "arithmetic_operation", 
                   "array_declaration", "array_elements", "variable_declaration", 
                   "if_statement", "elif_statement", "else_statement", "while_loop", 
                   "for_loop", "condition", "and_condition", "or_condition", 
                   "expression", "term", "factor", "arith_op", "relational_op", 
                   "comment", "single_line_comment", "multi_line_comment" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    INT=27
    FLOAT=28
    ID=29
    WS=30
    STRING=31
    ADD=32
    SUB=33
    MUL=34
    DIV=35
    MOD=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.StatementContext,i)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ArithmeticParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.statement()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 645928992) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ArithmeticParser.AssignmentContext,0)


        def arithmetic_operation(self):
            return self.getTypedRuleContext(ArithmeticParser.Arithmetic_operationContext,0)


        def array_declaration(self):
            return self.getTypedRuleContext(ArithmeticParser.Array_declarationContext,0)


        def variable_declaration(self):
            return self.getTypedRuleContext(ArithmeticParser.Variable_declarationContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ArithmeticParser.If_statementContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(ArithmeticParser.While_loopContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(ArithmeticParser.For_loopContext,0)


        def comment(self):
            return self.getTypedRuleContext(ArithmeticParser.CommentContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ArithmeticParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.arithmetic_operation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.array_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.variable_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.if_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.while_loop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.for_loop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 58
                self.comment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArithmeticParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(ArithmeticParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ArithmeticParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ArithmeticParser.ID)
            self.state = 62
            self.match(ArithmeticParser.T__0)
            self.state = 63
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Arith_opContext

        def ID(self):
            return self.getToken(ArithmeticParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(ArithmeticParser.ExpressionContext,0)


        def arith_op(self):
            return self.getTypedRuleContext(ArithmeticParser.Arith_opContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_arithmetic_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_operation" ):
                listener.enterArithmetic_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_operation" ):
                listener.exitArithmetic_operation(self)




    def arithmetic_operation(self):

        localctx = ArithmeticParser.Arithmetic_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arithmetic_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(ArithmeticParser.ID)
            self.state = 66
            localctx.op = self.arith_op()
            self.state = 67
            self.match(ArithmeticParser.T__0)
            self.state = 68
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArithmeticParser.ID, 0)

        def array_elements(self):
            return self.getTypedRuleContext(ArithmeticParser.Array_elementsContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_array_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_declaration" ):
                listener.enterArray_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_declaration" ):
                listener.exitArray_declaration(self)




    def array_declaration(self):

        localctx = ArithmeticParser.Array_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_array_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(ArithmeticParser.ID)
            self.state = 71
            self.match(ArithmeticParser.T__0)
            self.state = 72
            self.match(ArithmeticParser.T__1)
            self.state = 73
            self.array_elements()
            self.state = 74
            self.match(ArithmeticParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_array_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_elements" ):
                listener.enterArray_elements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_elements" ):
                listener.exitArray_elements(self)




    def array_elements(self):

        localctx = ArithmeticParser.Array_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.expression()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 77
                self.match(ArithmeticParser.T__3)
                self.state = 78
                self.expression()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArithmeticParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(ArithmeticParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)




    def variable_declaration(self):

        localctx = ArithmeticParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(ArithmeticParser.ID)
            self.state = 85
            self.match(ArithmeticParser.T__0)
            self.state = 86
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(ArithmeticParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.StatementContext,i)


        def elif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.Elif_statementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.Elif_statementContext,i)


        def else_statement(self):
            return self.getTypedRuleContext(ArithmeticParser.Else_statementContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = ArithmeticParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ArithmeticParser.T__4)
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 89
                self.match(ArithmeticParser.T__5)
                self.state = 90
                self.condition()
                self.state = 91
                self.match(ArithmeticParser.T__6)
                pass

            elif la_ == 2:
                self.state = 93
                self.condition()
                pass


            self.state = 96
            self.match(ArithmeticParser.T__7)
            self.state = 98 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 97
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 100 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 102
                    self.elif_statement() 
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 108
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(ArithmeticParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.StatementContext,i)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_elif_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_statement" ):
                listener.enterElif_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_statement" ):
                listener.exitElif_statement(self)




    def elif_statement(self):

        localctx = ArithmeticParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(ArithmeticParser.T__8)
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 112
                self.match(ArithmeticParser.T__5)
                self.state = 113
                self.condition()
                self.state = 114
                self.match(ArithmeticParser.T__6)
                pass

            elif la_ == 2:
                self.state = 116
                self.condition()
                pass


            self.state = 119
            self.match(ArithmeticParser.T__7)
            self.state = 121 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 120
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 123 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.StatementContext,i)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_else_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_statement" ):
                listener.enterElse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_statement" ):
                listener.exitElse_statement(self)




    def else_statement(self):

        localctx = ArithmeticParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(ArithmeticParser.T__9)
            self.state = 126
            self.match(ArithmeticParser.T__7)
            self.state = 128 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 127
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 130 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(ArithmeticParser.ConditionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.StatementContext,i)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)




    def while_loop(self):

        localctx = ArithmeticParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(ArithmeticParser.T__10)
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 133
                self.match(ArithmeticParser.T__5)
                self.state = 134
                self.condition()
                self.state = 135
                self.match(ArithmeticParser.T__6)
                pass

            elif la_ == 2:
                self.state = 137
                self.condition()
                pass


            self.state = 140
            self.match(ArithmeticParser.T__7)
            self.state = 142 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 141
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 144 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArithmeticParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(ArithmeticParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.StatementContext,i)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)




    def for_loop(self):

        localctx = ArithmeticParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ArithmeticParser.T__11)
            self.state = 147
            self.match(ArithmeticParser.ID)
            self.state = 148
            self.match(ArithmeticParser.T__12)
            self.state = 149
            self.expression()
            self.state = 150
            self.match(ArithmeticParser.T__7)
            self.state = 152 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 151
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 154 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_condition(self):
            return self.getTypedRuleContext(ArithmeticParser.And_conditionContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = ArithmeticParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.and_condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class And_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.Or_conditionContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.Or_conditionContext,i)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_and_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd_condition" ):
                listener.enterAnd_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd_condition" ):
                listener.exitAnd_condition(self)




    def and_condition(self):

        localctx = ArithmeticParser.And_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_and_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.or_condition()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14 or _la==15:
                self.state = 159
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 160
                self.or_condition()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.ExpressionContext,i)


        def relational_op(self):
            return self.getTypedRuleContext(ArithmeticParser.Relational_opContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_or_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_condition" ):
                listener.enterOr_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_condition" ):
                listener.exitOr_condition(self)




    def or_condition(self):

        localctx = ArithmeticParser.Or_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_or_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.expression()
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 167
                self.relational_op()
                self.state = 168
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.TermContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.TermContext,i)


        def ADD(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.ADD)
            else:
                return self.getToken(ArithmeticParser.ADD, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.SUB)
            else:
                return self.getToken(ArithmeticParser.SUB, i)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ArithmeticParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.term()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==33:
                self.state = 173
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 174
                self.term()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticParser.FactorContext)
            else:
                return self.getTypedRuleContext(ArithmeticParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MUL)
            else:
                return self.getToken(ArithmeticParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.DIV)
            else:
                return self.getToken(ArithmeticParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.MOD)
            else:
                return self.getToken(ArithmeticParser.MOD, i)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = ArithmeticParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.factor()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0):
                self.state = 181
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 182
                self.factor()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ArithmeticParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ArithmeticParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(ArithmeticParser.STRING, 0)

        def ID(self):
            return self.getToken(ArithmeticParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(ArithmeticParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = ArithmeticParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_factor)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(ArithmeticParser.INT)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(ArithmeticParser.FLOAT)
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.match(ArithmeticParser.STRING)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.match(ArithmeticParser.ID)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 192
                self.match(ArithmeticParser.T__5)
                self.state = 193
                self.expression()
                self.state = 194
                self.match(ArithmeticParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arith_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(ArithmeticParser.ADD, 0)

        def SUB(self):
            return self.getToken(ArithmeticParser.SUB, 0)

        def MUL(self):
            return self.getToken(ArithmeticParser.MUL, 0)

        def DIV(self):
            return self.getToken(ArithmeticParser.DIV, 0)

        def MOD(self):
            return self.getToken(ArithmeticParser.MOD, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_arith_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArith_op" ):
                listener.enterArith_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArith_op" ):
                listener.exitArith_op(self)




    def arith_op(self):

        localctx = ArithmeticParser.Arith_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arith_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 133143986176) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithmeticParser.RULE_relational_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational_op" ):
                listener.enterRelational_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational_op" ):
                listener.exitRelational_op(self)




    def relational_op(self):

        localctx = ArithmeticParser.Relational_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relational_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8372224) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_line_comment(self):
            return self.getTypedRuleContext(ArithmeticParser.Single_line_commentContext,0)


        def multi_line_comment(self):
            return self.getTypedRuleContext(ArithmeticParser.Multi_line_commentContext,0)


        def getRuleIndex(self):
            return ArithmeticParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = ArithmeticParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.state = 202
                self.single_line_comment()
                pass
            elif token in [25, 26]:
                self.state = 203
                self.multi_line_comment()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_line_commentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithmeticParser.RULE_single_line_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle_line_comment" ):
                listener.enterSingle_line_comment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle_line_comment" ):
                listener.exitSingle_line_comment(self)




    def single_line_comment(self):

        localctx = ArithmeticParser.Single_line_commentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_single_line_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(ArithmeticParser.T__22)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 207
                    self.matchWildcard() 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 213
            self.match(ArithmeticParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_line_commentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ArithmeticParser.RULE_multi_line_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulti_line_comment" ):
                listener.enterMulti_line_comment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulti_line_comment" ):
                listener.exitMulti_line_comment(self)




    def multi_line_comment(self):

        localctx = ArithmeticParser.Multi_line_commentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_multi_line_comment)
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(ArithmeticParser.T__24)
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 216
                        self.matchWildcard() 
                    self.state = 221
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                self.state = 222
                self.match(ArithmeticParser.T__24)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(ArithmeticParser.T__25)
                self.state = 227
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 224
                        self.matchWildcard() 
                    self.state = 229
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                self.state = 230
                self.match(ArithmeticParser.T__25)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





