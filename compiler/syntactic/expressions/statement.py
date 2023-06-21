from .expression import Expression
from .iteration_statement import IterationStatement
from .compound_statement import CompoundStatement

from compiler import TokenList as Tk

class Statement(Expression):

   def interprete(self):
      if self.interpret_expression(IterationStatement) or self.interpret_expression(CompoundStatement):
         return True
      return False

   def interpret(self):
      return True