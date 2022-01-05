import ply.lex as lex


class Lexer(object):
    def __init__(self):
        self.lexer = lex.lex(object=self)

    def input_data(self, data):
        self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    literals = ['+', '-', '*', '/']

    reserved = {
        # logic operators
        'if': 'IF',
        'then': 'THEN',
        'else': 'ELSE',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',

        # loops
        'while': 'WHILE',
        'for': 'FOR',
        'repeat': 'REPEAT',
        'do': 'DO',
        'to': 'TO',
        'downto': 'DOWNTO',
        'until': 'UNTIL',

        # beginning and end
        'program': 'PROGRAM',
        'begin': 'BEGIN',
        'end': 'END',
        'var': 'VAR',

        # procedures and fucntions
        'procedure': 'PROCEDURE',
        'function': 'FUNCTION',

        'writeLn': 'WRITELN'
    }

    # List of token names.
    tokens = [
                 # arithmetics, comparison and parenthesis
                 'PLUS',
                 'MINUS',
                 'TIMES',
                 'DIVIDE',

                 'EQ',
                 'NEQ',
                 'GREATER',
                 'LESS',
                 'GEQ',
                 'LEQ',

                 'LPAREN',
                 'RPAREN',

                 # assignments
                 'ID',
                 'ASSIGNMENT',
                 'SEMICOLON',
                 'COLON',
                 'COMMA',
                 'DOT',

                 # types
                 'INTEGER',
                 'REAL',
                 'STRING',
                 'BOOLEAN',
                 'CHAR'

             ] + list(reserved.values())

    # Regular expression rules for simple tokens
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_EQ = r'=='
    t_NEQ = r'\<\>"'
    t_LESS = r'<'
    t_GREATER = r'>'
    t_LEQ = r'<='
    t_GEQ = r'>='
    t_ASSIGNMENT = r':='
    t_SEMICOLON = r';'
    t_COLON = r':'
    t_COMMA = r','
    t_DOT = '\.'

    def t_ID(self, t):
        r"[a-zA-Z][a-zA-Z0-9]*"
        if t.value.lower() in Lexer.reserved:
            t.type = Lexer.reserved[t.value.lower()]
        return t

    def t_REAL(self, t):
        r"(\-)*[0-9]+\.[0-9]+"
        t.value = float(t.value)
        return t

    def t_INTEGER(self, t):
        r"(\-)*[0-9]+"
        t.value = int(t.value)
        return t

    def t_CHAR(self, t):
        r"(\'([^\\\'])\')"
        return t

    def t_STRING(self, t):
        r"\'([^\\\']|(\\.))*\'"
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = ' \t'

    def t_error(self, t):
        print('Illegal character ', t.value[0])
        t.lexer.skip(1)
