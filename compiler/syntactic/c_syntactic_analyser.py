from compiler.syntactic import SyntacticAnalyser
from compiler import TokenList as Tk

class CSyntacticAnalyser(SyntacticAnalyser):
   QUALIFIER_LIST = [Tk.TK_UNSIGNED, Tk.TK_LONG]
   def __init__(self, token_list) -> None:
      super().__init__(token_list)

   def analyze(self) -> bool:
      if self.type_qualifier():
         print("PASSOU")
      else:
         print("REPROVOU")

   def type_qualifier(self) -> bool:
      print("In type_qualifier()")
      if self.token() in self.QUALIFIER_LIST:
         return True
      elif self.type_qualifier():
         return True
      else:
         return False
   def translation_unit(self) -> bool:
      if self.external_declaration():
         return True
      if self.translation_unit():
         if self.external_declaration():
            return True
      return False

   def external_declaration(self) -> bool:
      if self.function_definition() or self.declaration():
         return True
      return False

   def function_definition(self) -> bool:
      pass

   def declaration(self) -> bool:
      pass
