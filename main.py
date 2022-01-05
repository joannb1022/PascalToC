
from ply import lex, yacc
import my_lexer, my_parser

test = open('test.pas', 'r')
data = test.read()
lexer = my_lexer.Lexer()
lexer.input_data(data)

#
while True:
    tok = lexer.token()
    if not tok:
        break
    print("%s - %s " % (tok.type, tok.value))


# lex.lex(debug=True)
# yacc.yacc(debug=True)
#
# parser = my_parser.parser
#
# ast = parser.parse(data, lexer=lexer)
# ast.printTree()