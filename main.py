# #
# # from ply import lex, yacc
# # import my_lexer, my_parser
# #
# # test = open('test.pas', 'r')
# # data = test.read()
# # lexer = my_lexer.Lexer()
# # lexer.input_data(data)
# #
# # #
# # while True:
# #     tok = lexer.token()
# #     if not tok:
# #         break
# #     print("%s - %s " % (tok.type, tok.value))
# #
# #
# # ast = parser.parse(data, lexer=lexer)
# # ast.toC()
#
# import logging
#
# from ply import yacc
# from my_lexer import Lexer
# from my_parser import *
#
#
# if __name__ == '__main__':
#     lexer = Lexer()
#     print(Lexer.tokens)
#     parser = yacc.yacc()
#
#     # test = open(str(sys.argv[1]), 'r')
#     test = open('test1.pas', 'r')
#     data = test.read()
#
#     ast = parser.parse(input=data, lexer=lexer)
#     print(ast)
#     # file = open(str(sys.argv[2]), 'w')
#     # # file = open('tests/test1.c', 'w')
#     # file.write(ast.toC())
#     # file.close()

import logging

from ply import yacc

from tokens import *
from grammar import *

 # m = MyLexer()
 # a = lex.lex(object=m)      # Create a lexer
 #
 # b = a.clone()              # Clone the lexer


if __name__ == '__main__':
    lexer = lex.lex()
    logging.basicConfig(
        level=logging.DEBUG,
        filename="parselog.txt",
        filemode="w",
        format="%(filename)10s:%(lineno)4d:%(message)s"
    )
    print("ge")

    log = logging.getLogger()
    parser = yacc.yacc(start="program", debug=True, errorlog=log)
    print("geh")
    # test = open(str(sys.argv[1]), 'r')
    test = open('test.pas', 'r')
    data = test.read()

    ast = parser.parse(input=data, lexer=lexer)
    print(ast)
    # file = open(str(sys.argv[2]), 'w')
    file = open('test.c', 'w')
    file.write(ast.convert())
    file.close()
