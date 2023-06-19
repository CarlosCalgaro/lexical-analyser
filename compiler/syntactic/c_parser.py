from compiler.syntactic.expressions import TranslationUnitExpression

class CParser():
   def __init__(self, tokens) -> None:
      self.tokens = tokens
   
   def analyze(self):
    start_expression = TranslationUnitExpression(self.tokens)
    if start_expression.interpret():
      print("PASSOU")
    else:
      print("REPROVOU")