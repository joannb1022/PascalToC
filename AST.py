class Empty:
    def __str__(self):
        return "empty"

    def convert(self):
        return ""


class Program:
    def __init__(self, program_heading, type, var, proc_of_func, comp):
        self.program_heading = program_heading
        self.type = type
        self.var = var
        self.proc_or_func = proc_of_func
        self.comp = comp

    def __str__(self):
        return f"program "

    def convert(self):
        output = ""
        output += "#include <stdio.h> \n \n"
        if not isinstance(self.proc_or_func, Empty):
            output += self.proc_or_func.convert()
        if not isinstance(self.program_heading, Empty):
            output += self.program_heading.convert()
        if not isinstance(self.type, Empty):
            output += self.type.convert()
        if not isinstance(self.var, Empty):
            output += self.var.convert()
        if not isinstance(self.comp, Empty):
            output += self.comp.convert()
        output += "return 0\n }"
        return output


class ProgramHeading:
    def __init__(self, identifier):
        self.identifier = identifier

    def convert(self):
        output = ""
        output += "int main(){ \n"
        return output


class Block:
    def __init__(self, declaration_part, statement_part):
        self.declaration_part = declaration_part
        self.statement_part = statement_part

    def __str__(self):
        return "block: "

    def convert(self):
        output = ""
        if not isinstance(self.declaration_part, Empty):
            output += f"{self.declaration_part.convert()}\n"
        if not isinstance(self.statement_part, Empty):
            output += f"{self.statement_part.convert()}\n"
        return output


class Declaration:
    def __init__(self, type_definition_part, variable_declaration_part, procedure_or_function_declaration_part):
        self.type_definition_part = type_definition_part
        self.variable_definition_part = variable_declaration_part
        self.proc_func_part = procedure_or_function_declaration_part

    def __str__(self):
        return "dec"

    def convert(self):
        output = ""
        if not isinstance(self.type_definition_part, Empty):
            print("hej")
            output += f"{self.type_definition_part.convert()}\n"
        if not isinstance(self.variable_definition_part, Empty):
            output += f"{self.variable_definition_part.convert()}\n"
        if not isinstance(self.proc_func_part, Empty):
            output += f"{self.proc_func_part.convert()}\n"
        return output


class IdentifierList:
    def __init__(self, identifier, identifier_list):
        self.identifier = identifier
        self.identifier_list = identifier_list

    def __str__(self):
        return "hej"

    def convert(self):
        return f"{self.identifier.convert()},{self.identifier_list.convert()}"


class FunctionCall:
    def __init__(self, identifier, variables_list):
        self.identifier = identifier
        self.variables_list = variables_list

    def __str__(self):
        return f"function_call: {self.identifier}({self.variables_list}) \n"

    def convert(self):
        return f"{self.identifier.convert()}({self.variables_list.convert()})"


class ArrayType:
    def __init__(self, identifier, idx1, idx2, type):
        self.identifier = identifier
        self.idx1 = idx1
        self.idx2 = idx2
        self.type = type

    def __str__(self):
        return f"arrat"

    def convert(self):
        output = ""
        output += f"{self.type.convert()} {self.identifier.convert()}[{self.idx2 - self.idx1}]; "
        return output


class TypeDefinition:
    def __init__(self, identifier, type):
        self.identifier = identifier
        self.type = type

    def __str__(self):
        return "type"

    def convert(self):
        return f"{self.type.convert} "


class Real:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"real: {self.value} \n"

    def convert(self):
        return f"{self.value}f"


class Integer:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"integer: {self.value} \n"

    def convert(self):
        return f"{self.value}"


class String:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"string: {self.value} \n"

    def convert(self):
        return f"\"{self.value[1:-1]}\""


class Char:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"char: {self.value}\n"

    def convert(self):
        return f"\'{self.value[1:-1]}\'"


class Identifier:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}\n"

    def convert(self, data_type = None):
        if data_type:
            return f" {data_type.convert()} " + str(self.name)
        return str(self.name)


class Term:
    def __init__(self, term):
        self.term = term

    def __str__(self):
        return f"term: {self.term}\n"

    def convert(self):
        print("hello")
        return f"{self.term.convert()}"
        # if f"{self.term}"[0:-1] == "term: true":
        #     return "1"
        # elif f"{self.term}"[0:-1] == "term: false":
        #     return "0"
        # elif isinstance(self.term, Expression):
        #     return f"({self.term.convert()})"
        # elif self.no:
        #     return f"!{self.term.convert()}"
        # else:
        #     return f"{self.term.convert()}"


class Sign:
    def __init__(self, sign):
        self.sign = sign

    def __str__(self):
        return f"sign: {self.sign}"

    def convert(self):
        if self.sign == "div":
            return "/"
        elif self.sign == "mod":
            return "%"
        elif self.sign == "=":
            return "=="
        elif self.sign == "<>":
            return "!="
        else:
            return f"{self.sign}"


class AndOr:
    def __init__(self, operator):
        self.operator = operator

    def __str__(self):
        return f"and_or: {self.operator} \n"

    def convert(self):
        if self.operator == "and":
            return "&&"
        else:
            return "||"


class Expression:
    def __init__(self, expr1, sign, expr2):
        self.expr1 = expr1
        self.sign = sign
        self.expr2 = expr2

    def __str__(self):
        return f"expression: {self.expr1} {self.sign} {self.expr2}\n"

    def convert(self):
        return f"{self.expr1.convert()} {self.sign.convert()} {self.expr2.convert()}"

class AssignmentList:
    def __init__(self, assignmet, list):
        self.assignment = assignmet
        self.list = list
        print(list)

    def convert(self):
        output = ""
        output += f"{self.assignment.convert()}"
        output += f"{self.list.convert()}"
        return output


class Assignment:
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    def __str__(self):
        return f"assignment: {self.identifier} := {self.expression}"

    def convert(self):
        output = ""
        output += self.identifier.convert() + " = " + str(self.expression.convert()) + ";\n"
        return output

class For:
    def __init__(self, assignment, operator, expression, statement):
        self.assignment = assignment
        self.operator = operator
        self.expression = expression
        self.statement = statement

    def __str__(self):
        return f"for_statement: for {self.assignment} {self.operator} {self.expression} do {self.statement}\n"

    def convert(self):
        if self.operator == "to":
            return f"for({self.assignment.convert()[:-1]} {self.assignment.identifier.convert()} <= {self.expression.convert()}; {self.assignment.identifier.convert()}++)" + "{ \n" + self.statement.convert() + "}\n"
        else:
            return f"for({self.assignment.convert()[:-1]} {self.assignment.identifier.convert()} >= {self.expression.convert()}; {self.assignment.identifier.convert()}--)" + "{ \n" + self.statement.convert() + "\n}\n"


class While:
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def __str__(self):
        return f"while: while {self.expression} do {self.statement}\n"

    def convert(self):
        return "while(" + self.expression.convert() + ") {\n" + self.statement.convert() + "}\n"


class If:
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def __str__(self):
        return f"If: if {self.expression} then {self.statement}\n"

    def convert(self):
        return "if(" + self.expression.convert() + "){\n" + self.statement.convert() + "}\n"


class IfElse:
    def __init__(self, expression, statement1, statement2):
        self.expression = expression
        self.statement1 = statement1
        self.statement2 = statement2

    def __str__(self):
        return f"If: if {self.expression} then {self.statement1} else {self.statement2}\n"

    def convert(self):
        return "if(" + self.expression.convert() + "){\n" + self.statement1.convert() + "} else {\n" + self.statement2.convert() + "}\n"


class VariablesList:
    def __init__(self, variables, expression):
        self.variables = variables
        self.expression = expression

    def __str__(self):
        return f"variables list: {self.variables}, {self.expression}\n"

    def convert(self):
        output = f"{self.variables.convert()}, {self.expression.convert()}"
        return output


class ProcOrFunCall:
    def __init__(self, identifier, variables=None):
        self.identifier = identifier
        self.variables = variables

    def __str__(self):
        return f"procedure or function call: {self.identifier}{self.variables}\n"

    def convert(self):
        if f"{self.identifier}"[0:-1] == "write":
            self.identifier = Identifier("printf")
        elif f"{self.identifier}"[0:-1] == "readln":
            self.identifier = Identifier("scanf")
        if self.variables is None:
            return f"{self.identifier.convert()}();\n"
        else:
            return f"{self.identifier.convert()}({self.variables.convert()});\n"

class StatementPart:
    def __init__(self, statement):
        self.statement = statement

    def convert(self):
        print("daD")
        output = f"{self.statement.convert()}"
        return output

class StatementList:
    def __init__(self, part, list):
        self.part = part
        self.list = list
    def covert(self):
        output = ""
        output += f"{self.part.convert()} \n {self.list.convert()}"

class Type:
    def __init__(self, typename):
        self.typename = typename

    def __str__(self):
        return f"type: {self.typename}"

    def convert(self):
        if self.typename == "integer":
            return "int"
        elif self.typename == "real":
            return "float"
        elif self.typename == "boolean":
            return "int"
        elif self.typename == "string":
            return "char"
        else:
            return f"{self.typename}"

class SimpleTypeName:
    def __init__(self, typename):
        self.typename = typename

    def __str__(self):
        return f"type: {self.typename}"

    def convert(self):
        if self.typename == "integer":
            return "int"
        elif self.typename == "real":
            return "float"
        elif self.typename == "boolean":
            return "int"
        elif self.typename == "string":
            return "char"
        else:
            return f"{self.typename}"


class Parameters:
    def __init__(self, names_list, type):
        self.names_list = names_list
        self.type = type

    def __str__(self):
        return f"parameter: {self.names_list}: {self.type}\n"

    def convert(self):
        output = ""
        output += f"{self.names_list.convert(self.type)}"
        return output


class NamesList:
    def __init__(self, name, name_list, comma=False):
        self.name = name
        self.name_list = name_list
        self.comma = comma

    def convert(self, data_type = None):
        output = ""
        output += f"{data_type.convert()}  {self.name.convert()}"
        output += ","
        output += f"{self.name_list.convert(data_type)}"
        return output


class FunctionDeclaration:
    def __init__(self, function_heading, block):
        self.function_heading = function_heading
        self.block = block

    def convert(self):
        output = ""
        output += f"{self.function_heading.convert()}"
        output += f"{self.block.convert()}"
        output += f"\n return {self.function_heading.identifier.convert()}"
        output += "\n\n"
        return output


class FunctionHeading:
    def __init__(self, identifier, parameters, type):
        self.identifier = identifier
        self.type = type
        self.parameters = parameters

    def convert(self):
        output = f"{self.type.convert()}"

        if f"{self.type}" == "type: string":
            output += "*"
        output += f" {self.identifier.convert()}"
        output += "("
        if not isinstance(self.parameters, Empty):
            output += f"{self.parameters.convert()}"
        output += "){ \n "
        output += f"{self.type.convert()} {self.identifier.convert()}; \n"
        return output


class Function:
    def __init__(self, declaration, proc_or_func):
        self.declaration = declaration
        self.proc_or_func = proc_or_func

    def __str__(self):
        return f"procedure or function: {self.declaration}; {self.proc_or_func}\n"

    def convert(self):
        return f"{self.declaration.convert()}\n{self.proc_or_func.convert()}"


class Variable:
    def __init__(self, identifier, typename):
        self.identifier = identifier
        self.typename = typename

    def convert(self):
        if f"{self.typename}" == "type: string":
            return f"{self.typename.convert()} *{self.identifier.convert()};"
        else:
            return f"{self.typename.convert()} {self.identifier.convert()};"


class VariableDeclaration:
    def __init__(self, identifier_list, typename):
        self.identifier_list = identifier_list
        self.typename = typename

    def convert(self):
        res = ""
        res += f"{self.typename.convert()} {self.identifier_list.convert()}; \n"
        return res


class VariableDeclarationList:
    def __init__(self, variable, varlist):
        self.variable = variable
        self.varlist = varlist

    def convert(self):
        return f"{self.variable.convert()}\n{self.varlist.convert()}"
