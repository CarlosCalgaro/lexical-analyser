from .expression import Expression
from .type_specifier import TypeSpecifier
from .variable_declaration_suffix import VariableDeclarationSuffix
from .variable_declaration_prefix import VariableDeclarationPrefix
from .variable_name import VariableName
from compiler import TokenList as Tk
class VariableDeclaration(Expression):

   def interpret(self):
      if self.interpret_expression(TypeSpecifier):
         self.interpret_expression(VariableDeclarationPrefix)
         if self.interpret_expression(VariableName):
            self.interpret_expression(VariableDeclarationSuffix)
            if self.check_tokens(Tk.TK_SEMICOLON):
               print("Found a variable:")
               self.print_token_list()
               self.consumed_tokens = []
               return True
      return False