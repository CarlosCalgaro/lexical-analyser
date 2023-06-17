start translation_unit

translation_unit
   external_declaration
   | translation_unit external_declaration

external_declaration
   function_definition
   | declaration

declaration
   declaration_specifiers ;
   | declaration_specifiers init_declarator_list ;

init_declarator_list
   init_declarator
   | init_declarator_list , init_declarator

declaration_specifiers
   type_qualifier type_name
   | type_name

init_declarator
   declarator
   | declarator = initializer

initializer
   assignment_expression
   | { initializer_list }
   | { initializer_list ',' } ??????

initializer_list
   initializer
   | initializer_list , initializer

assignment_expression
   conditional_expression ??????
   | unary_expression assignment_operator assignment_expression

unary_expression
   postfix_expression 
   | ++ unary_expression
   | -- unary_expression

postfix_expression
   primary_expression
   | postfix_expression [ expression ]
   | postfix_expression ()
   | postfix_expression
   | postfix_expression '(' argument_expression_list ')'
   | postfix_expression '.' IDENTIFIER
   | postfix_expression PTR_OP IDENTIFIER
   | postfix_expression INC_OP
   | postfix_expression DEC_OP

primary_expression
   IDENTIFIER
   | CONSTANT
   | STRING_LITERAL
   | ( expression )

assignment_operator (Tem mais mas depois eu faco)
   =

type_qualifier
   type_qualifier long
   | type_qualifier unsigned
   | unsigned
   | long

type_name
   int
   | float
   | char
   | double

ptr_operator
   * 