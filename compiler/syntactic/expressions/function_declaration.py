from .expression import Expression
from .type_specifier import TypeSpecifier
from compiler import TokenList as Tk
from .variable_name import VariableName
from .parameters_list import ParametersList
from .compount_statement import CompoundStatement

# Precisa Remover ambiguidade
# function_declaration -> 
#   type_specifier function_name ( parameter_list ) compound_statement | 
#   type_specifier function_name ( ) compound_statement 
class FunctionDeclaration(Expression):

   def interpret(self):
      if (self.interpret_expression(TypeSpecifier) and self.interpret_expression(VariableName)):
         if self.check_tokens(Tk.TK_OPEN_PARENTHESIS) and (self.interpret_expression(ParametersList) or True):
            if self.check_tokens(Tk.TK_CLOSE_PARENTHESIS):
               if self.interpret_expression(CompoundStatement):
                  return True
      return False