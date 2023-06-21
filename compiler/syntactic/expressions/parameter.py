from .expression import Expression
from .type_specifier import TypeSpecifier
from .variable_name import VariableName

class Parameter(Expression):
    
    def interpret(self):
      if self.interpret_expression(TypeSpecifier):
         if self.interpret_expression(VariableName):
            return True
      return False