from .expression import Expression
from compiler import TokenList as Tk

class TypeSpecifierLongExpression(Expression):

   def interpret(self):
      self.print_tree('Type Specifier LONG', 5)
      return self.interpret_long_token()

   def interpret_long_token(self):
      if self.current_token_name() == Tk.TK_LONG:
         self.print_tree(f"- Consumed {self.current_token_name()}", 6)
         self.consume_token()
         if self.current_token_name() == Tk.TK_LONG:
            self.print_tree(f"- Consumed {self.current_token_name()}", 6)
            self.consume_token()
         return True
      return False