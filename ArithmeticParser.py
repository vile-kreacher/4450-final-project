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
        4,1,16,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,52,8,5,10,5,12,5,55,9,5,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,5,7,64,8,7,10,7,12,7,67,9,7,1,8,1,8,1,
        8,5,8,72,8,8,10,8,12,8,75,9,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,
        9,85,8,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,3,1,
        0,12,13,1,0,14,16,1,0,12,16,88,0,23,1,0,0,0,2,31,1,0,0,0,4,33,1,
        0,0,0,6,37,1,0,0,0,8,42,1,0,0,0,10,48,1,0,0,0,12,56,1,0,0,0,14,60,
        1,0,0,0,16,68,1,0,0,0,18,84,1,0,0,0,20,86,1,0,0,0,22,24,3,2,1,0,
        23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,1,1,0,
        0,0,27,32,3,4,2,0,28,32,3,6,3,0,29,32,3,8,4,0,30,32,3,12,6,0,31,
        27,1,0,0,0,31,28,1,0,0,0,31,29,1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,
        0,33,34,5,9,0,0,34,35,5,1,0,0,35,36,3,14,7,0,36,5,1,0,0,0,37,38,
        5,9,0,0,38,39,3,20,10,0,39,40,5,1,0,0,40,41,3,14,7,0,41,7,1,0,0,
        0,42,43,5,9,0,0,43,44,5,1,0,0,44,45,5,2,0,0,45,46,3,10,5,0,46,47,
        5,3,0,0,47,9,1,0,0,0,48,53,3,14,7,0,49,50,5,4,0,0,50,52,3,14,7,0,
        51,49,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,11,1,
        0,0,0,55,53,1,0,0,0,56,57,5,9,0,0,57,58,5,1,0,0,58,59,3,14,7,0,59,
        13,1,0,0,0,60,65,3,16,8,0,61,62,7,0,0,0,62,64,3,16,8,0,63,61,1,0,
        0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,15,1,0,0,0,67,65,
        1,0,0,0,68,73,3,18,9,0,69,70,7,1,0,0,70,72,3,18,9,0,71,69,1,0,0,
        0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,17,1,0,0,0,75,73,
        1,0,0,0,76,85,5,7,0,0,77,85,5,8,0,0,78,85,5,11,0,0,79,85,5,9,0,0,
        80,81,5,5,0,0,81,82,3,14,7,0,82,83,5,6,0,0,83,85,1,0,0,0,84,76,1,
        0,0,0,84,77,1,0,0,0,84,78,1,0,0,0,84,79,1,0,0,0,84,80,1,0,0,0,85,
        19,1,0,0,0,86,87,7,2,0,0,87,21,1,0,0,0,6,25,31,53,65,73,84
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'['", "']'", "','", "'('", "')'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_expression = 7
    RULE_term = 8
    RULE_factor = 9
    RULE_arith_op = 10

    ruleNames =  [ "program", "statement", "assignment", "arithmetic_operation", 
                   "array_declaration", "array_elements", "variable_declaration", 
                   "expression", "term", "factor", "arith_op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    INT=7
    FLOAT=8
    ID=9
    WS=10
    STRING=11
    ADD=12
    SUB=13
    MUL=14
    DIV=15
    MOD=16

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
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
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
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.arithmetic_operation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.array_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.variable_declaration()
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
            self.state = 33
            self.match(ArithmeticParser.ID)
            self.state = 34
            self.match(ArithmeticParser.T__0)
            self.state = 35
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
            self.state = 37
            self.match(ArithmeticParser.ID)
            self.state = 38
            localctx.op = self.arith_op()
            self.state = 39
            self.match(ArithmeticParser.T__0)
            self.state = 40
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
            self.state = 42
            self.match(ArithmeticParser.ID)
            self.state = 43
            self.match(ArithmeticParser.T__0)
            self.state = 44
            self.match(ArithmeticParser.T__1)
            self.state = 45
            self.array_elements()
            self.state = 46
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
            self.state = 48
            self.expression()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 49
                self.match(ArithmeticParser.T__3)
                self.state = 50
                self.expression()
                self.state = 55
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
            self.state = 56
            self.match(ArithmeticParser.ID)
            self.state = 57
            self.match(ArithmeticParser.T__0)
            self.state = 58
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
        self.enterRule(localctx, 14, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.term()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12 or _la==13:
                self.state = 61
                _la = self._input.LA(1)
                if not(_la==12 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 62
                self.term()
                self.state = 67
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
        self.enterRule(localctx, 16, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.factor()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0):
                self.state = 69
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 70
                self.factor()
                self.state = 75
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
        self.enterRule(localctx, 18, self.RULE_factor)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(ArithmeticParser.INT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(ArithmeticParser.FLOAT)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.match(ArithmeticParser.STRING)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.match(ArithmeticParser.ID)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.match(ArithmeticParser.T__4)
                self.state = 81
                self.expression()
                self.state = 82
                self.match(ArithmeticParser.T__5)
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
        self.enterRule(localctx, 20, self.RULE_arith_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0)):
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





