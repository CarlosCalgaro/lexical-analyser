from .expression import Expression
from .variable_declaration_expression import VariableDeclarationExpression
# from compiler.syntactic.expressions import Expression

from compiler import TokenList as Tk

class DeclarationExpression(Expression):
   def __init__(self, tokens) -> None:
      self.tokens = tokens

   def interpret(self):
      variable_declaration_expression = VariableDeclarationExpression(self.tokens)
      print("In Declaration Exprssion")
      if variable_declaration_expression.interpret():
         self.tokens = variable_declaration_expression.tokens
         return True
      return False