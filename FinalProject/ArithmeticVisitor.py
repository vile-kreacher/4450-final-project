# Generated from Arithmetic.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ArithmeticParser import ArithmeticParser
else:
    from ArithmeticParser import ArithmeticParser

# This class defines a complete generic visitor for a parse tree produced by ArithmeticParser.

class ArithmeticVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ArithmeticParser#program.
    def visitProgram(self, ctx:ArithmeticParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#statement.
    def visitStatement(self, ctx:ArithmeticParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#assignment.
    def visitAssignment(self, ctx:ArithmeticParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#arithmetic_operation.
    def visitArithmetic_operation(self, ctx:ArithmeticParser.Arithmetic_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#array_declaration.
    def visitArray_declaration(self, ctx:ArithmeticParser.Array_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#array_elements.
    def visitArray_elements(self, ctx:ArithmeticParser.Array_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#variable_declaration.
    def visitVariable_declaration(self, ctx:ArithmeticParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#expression.
    def visitExpression(self, ctx:ArithmeticParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#term.
    def visitTerm(self, ctx:ArithmeticParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#factor.
    def visitFactor(self, ctx:ArithmeticParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ArithmeticParser#arith_op.
    def visitArith_op(self, ctx:ArithmeticParser.Arith_opContext):
        return self.visitChildren(ctx)



del ArithmeticParser