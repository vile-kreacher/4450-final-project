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
        4,1,29,166,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,4,0,38,8,0,11,0,12,0,
        39,1,1,1,1,1,1,1,1,1,1,3,1,47,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,67,8,5,10,5,12,5,70,
        9,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,82,8,7,1,7,1,7,4,
        7,86,8,7,11,7,12,7,87,1,7,5,7,91,8,7,10,7,12,7,94,9,7,1,7,3,7,97,
        8,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,105,8,8,1,8,1,8,4,8,109,8,8,11,8,
        12,8,110,1,9,1,9,1,9,4,9,116,8,9,11,9,12,9,117,1,10,1,10,1,11,1,
        11,1,11,5,11,125,8,11,10,11,12,11,128,9,11,1,12,1,12,1,12,1,12,3,
        12,134,8,12,1,13,1,13,1,13,5,13,139,8,13,10,13,12,13,142,9,13,1,
        14,1,14,1,14,5,14,147,8,14,10,14,12,14,150,9,14,1,15,1,15,1,15,1,
        15,1,15,1,15,1,15,1,15,3,15,160,8,15,1,16,1,16,1,17,1,17,1,17,0,
        0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,5,1,0,11,
        12,1,0,25,26,1,0,27,29,1,0,25,29,1,0,11,19,168,0,37,1,0,0,0,2,46,
        1,0,0,0,4,48,1,0,0,0,6,52,1,0,0,0,8,57,1,0,0,0,10,63,1,0,0,0,12,
        71,1,0,0,0,14,75,1,0,0,0,16,98,1,0,0,0,18,112,1,0,0,0,20,119,1,0,
        0,0,22,121,1,0,0,0,24,129,1,0,0,0,26,135,1,0,0,0,28,143,1,0,0,0,
        30,159,1,0,0,0,32,161,1,0,0,0,34,163,1,0,0,0,36,38,3,2,1,0,37,36,
        1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,1,1,0,0,0,41,
        47,3,4,2,0,42,47,3,6,3,0,43,47,3,8,4,0,44,47,3,12,6,0,45,47,3,14,
        7,0,46,41,1,0,0,0,46,42,1,0,0,0,46,43,1,0,0,0,46,44,1,0,0,0,46,45,
        1,0,0,0,47,3,1,0,0,0,48,49,5,22,0,0,49,50,5,1,0,0,50,51,3,26,13,
        0,51,5,1,0,0,0,52,53,5,22,0,0,53,54,3,32,16,0,54,55,5,1,0,0,55,56,
        3,26,13,0,56,7,1,0,0,0,57,58,5,22,0,0,58,59,5,1,0,0,59,60,5,2,0,
        0,60,61,3,10,5,0,61,62,5,3,0,0,62,9,1,0,0,0,63,68,3,26,13,0,64,65,
        5,4,0,0,65,67,3,26,13,0,66,64,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,
        0,68,69,1,0,0,0,69,11,1,0,0,0,70,68,1,0,0,0,71,72,5,22,0,0,72,73,
        5,1,0,0,73,74,3,26,13,0,74,13,1,0,0,0,75,81,5,5,0,0,76,77,5,6,0,
        0,77,78,3,20,10,0,78,79,5,7,0,0,79,82,1,0,0,0,80,82,3,20,10,0,81,
        76,1,0,0,0,81,80,1,0,0,0,82,83,1,0,0,0,83,85,5,8,0,0,84,86,3,2,1,
        0,85,84,1,0,0,0,86,87,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,92,
        1,0,0,0,89,91,3,16,8,0,90,89,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,
        92,93,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,95,97,3,18,9,0,96,95,1,
        0,0,0,96,97,1,0,0,0,97,15,1,0,0,0,98,104,5,9,0,0,99,100,5,6,0,0,
        100,101,3,20,10,0,101,102,5,7,0,0,102,105,1,0,0,0,103,105,3,20,10,
        0,104,99,1,0,0,0,104,103,1,0,0,0,105,106,1,0,0,0,106,108,5,8,0,0,
        107,109,3,2,1,0,108,107,1,0,0,0,109,110,1,0,0,0,110,108,1,0,0,0,
        110,111,1,0,0,0,111,17,1,0,0,0,112,113,5,10,0,0,113,115,5,8,0,0,
        114,116,3,2,1,0,115,114,1,0,0,0,116,117,1,0,0,0,117,115,1,0,0,0,
        117,118,1,0,0,0,118,19,1,0,0,0,119,120,3,22,11,0,120,21,1,0,0,0,
        121,126,3,24,12,0,122,123,7,0,0,0,123,125,3,24,12,0,124,122,1,0,
        0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,23,1,0,0,
        0,128,126,1,0,0,0,129,133,3,26,13,0,130,131,3,34,17,0,131,132,3,
        26,13,0,132,134,1,0,0,0,133,130,1,0,0,0,133,134,1,0,0,0,134,25,1,
        0,0,0,135,140,3,28,14,0,136,137,7,1,0,0,137,139,3,28,14,0,138,136,
        1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,27,1,
        0,0,0,142,140,1,0,0,0,143,148,3,30,15,0,144,145,7,2,0,0,145,147,
        3,30,15,0,146,144,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,
        1,0,0,0,149,29,1,0,0,0,150,148,1,0,0,0,151,160,5,20,0,0,152,160,
        5,21,0,0,153,160,5,24,0,0,154,160,5,22,0,0,155,156,5,6,0,0,156,157,
        3,26,13,0,157,158,5,7,0,0,158,160,1,0,0,0,159,151,1,0,0,0,159,152,
        1,0,0,0,159,153,1,0,0,0,159,154,1,0,0,0,159,155,1,0,0,0,160,31,1,
        0,0,0,161,162,7,3,0,0,162,33,1,0,0,0,163,164,7,4,0,0,164,35,1,0,
        0,0,15,39,46,68,81,87,92,96,104,110,117,126,133,140,148,159
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'['", "']'", "','", "'if'", "'('", 
                     "')'", "':'", "'elif'", "'else'", "'and'", "'or'", 
                     "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", "'not'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "FLOAT", "ID", "WS", "STRING", "ADD", "SUB", 
                      "MUL", "DIV", "MOD" ]

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
    RULE_condition = 10
    RULE_and_condition = 11
    RULE_or_condition = 12
    RULE_expression = 13
    RULE_term = 14
    RULE_factor = 15
    RULE_arith_op = 16
    RULE_relational_op = 17

    ruleNames =  [ "program", "statement", "assignment", "arithmetic_operation", 
                   "array_declaration", "array_elements", "variable_declaration", 
                   "if_statement", "elif_statement", "else_statement", "condition", 
                   "and_condition", "or_condition", "expression", "term", 
                   "factor", "arith_op", "relational_op" ]

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
    INT=20
    FLOAT=21
    ID=22
    WS=23
    STRING=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MOD=29

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
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.statement()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==22):
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
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.arithmetic_operation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.array_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.variable_declaration()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.if_statement()
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
            self.state = 48
            self.match(ArithmeticParser.ID)
            self.state = 49
            self.match(ArithmeticParser.T__0)
            self.state = 50
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
            self.state = 52
            self.match(ArithmeticParser.ID)
            self.state = 53
            localctx.op = self.arith_op()
            self.state = 54
            self.match(ArithmeticParser.T__0)
            self.state = 55
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
            self.state = 57
            self.match(ArithmeticParser.ID)
            self.state = 58
            self.match(ArithmeticParser.T__0)
            self.state = 59
            self.match(ArithmeticParser.T__1)
            self.state = 60
            self.array_elements()
            self.state = 61
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
            self.state = 63
            self.expression()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 64
                self.match(ArithmeticParser.T__3)
                self.state = 65
                self.expression()
                self.state = 70
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
            self.state = 71
            self.match(ArithmeticParser.ID)
            self.state = 72
            self.match(ArithmeticParser.T__0)
            self.state = 73
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
            self.state = 75
            self.match(ArithmeticParser.T__4)
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 76
                self.match(ArithmeticParser.T__5)
                self.state = 77
                self.condition()
                self.state = 78
                self.match(ArithmeticParser.T__6)
                pass

            elif la_ == 2:
                self.state = 80
                self.condition()
                pass


            self.state = 83
            self.match(ArithmeticParser.T__7)
            self.state = 85 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 84
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 87 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 92
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 89
                    self.elif_statement() 
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 95
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
            self.state = 98
            self.match(ArithmeticParser.T__8)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 99
                self.match(ArithmeticParser.T__5)
                self.state = 100
                self.condition()
                self.state = 101
                self.match(ArithmeticParser.T__6)
                pass

            elif la_ == 2:
                self.state = 103
                self.condition()
                pass


            self.state = 106
            self.match(ArithmeticParser.T__7)
            self.state = 108 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 107
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 110 
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
            self.state = 112
            self.match(ArithmeticParser.T__9)
            self.state = 113
            self.match(ArithmeticParser.T__7)
            self.state = 115 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 114
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 117 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
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
        self.enterRule(localctx, 22, self.RULE_and_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.or_condition()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11 or _la==12:
                self.state = 122
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 123
                self.or_condition()
                self.state = 128
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
        self.enterRule(localctx, 24, self.RULE_or_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.expression()
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 130
                self.relational_op()
                self.state = 131
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
        self.enterRule(localctx, 26, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.term()
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 136
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 137
                self.term()
                self.state = 142
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
        self.enterRule(localctx, 28, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.factor()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0):
                self.state = 144
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 145
                self.factor()
                self.state = 150
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
        self.enterRule(localctx, 30, self.RULE_factor)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(ArithmeticParser.INT)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(ArithmeticParser.FLOAT)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 153
                self.match(ArithmeticParser.STRING)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 154
                self.match(ArithmeticParser.ID)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 155
                self.match(ArithmeticParser.T__5)
                self.state = 156
                self.expression()
                self.state = 157
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
        self.enterRule(localctx, 32, self.RULE_arith_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1040187392) != 0)):
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
        self.enterRule(localctx, 34, self.RULE_relational_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1046528) != 0)):
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





