from .expression import Expression
from compiler import TokenList as Tk
from .iteration_statement import IterationStatement

class Statement(Expression):

   def interpret(self):
      if self.interpret_expression(IterationStatement):
         return True
      return False
