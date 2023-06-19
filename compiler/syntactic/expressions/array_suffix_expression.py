from .expression import Expression
from compiler import TokenList as Tk


class ArraySuffixExpression(Expression):

   def interpret(self):
      if self.current_token_name() == Tk.TK_OPEN_BRACKET:
         self.print_tree(f"- Consumed {self.current_token_name()}", 6)
         self.consume_token()
         if self.constant_expression():
            if self.current_token_name() == Tk.TK_CLOSE_BRACKET:
               self.print_tree(f"- Consumed {self.current_token_name()}", 6)
               self.consume_token()
               return True
      return False

   def constant_expression(self):
      if self.current_token_name() in [Tk.TK_ID, Tk.TK_CONST]:
         self.print_tree(f"- Consumed {self.current_token_name()}", 6)
         self.consume_token()
         return True
      return False