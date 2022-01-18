import logging

from ply import yacc

from tokens import *
from grammar import *

if __name__ == '__main__':
    lexer = lex.lex()

    logging.basicConfig(
        level=logging.DEBUG,
        filename="parselog.txt",
        filemode="w",
        format="%(filename)10s:%(lineno)4d:%(message)s"
    )

    log = logging.getLogger()
    parser = yacc.yacc(start="program", debug=True, errorlog=log)

    # test = open('test/test_while.pas', 'r')
    # test = open('test/test_function.pas', 'r')
    test = open('test/test_array.pas', 'r')
    data = test.read()

    ast = parser.parse(input=data, lexer=lexer)

    # file = open('test/test_while.c', 'w')
    # file = open('test/test_function.c', 'w')
    file = open('test/test_array.c', 'w')

    file.write(ast.convert())
    file.close()
