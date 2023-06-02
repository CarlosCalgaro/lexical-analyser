# define Python user-defined exceptions
class LexicErrorException(Exception):
   """Exception raised for lexical errors found in compiled file
   Attributes:
      file being compiled
   """

   def __init__(self, file, message="Lexic error in file at"):
      self.file = file
      self.message = message
      super().__init__(f"{self.message}:\n {self.file}")