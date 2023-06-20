from .expression import Expression
from .type_specifier_expression import TypeSpecifierExpression
from .variable_name_expression import VariableNameExpression
from .parameters_list_expression import ParametersListExpression
from compiler import TokenList as Tk

class FunctionDeclarationExpression(Expression):

   def interpret(self):
      self.print_tree('Function Declaration', 4)
      if self.interpret_expression(TypeSpecifierExpression) and self.interpret_expression(VariableNameExpression):
         if self.check_parenthesis(): # Open Parenthesis
            if self.interpret_parameters_list():
               return True

      return False

   def check_parenthesis(self, close = False):
      expected_token = Tk.TK_OPEN_PARENTHESIS if close else Tk.TK_CLOSE_PARENTHESIS
      if self.current_token_name() == expected_token:
         self.consume_token()
         return True
      return False