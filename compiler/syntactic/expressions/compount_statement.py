from .expression import Expression
from compiler import TokenList as Tk
from .statement_list import StatementList
class CompoundStatement(Expression):

   def interpret(self):
      if self.check_tokens(Tk.TK_OPEN_BRACE):
            print("AQUI")
            if self.interpret_expression(StatementList) and self.check_tokens(Tk.TK_CLOSE_BRACE):
               return True
            elif self.check_tokens(Tk.TK_CLOSE_BRACE):
               return True
      return False