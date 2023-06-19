from compiler.syntactic.expressions import DeclarationListExpression
from compiler import TokenList as Tk

class CParser():
   def __init__(self, tokens) -> None:
      self.tokens = tokens
   
   def analyze(self):
      expression = DeclarationListExpression(self.tokens)
      if expression.interpret():
         self.tokens = expression.tokens
         if(self.tokens[0].name == Tk.TK_EOF):
            print("PASSOU")
         else: 
            print("REPROVOU")
      else:
         print("REPROVOU")