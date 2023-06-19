from .expression import Expression
from compiler import TYPE_SPECIFIER_LIST


class TypeSpecifierExpression(Expression):
   def __init__(self, tokens) -> None:
      self.tokens = tokens

   def interpret(self):
      print("In Type Specifier")
      if self.tokens[0].name in TYPE_SPECIFIER_LIST:
         self.tokens = self.tokens[1:]
         print(f"ACHOU {self.tokens[0].string()}")
         return True, self.tokens[1:]
      return False, self.tokens