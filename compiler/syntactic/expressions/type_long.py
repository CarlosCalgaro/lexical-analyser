from .expression import Expression
from compiler import TokenList as Tk

class TypeLong(Expression):

   def interpret(self):
      if self.check_tokens(Tk.TK_LONG):
         if self.check_tokens(Tk.TK_LONG):
            return True
         return True
      return False