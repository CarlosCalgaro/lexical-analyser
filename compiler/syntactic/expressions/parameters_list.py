from .expression import Expression
from .parameter import Parameter
from compiler import TokenList as Tk

class ParametersList(Expression):

   def interpret(self):
      if self.interpret_expression(Parameter):
         if self.check_tokens(Tk.TK_COMMA):
            if self.interpret_expression(ParametersList):
               return True
            return False
         return True
      return False