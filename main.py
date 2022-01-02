
from ply import lex, yacc
import my_scanner

test = open('test.pas', 'r')
data = test.read()
lexer = my_scanner.my_lexer
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print("%s - %s " % ( tok.type, tok.value))
#
# lex.lex(debug=True, debuglog=log)
# yacc.yacc(debug=True, debuglog=log)