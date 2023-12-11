
import sys
from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ArithmeticLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ArithmeticParser(stream)
    tree = parser.program()
    print(tree)

if __name__ == '__main__':
    main(sys.argv)