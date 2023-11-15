# Generated from Arithmetic.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ArithmeticParser import ArithmeticParser
else:
    from ArithmeticParser import ArithmeticParser

# This class defines a complete listener for a parse tree produced by ArithmeticParser.
class ArithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by ArithmeticParser#program.
    def enterProgram(self, ctx:ArithmeticParser.ProgramContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#program.
    def exitProgram(self, ctx:ArithmeticParser.ProgramContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#statement.
    def enterStatement(self, ctx:ArithmeticParser.StatementContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#statement.
    def exitStatement(self, ctx:ArithmeticParser.StatementContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#assignment.
    def enterAssignment(self, ctx:ArithmeticParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#assignment.
    def exitAssignment(self, ctx:ArithmeticParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#arithmetic_operation.
    def enterArithmetic_operation(self, ctx:ArithmeticParser.Arithmetic_operationContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#arithmetic_operation.
    def exitArithmetic_operation(self, ctx:ArithmeticParser.Arithmetic_operationContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#array_declaration.
    def enterArray_declaration(self, ctx:ArithmeticParser.Array_declarationContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#array_declaration.
    def exitArray_declaration(self, ctx:ArithmeticParser.Array_declarationContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#array_elements.
    def enterArray_elements(self, ctx:ArithmeticParser.Array_elementsContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#array_elements.
    def exitArray_elements(self, ctx:ArithmeticParser.Array_elementsContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#variable_declaration.
    def enterVariable_declaration(self, ctx:ArithmeticParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#variable_declaration.
    def exitVariable_declaration(self, ctx:ArithmeticParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#expression.
    def enterExpression(self, ctx:ArithmeticParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#expression.
    def exitExpression(self, ctx:ArithmeticParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#term.
    def enterTerm(self, ctx:ArithmeticParser.TermContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#term.
    def exitTerm(self, ctx:ArithmeticParser.TermContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#factor.
    def enterFactor(self, ctx:ArithmeticParser.FactorContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#factor.
    def exitFactor(self, ctx:ArithmeticParser.FactorContext):
        pass


    # Enter a parse tree produced by ArithmeticParser#arith_op.
    def enterArith_op(self, ctx:ArithmeticParser.Arith_opContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#arith_op.
    def exitArith_op(self, ctx:ArithmeticParser.Arith_opContext):
        pass



del ArithmeticParser