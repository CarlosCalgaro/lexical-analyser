from .expression import Expression
from .parameter_expression import ParameterExpression
from compiler import TokenList as Tk

class ParametersListExpression(Expression):
   def interpret(self):
      self.print_tree('Parameters List Expression', 4)
      if self.interpret_expression(ParameterExpression):
         if self.check_token()
         return True
      return False
      # if self.interpret_expression(Param) and self.interpret_expression(VariableNameExpression):
         # if self.check_parenthesis(): # Open Parenthesis
            # if self.interpret_parameters_list():
               # return True

      return False

   def check_parenthesis(self, close = False):
      expected_token = Tk.TK_OPEN_PARENTHESIS if close else Tk.TK_CLOSE_PARENTHESIS
      if self.current_token_name() == expected_token:
         self.consume_token()
         return True
      return False