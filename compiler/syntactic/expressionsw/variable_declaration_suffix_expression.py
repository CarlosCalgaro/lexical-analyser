from .expression import Expression
from .array_suffix_expression import ArraySuffixExpression
from compiler import TokenList as Tk


class VariableDeclarationSuffixExpression(Expression):

   def interpret(self):
      self.print_tree(f"Variable Suffix", 5)
      array_suffix_expression = ArraySuffixExpression(self.tokens)
      array_suffix_expression.interpret()
      self.tokens = array_suffix_expression.tokens
      return True