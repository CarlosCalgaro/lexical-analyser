from .expression import Expression
from .logical_and_expression import LogicalAndExpression
from .logical_or_expression_d import LogicalOrExpressionD
from compiler import TokenList as Tk

class AssignmentExpression(Expression):

   def interpret(self):
      if (self.interpret_expression(LogicalAndExpression) and 
          self.interpret_expression(LogicalOrExpressionD)):
         return True
      return False