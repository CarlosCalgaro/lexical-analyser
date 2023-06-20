from .expression import Expression
from compiler import TokenList as Tk


class VariableDeclarationPrefixExpression(Expression):

   def interpret(self):
      self.print_tree(f"Variable Prefix", 5)
      if self.current_token_name() == Tk.TK_ASTERISK:
         self.print_tree(f" - Consumed {self.current_token_name()}", 6)
         self.consume_token()
         variable_declaration_prefix = VariableDeclarationPrefixExpression(self.tokens)
         if variable_declaration_prefix.interpret():
            self.tokens = variable_declaration_prefix.tokens
      return True