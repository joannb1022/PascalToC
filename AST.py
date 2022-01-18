class Empty:
    def convert(self):
        return ""


class Program:
    def __init__(self, program_heading, data_type, var, func, comp):
        self.program_heading = program_heading
        self.data_type = data_type
        self.var = var
        self.func = func
        self.comp = comp

    def convert(self):
        output = ""
        output += "#include <stdio.h> \n#include <string.h> \n\n"
        if not isinstance(self.func, Empty):
            output += self.func.convert()
        if not isinstance(self.program_heading, Empty):
            output += self.program_heading.convert()
        if not isinstance(self.data_type, Empty):
            output += self.data_type.convert()
        if not isinstance(self.var, Empty):
            output += self.var.convert()
        if not isinstance(self.comp, Empty):
            output += self.comp.convert()
        output += "return 0;\n }"
        return output


class StatementPartList:
    def __init__(self, s_list, statement):
        self.statement = statement
        self.s_list = s_list

    def convert(self):
        output = ""
        output += f"{self.statement.convert()}\n"
        output += f"{self.s_list.convert()}"
        return output


class ProgramHeading:
    def __init__(self, identifier):
        self.id = identifier

    def convert(self):
        output = ""
        output += "int main(){ \n"
        return output


class Block:
    def __init__(self, declaration_part, statement_part):
        self.declaration_part = declaration_part
        self.statement_part = statement_part

    def convert(self):
        output = ""
        if not isinstance(self.declaration_part, Empty):
            output += f"{self.declaration_part.convert()}"
        if not isinstance(self.statement_part, Empty):
            output += f"{self.statement_part.convert()}\n"
        return output


class Declaration:
    def __init__(self, type_definition_part, variable_declaration_part, function_declaration_part):
        self.type_definition_part = type_definition_part
        self.variable_definition_part = variable_declaration_part
        self.func_part = function_declaration_part

    def convert(self):
        output = ""
        if not isinstance(self.type_definition_part, Empty):
            output += f"{self.type_definition_part.convert()}\n"
        if not isinstance(self.variable_definition_part, Empty):
            output += f"{self.variable_definition_part.convert()}"
        if not isinstance(self.func_part, Empty):
            output += f"{self.func_part.convert()}\n"
        return output


class IdentifierList:
    def __init__(self, identifier, id_list):
        self.id = identifier
        self.id_list = id_list

    def convert(self):
        return f"{self.id.convert()},{self.id_list.convert()}"


class FunctionCall:
    def __init__(self, identifier, variables_list):
        self.id = identifier
        self.variables_list = variables_list

    def convert(self):
        return f"{self.id.convert()}({self.variables_list.convert()})"


class ArrayType:
    def __init__(self, identifier, idx1, idx2, data_type):
        self.id = identifier
        self.idx1 = idx1
        self.idx2 = idx2
        self.type = data_type

    def convert(self):
        output = ""
        output += f"{self.type.convert()} {self.id.convert()}[{self.idx2 - self.idx1}]; "
        return output


types = {}


class ArrayTypeDefinition:
    def __init__(self, identifier, idx1, idx2, data_type):
        self.id = identifier
        self.idx1 = idx1
        self.idx2 = idx2
        self.type = data_type

        types.update({f"{identifier.convert()}": data_type})

    def convert(self):
        output = ""
        output += f"{self.type.convert()} {self.id.convert()}[{self.idx2 - self.idx1}]; "
        return output


class ArrayAssignment:
    def __init__(self, identifier, term, expression):
        self.id = identifier
        self.term = term
        self.expression = expression

    def convert(self):
        output = ""
        output += f"{self.id.convert()}[{self.term.convert()}] = "
        output += f"{self.expression.convert()};\n"
        return output


class TypeDefinitionList:
    def __init__(self, data_type, type_list):
        self.type = data_type
        self.type_list = type_list

    def convert(self):
        output = ""
        output += f"{self.type.convert()} \n"
        output += f'{self.type_list.convert()}'
        return output


class Real:
    def __init__(self, value):
        self.value = value

    def convert(self):
        return f"{self.value}f"


class Integer:
    def __init__(self, value):
        self.value = value

    def convert(self):
        return f"{self.value}"


class String:
    def __init__(self, value):
        self.value = value

    def convert(self):
        return f"\"{self.value[1:-1]}\""


class Char:
    def __init__(self, value):
        self.value = value

    def convert(self):
        return f"\'{self.value[1:-1]}\'"


class Identifier:
    def __init__(self, name):
        self.name = name

    def convert(self, data_type=None):
        if data_type:
            return f" {data_type.convert()} " + str(self.name)
        return self.name


class Term:
    def __init__(self, term):
        self.term = term

    def convert(self):
        return f"{self.term.convert()}"


class Sign:
    def __init__(self, sign):
        self.sign = sign

    def convert(self):
        if self.sign == "=":
            return "=="
        elif self.sign == "<>":
            return "!="
        else:
            return f"{self.sign}"


class AndOr:
    def __init__(self, operator):
        self.operator = operator

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

    def convert(self):
        return f"{self.expr1.convert()} {self.sign.convert()} {self.expr2.convert()}"


class AssignmentList:
    def __init__(self, assignmet, as_list):
        self.assignment = assignmet
        self.list = as_list

    def convert(self):
        output = ""
        output += f"{self.assignment.convert()}"
        output += f"{self.list.convert()}"
        return output


class List:
    def __init__(self, statement, my_list):
        self.statement = statement
        self.list = my_list

    def convert(self):
        output = ""
        output += f"{self.statement.convert()}"
        output += f"{self.list.convert()}"
        return output


class Assignment:
    def __init__(self, identifier, expression):
        self.id = identifier
        self.expression = expression

    def convert(self):
        output = ""
        if f"{self.id.convert()}" in strings:
            output += f"strcpy({self.id.convert()}, {self.expression.convert()});\n"
        else:
            output += self.id.convert() + " = " + str(self.expression.convert()) + ";\n"
        return output


class While:
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def convert(self):
        return "while(" + self.expression.convert() + ") {\n" + self.statement.convert() + "}\n"


class If:
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def convert(self):
        return "if(" + self.expression.convert() + "){\n" + self.statement.convert() + "}\n"


class IfElse:
    def __init__(self, expression, statement1, statement2):
        self.expression = expression
        self.statement1 = statement1
        self.statement2 = statement2

    def convert(self):
        return "if(" + self.expression.convert() + "){\n" + self.statement1.convert() + "}\nelse {\n" + self.statement2.convert() + "}\n"


class VariablesList:
    def __init__(self, variables, expression):
        self.variables = variables
        self.expression = expression

    def convert(self):
        output = f"{self.variables.convert()}, {self.expression.convert()}"
        return output


class StatementPart:
    def __init__(self, statement):
        self.statement = statement

    def convert(self):
        output = f"{self.statement.convert()}"
        return output


class SimpleTypeName:
    def __init__(self, data_type):
        self.data_type = data_type

    def convert(self):
        if self.data_type == "integer":
            return "int"
        elif self.data_type == "real":
            return "float"
        elif self.data_type == "string":
            return "char*"
        else:
            return f"{self.data_type}"


class Parameters:
    def __init__(self, names_list, data_type, p_list=None):
        self.names_list = names_list
        self.type = data_type
        self.p_list = p_list

    def convert(self):
        output = ""
        output += f"{self.names_list.convert(self.type)}"
        if self.p_list:
            output += f",{self.p_list.convert()}"
        return output


class NamesList:
    def __init__(self, name, name_list, comma=False):
        self.name = name
        self.name_list = name_list
        self.comma = comma

    def convert(self, data_type=None):
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
        output += f"return {self.function_heading.id.convert()};"
        output += "\n}\n"
        return output


class FunctionHeading:
    def __init__(self, identifier, parameters, data_type):
        self.id = identifier
        self.type = data_type
        self.parameters = parameters

    def convert(self):
        output = f"{self.type.convert()}"
        output += f" {self.id.convert()}"
        output += "("
        if not isinstance(self.parameters, Empty):
            output += f"{self.parameters.convert()}"
        output += "){ \n "
        output += f"{self.type.convert()} {self.id.convert()}; \n"
        return output


class Function:
    def __init__(self, declaration, function):
        self.declaration = declaration
        self.function = function

    def convert(self):
        output = ""
        output += f"{self.declaration.convert()}\n{self.function.convert()}"
        return output


strings = []


class VariableDeclaration:
    def __init__(self, id_list, data_type):
        self.id_list = id_list
        self.data_type = data_type

    def convert(self):
        res = ""
        if isinstance(self.data_type, Identifier):
            res += f"\n{types[self.data_type.convert()].convert()}* {self.id_list.convert()} = {self.data_type.convert()};"
        elif f"{self.data_type}" == "string":
            res += f"char {self.id_list.convert()}[100];\n"
            strings.append(f"{self.id_list.convert()}")
        else:
            res += f"{self.data_type.convert()} {self.id_list.convert()};\n"
        return res


class VariableDeclarationList:
    def __init__(self, variable, varlist):
        self.variable = variable
        self.varlist = varlist

    def convert(self):
        return f"{self.variable.convert()}\n{self.varlist.convert()}"
