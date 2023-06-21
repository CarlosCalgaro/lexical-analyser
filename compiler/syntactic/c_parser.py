from compiler.syntactic.expressions import TranslationUnit

class CParser():
   def __init__(self, tokens) -> None:
      self.tokens = tokens
   
   def analyze(self):
    start_expression = TranslationUnit(self.tokens)
    if start_expression.interpret():
      print("PASSOU")
    else:
      print("REPROVOU")