from .expression import Expression
from compiler import TokenList as Tk, TYPE_SPECIFIER_LIST
from .type_long import TypeLong

class TypeSpecifier(Expression):

   def interpret(self):
      if self.interpret_expression(TypeLong):
         if self.check_tokens(Tk.TK_INT):
            return True
      if self.check_tokens(TYPE_SPECIFIER_LIST):
         return True
      return False