program -> declaration_list

declaration_list -> declaration | declaration declaration_list

declaration -> variable_declaration | function_declaration

variable_declaration -> type_specifier variable_declaration_prefix variable_name variable_declaration_suffix ;

variable_name -> TK_CONST | TK_ID

type_specifier -> int | float | char | double | type_specifier_long

type_specifier_long -> long int | long long int

variable_declaration_prefix -> * variable_declaration_prefix | * | vazio

variable_declaration_suffix -> array_suffix | vazio

array_suffix -> [ constant_expression ]
 
pointer_suffix -> * pointer_suffix | *














function_declaration -> type_specifier function_name ( parameter_list ) compound_statement

parameter_list -> parameter | parameter , parameter_list

parameter -> type_specifier parameter_name

compound_statement -> { statement_list }

statement_list -> statement | statement statement_list

statement -> while_statement | do_while_statement | for_statement | if_statement | compound_statement | expression_statement

while_statement -> while ( expression ) statement

do_while_statement -> do statement while ( expression ) ;

for_statement -> for ( for_init ; for_condition ; for_iteration ) statement

for_init -> expression_statement | variable_declaration

for_condition -> expression

for_iteration -> expression

if_statement -> if ( expression ) statement | if ( expression ) statement else statement

expression_statement -> expression ;

expression -> assignment_expression | expression , assignment_expression

assignment_expression -> unary_expression assignment_operator assignment_expression | conditional_expression

assignment_operator -> = | += | -= | *= | /= | %= | >>= | <<=

conditional_expression -> logical_or_expression | logical_or_expression ? expression : conditional_expression

logical_or_expression -> logical_and_expression | logical_or_expression || logical_and_expression

logical_and_expression -> bitwise_or_expression | logical_and_expression && bitwise_or_expression

bitwise_or_expression -> bitwise_xor_expression | bitwise_or_expression | bitwise_xor_expression

bitwise_xor_expression -> bitwise_and_expression | bitwise_xor_expression ^ bitwise_and_expression

bitwise_and_expression -> equality_expression | bitwise_and_expression & equality_expression

equality_expression -> relational_expression | equality_expression == relational_expression | equality_expression != relational_expression

relational_expression -> additive_expression | relational_expression > additive_expression | relational_expression < additive_expression | relational_expression >= additive_expression | relational_expression <= additive_expression

additive_expression -> multiplicative_expression | additive_expression + multiplicative_expression | additive_expression - multiplicative_expression

multiplicative_expression -> unary_expression | multiplicative_expression * unary_expression | multiplicative_expression / unary_expression | multiplicative_expression % unary_expression

unary_expression -> postfix_expression | - unary_expression | ! unary_expression | ~ unary_expression

postfix_expression -> primary_expression | postfix_expression [ expression ] | postfix_expression ( argument_expression_list ) | postfix_expression . identifier

argument_expression_list -> assignment_expression | assignment_expression , argument_expression_list

primary_expression -> identifier | constant | ( expression )