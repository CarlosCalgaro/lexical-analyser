from compiler import TokenList as Tk

class Token():
   def __init__(self, name, match, line=0, column=0) -> None:
      self.name = name
      self.match = match
      self.line = line
      self.column = column

   def string(self):
      return self.match.group(0)