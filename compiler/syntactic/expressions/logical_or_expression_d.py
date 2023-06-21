from .expression import Expression
from .logical_and_expression import LogicalAndExpression
from compiler import TokenList as Tk

class LogicalOrExpressionD(Expression):

   def interpret(self):
      if self.check_tokens(Tk.TK_LOGICAL_OR):
         if (self.interpret_expression(LogicalAndExpression) and
               self.interpret_expression(LogicalOrExpressionD)):
            return True
         return False
      return True