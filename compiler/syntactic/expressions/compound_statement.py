from .expression import Expression
from .statement_list import StatementList
from compiler import TokenList as Tk

class CompoundStatement(Expression):

   def interpret(self):
      if self.check_tokens(Tk.TK_OPEN_BRACE):
         if self.interpret_expression(StatementList):
            return True
         if self.check_tokens(Tk.TK_CLOSE_BRACE):
            return True
      return False