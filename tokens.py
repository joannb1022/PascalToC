from ply import lex

tokens = (

    'IDENTIFIER',
    'ASSIGNMENT',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'DD',

    'PROGRAM',
    'DOT',
    'VAR',
    'BEGIN',
    'TYPE',
    'END',
    'IF',
    'THEN',
    'ELSE',
    'WHILE',
    'DO',

    'AND',
    'OR',

    'PLUS',
    'MINUS',
    'EQ',
    'NEQ',
    'LT',
    'GT',
    'LTE',
    'GTE',

    'LPAREN',
    'RPAREN',

    'FUNCTION',

    'INTEGER',
    'REAL',
    'STRING',
    'CHAR',

    'ARRAY',
    'LPARENARR',
    'RPARENARR',
    'OF',

    'SREAL',
    'SINTEGER',
    'SSTRING',
    'SCHAR',
)

# Regular statement rules for tokens.
t_DOT = r"\."

t_ASSIGNMENT = r":="
t_SEMICOLON = r";"
t_COLON = r":"
t_COMMA = r","

t_PLUS = r"\+"
t_MINUS = r"\-"

t_EQ = r"\="
t_NEQ = r"\<\>"
t_LT = r"\<"
t_GT = r"\>"
t_LTE = r"\<\="
t_GTE = r"\>\="

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LPARENARR = r"\["
t_RPARENARR = r"\]"
t_DDD = r"\.."

reserved_keywords = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'type': 'TYPE',
    'begin': 'BEGIN',
    'end': 'END',

    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'and': 'AND',
    'or': 'OR',

    'function': 'FUNCTION',

    'real': 'SREAL',
    'integer': 'SINTEGER',
    'string': 'SSTRING',
    'char': 'SCHAR',
    'array': 'ARRAY',
    'of': 'OF'
}


def t_BOOLEAN(t):
    r"true|false"
    return t


def t_IDENTIFIER(t):
    r"[a-zA-Z][a-zA-Z0-9]*"
    if t.value.lower() in reserved_keywords:
        t.type = reserved_keywords[t.value.lower()]
    return t


def t_REAL(t):
    r"(\-)*[0-9]+\.[0-9]+"
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r"(\-)*[0-9]+"
    t.value = int(t.value)
    return t


def t_CHAR(t):
    r"(\'([^\\\'])\')"
    return t


def t_STRING(t):
    r"\'([^\\\']|(\\.))*\'"
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
