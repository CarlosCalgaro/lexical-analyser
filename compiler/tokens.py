from enum import Enum, auto

class TokenList(Enum):
   TK_WHITESPACE = auto()
   TK_NEWLINE = auto()
   TK_ARROW = auto()
   TK_LONG = auto()
   TK_UNSIGNED = auto()
   TK_INT = auto()
   TK_FLOAT = auto()
   TK_CHAR = auto()
   TK_DOUBLE = auto()
   TK_STRUCT = auto()
   TK_IF = auto()
   TK_ELSE = auto()
   TK_IDENT = auto()
   TK_WHILE = auto()
   TK_FOR = auto()
   TK_DO = auto()
   TK_SWITCH = auto()
   TK_CASE = auto()
   TK_DEFAULT = auto()
   TK_LOGICAL_AND = auto()
   TK_LOGICAL_OR = auto()
   TK_LOGICAL_EQUAL = auto()
   TK_BITWISE_LEFT_SHIFT = auto()
   TK_BITWISE_RIGHT_SHIFT = auto()
   TK_LOGICAL_GREATER_EQUAL = auto()
   TK_LOGICAL_LESSER_EQUAL = auto()
   TK_LOGICAL_NOT_EQUAL = auto()
   TK_LOGICAL_GREATER = auto()
   TK_LOGICAL_LESSER = auto()
   TK_LOGICAL_NOT = auto()
   TK_BITWISE_AND = auto()
   TK_BITWISE_OR = auto()
   TK_BITWISE_XOR = auto()
   TK_BITWISE_NOT = auto()
   TK_ASSIGNMENT = auto()
   TK_COMMA = auto()
   TK_OPEN_PARENTHESIS = auto()
   TK_CLOSE_PARENTHESIS = auto()
   TK_OPEN_BRACKET = auto()
   TK_CLOSE_BRACKET = auto()
   TK_OPEN_BRACE = auto()
   TK_CLOSE_BRACE = auto()
   TK_SEMICOLON = auto()
   TK_POINT = auto()
   TK_COLON = auto()
   TK_OP = auto()
   TK_CONST = auto()
   TK_ID = auto()
   TK_EOF = auto()
   TK_ASTERISK = auto()
   TK_HYPHEN = auto()
   TK_PLUS = auto()
   TK_SLASH = auto()
   TK_PERCENT = auto()
TOKENS = [
    (TokenList.TK_WHITESPACE, r'^( )'),
    (TokenList.TK_NEWLINE, r'^\n'),
    (TokenList.TK_ARROW, r'^(->)'),
    (TokenList.TK_LONG, r'^\blong\b'),
    (TokenList.TK_UNSIGNED, r'^\bunsigned\b'),
    (TokenList.TK_INT, r'^\bint\b'),
    (TokenList.TK_FLOAT, r'^\bfloat\b'),
    (TokenList.TK_CHAR, r'^\bchar\b'),
    (TokenList.TK_DOUBLE, r'^\bdouble\b'),
    (TokenList.TK_STRUCT, r'^\bstruct\b'),
    (TokenList.TK_IF, r'^\bif\b'),
    (TokenList.TK_ELSE, r'^\belse\b'),
    (TokenList.TK_IDENT, r'^\bident\b'),
    (TokenList.TK_WHILE, r'^\bwhile\b'),
    (TokenList.TK_FOR, r'^\bfor\b'),
    (TokenList.TK_DO, r'^\bdo\b'),
    (TokenList.TK_SWITCH, r'^\bswitch\b'),
    (TokenList.TK_CASE, r'^\bcase\b'),
    (TokenList.TK_DEFAULT, r'^\bdefault\b'),
    (TokenList.TK_LOGICAL_AND, r"^&{2}"),
    (TokenList.TK_LOGICAL_OR, r"^\|{2}"),
    (TokenList.TK_LOGICAL_EQUAL, r"^={2}"),
    (TokenList.TK_BITWISE_LEFT_SHIFT, r"^<{2}"),
    (TokenList.TK_BITWISE_RIGHT_SHIFT, r"^>{2}"),
    (TokenList.TK_LOGICAL_GREATER_EQUAL, r'^\b>=\b'),
    (TokenList.TK_LOGICAL_LESSER_EQUAL, r'^\b<=\b'),
    (TokenList.TK_LOGICAL_NOT_EQUAL, r'^!='),
    (TokenList.TK_LOGICAL_GREATER, r'^>'),
    (TokenList.TK_LOGICAL_LESSER, r'^<'),
    (TokenList.TK_LOGICAL_NOT, r"^\!"),
    (TokenList.TK_BITWISE_AND, r"^&"),
    (TokenList.TK_BITWISE_OR, r"^\|"),
    (TokenList.TK_BITWISE_XOR, r"^\^"),
    (TokenList.TK_BITWISE_NOT, r"^\~"),
    (TokenList.TK_ASSIGNMENT, r"^="),
    (TokenList.TK_COMMA, r'^\,'),
    (TokenList.TK_OPEN_PARENTHESIS, r'^\('),
    (TokenList.TK_CLOSE_PARENTHESIS, r'^\)'),
    (TokenList.TK_OPEN_BRACKET, r"^\["),
    (TokenList.TK_CLOSE_BRACKET, r'^\]'),
    (TokenList.TK_OPEN_BRACE, r'^{'),
    (TokenList.TK_CLOSE_BRACE, r'^}'),
    (TokenList.TK_SEMICOLON, r"^;"),
    (TokenList.TK_POINT, r"^\."),
    (TokenList.TK_COLON, r"^\:"),
    (TokenList.TK_ASTERISK, r"^\*"),
    (TokenList.TK_HYPHEN, r"^\-"),
    (TokenList.TK_PLUS, r"^\+"),
    (TokenList.TK_SLASH, r"^\/"),
    (TokenList.TK_PERCENT, r'^\%'),
    (TokenList.TK_CONST, r"^\d+(\.\d+)?"),
    (TokenList.TK_ID, r'^[a-zA-Z_][a-zA-Z0-9_]*')
]
ASSIGNABLES_LIST = [TokenList.TK_ID]
OPERATOR_LIST = [ TokenList.TK_PLUS, TokenList.TK_HYPHEN, TokenList.TK_ASTERISK, TokenList.TK_SLASH, TokenList.TK_PERCENT]
SPECIFIER_MUTATOR_LIST = [TokenList.TK_UNSIGNED, TokenList.TK_LONG]
TYPE_SPECIFIER_LIST = [TokenList.TK_INT, TokenList.TK_FLOAT, TokenList.TK_CHAR, TokenList.TK_DOUBLE]