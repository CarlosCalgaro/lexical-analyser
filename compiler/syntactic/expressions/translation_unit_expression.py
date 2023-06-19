from .expression import Expression
from .declaration_list_expression import DeclarationListExpression
from compiler import TokenList as Tk

class TranslationUnitExpression(Expression):

  def interpret(self):
    self.print_tree('Translation_Unit')
    expression = DeclarationListExpression(self.tokens)
    if expression.interpret():
        self.tokens = expression.tokens
        if(self.tokens[0].name == Tk.TK_EOF):
          return True
    return False