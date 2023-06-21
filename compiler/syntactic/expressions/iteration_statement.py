from .expression import Expression
from .language_expression import LanguageExpression
from .statement import Statement
from compiler import TokenList as Tk

class IterationStatement(Expression):

   def __init__(self, tokens):
      self.current_token_list = tokens
      super().__init__(tokens)

   def interpret(self):
      return True
   #    return (self.while_iteration() or self.do_while_iteration())
   
   # def while_iteration(self) -> bool:
   #    if self.check_tokens(Tk.TK_WHILE) and self.check_tokens(Tk.TK_OPEN_PARENTHESIS):
   #       if self.interpret_expression(LanguageExpression):
   #          if self.check_tokens(Tk.TK_CLOSE_PARENTHESIS):
   #             if self.interpret_expression(Statement):
   #                return True
   #    return False

   # def do_while_iteration(self) -> bool:
   #    if self.check_tokens(Tk.TK_DO):
   #       if self.interpret_expression(Statement):
   #          if self.check_tokens(Tk.TK_WHILE) and self.check_tokens(Tk.TK_OPEN_PARENTHESIS):
   #             if self.interpret_expression(LanguageExpression):
   #                if self.check_tokens(Tk.TK_CLOSE_PARENTHESIS) and self.check_tokens(Tk.TK_SEMICOLON):
   #                   return True
   #    return False
