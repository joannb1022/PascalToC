from AST import *
import sys

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'EQ', 'NEQ', 'LTE', 'LT', 'GT', 'GTE'),
    ('left', 'OR', 'AND'),
)


def p_empty(p):
    """
    empty :
    """
    p[0] = Empty()


def p_program(p):
    """
    program : program_heading type_definition_part variable_declaration_part function_declaration_part compound_statement_dot
    """
    p[0] = Program(p[1], p[2], p[3], p[4], p[5])


def p_program_heading(p):
    """
    program_heading : PROGRAM identifier SEMICOLON
    """
    p[0] = ProgramHeading(p[1])


def p_declaration_part(p):
    """
    declaration_part : type_definition_part variable_declaration_part function_declaration_part
    """
    p[0] = Declaration(p[1], p[2], p[3])


def p_block(p):
    """
    block :  declaration_part statement_part
    """
    p[0] = Block(p[1], p[2])


def p_type_definition_part(p):
    """
    type_definition_part : TYPE type_definition_list
                            | empty
    """
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_type_definition_list(p):
    """
    type_definition_list : type_definition
                        | type_definition type_definition_list
    """

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = TypeDefinitionList(p[1], p[2])


def p_variable_declaration_part(p):
    """
    variable_declaration_part : VAR variable_declaration_list
                                | empty
    """
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_function_declaration_part(p):
    """
    function_declaration_part : function_declaration function_declaration_part
                                | empty
    """
    if len(p) > 2:
        p[0] = Function(p[1], p[2])
    else:
        p[0] = p[1]


def p_function_declaration(p):
    """ function_declaration : function_heading SEMICOLON block"""

    p[0] = FunctionDeclaration(p[1], p[3])


def p_function_heading(p):
    """ function_heading : FUNCTION identifier LPAREN parameters RPAREN COLON simple_type_name"""
    p[0] = FunctionHeading(p[2], p[4], p[7])


def p_parameters(p):
    """ parameters : names_list COLON simple_type_name
                    | names_list COLON simple_type_name SEMICOLON parameters"""
    p[0] = Parameters(p[1], p[3])


def p_names_list(p):
    """ names_list : identifier
                    | identifier COMMA names_list
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = NamesList(p[1], p[3], True)


def p_type_definition(p):
    """
    type_definition : identifier EQ ARRAY LPARENARR INTEGER DD INTEGER RPARENARR OF simple_type_name SEMICOLON

    """

    p[0] = ArrayTypeDefinition(p[1], p[5], p[7], p[10])


def p_statement_part(p):
    """
    statement_part : compound_statement
                    | assignment_list
                    | while_statement_list
                    | if_else_statement_list
                    | empty
    """
    if len(p) == 2:
        p[0] = p[1]


def p_while_statement_list(p):
    """ while_statement_list : while_statement statement_part """

    p[0] = List(p[1], p[2])

def p_if_else_statement_list(p):
    """ if_else_statement_list : if_else_statement statement_part """
    p[0] = List(p[1], p[2])


def p_single_statement_part(p):
    """
    single_statement_part : assignment
                    | while_statement
                    | if_else_statement
                    | empty
    """
    if len(p) == 2:
        p[0] = p[1]


def p_while_statement(p):
    """
    while_statement : WHILE expression DO single_statement_part
                    | WHILE expression DO BEGIN statement_part END SEMICOLON
    """
    if len(p) == 5:
        p[0] = While(p[2], p[4])
    else:
        p[0] = While(p[2], p[5])


def p_then_statement(p):
    """ then_statement : single_statement_part
                        | BEGIN statement_part END SEMICOLON"""

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_single_statement_part_else(p):
    """ single_statement_part_else : assignment_else
                                    | while_statement
                                    | if_else_statement
                                    | empty
                                    """
    p[0] = p[1]

def p_assignment_else(p):
    """ assignment_else :  identifier ASSIGNMENT expression
                        | identifier LPARENARR integer RPARENARR ASSIGNMENT expression """

    if len(p) == 4:
        p[0] = Assignment(p[1], p[3])
    else:
        p[0] = ArrayAssignment(p[1], p[3], p[6])

def p_else_statement(p):
    """ else_statement : single_statement_part_else
                        | BEGIN statement_part END  """

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_if_else_statement(p):
    """
    if_else_statement : IF expression THEN then_statement
                        | IF expression THEN else_statement ELSE then_statement
    """

    if len(p) == 5:
        p[0] = If(p[2], p[4])
    else:
        p[0] = IfElse(p[2], p[4], p[6])


def p_compound_statement(p):
    """ compound_statement : BEGIN statement_part END SEMICOLON
                             """
    p[0] = StatementPart(p[2])


def p_compound_statement_dot(p):
    """ compound_statement_dot : BEGIN statement_part END DOT
                             """
    p[0] = StatementPart(p[2])


def p_assignment_list(p):
    """
     assignment_list : assignment statement_part
    """

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = List(p[1], p[2])


def p_assignment(p):
    """ assignment : identifier ASSIGNMENT expression SEMICOLON
                     | identifier LPARENARR integer RPARENARR ASSIGNMENT expression SEMICOLON
                 """
    if len(p) == 5:
        p[0] = Assignment(p[1], p[3])
    else:
        p[0] = ArrayAssignment(p[1], p[3], p[6])


def p_expression(p):
    """ expression : term
                    | expression sign term
                    | expression and_or expression"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Expression(p[1], p[2], p[3])


def p_and_or(p):
    """ and_or : AND
                | OR"""
    p[0] = AndOr(p[1])


def p_sign(p):
    """ sign : PLUS
            | MINUS
            | EQ
            | NEQ
            | GT
            | LT
            | GTE
            | LTE"""

    p[0] = Sign(p[1])


def p_term(p):
    """ term : integer
            | real
            | char
            | string
            | function_call
            | identifier
    """

    p[0] = Term(p[1])


def p_integer(p):
    """ integer : INTEGER"""
    p[0] = Integer(p[1])


def p_real(p):
    """ real : REAL"""
    p[0] = Real(p[1])


def p_string(p):
    """string : STRING"""
    p[0] = String(p[1])


def p_char(p):
    """ char : CHAR"""
    p[0] = Char(p[1])


def p_function_call(p):
    """ function_call : identifier LPAREN identifier_list RPAREN"""
    p[0] = FunctionCall(p[1], p[3])


def p_variable_declaration_list(p):
    """
    variable_declaration_list : variable_declaration
                                | variable_declaration variable_declaration_list

    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = VariableDeclarationList(p[1], p[2])


def p_variable_declaration(p):
    """
    variable_declaration : identifier_list COLON simple_type_name SEMICOLON
                        | identifier COLON simple_type_name SEMICOLON
                        | identifier COLON identifier SEMICOLON
                        | identifier COLON ARRAY LPARENARR INTEGER DD INTEGER RPARENARR OF simple_type_name SEMICOLON
    """
    if len(p) == 2:
        p[0] = p[1]
    if len(p) == 5:
        p[0] = VariableDeclaration(p[1], p[3])
    else:
        p[0] = ArrayType(p[1], p[5], p[7], p[10])


def p_identifier_list(p):
    """
    identifier_list : identifier COMMA identifier_list
                    | identifier
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = IdentifierList(p[1], p[3])


def p_simple_type_name(p):
    """ simple_type_name : SSTRING
                        | SCHAR
                        | SREAL
                        | SINTEGER
                        """

    p[0] = SimpleTypeName(p[1])


def p_identifier(p):
    """ identifier : IDENTIFIER """
    p[0] = Identifier(str(p[1]))


def p_error(p):
    print("ERROR", p.lineno)
    sys.exit()
