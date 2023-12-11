grammar Arithmetic;

INT: [0-9]+;
FLOAT: [0-9]+('.'[0-9]+)?;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \r\t\n]+ -> skip;
STRING: '\'' ~'\''* '\''
      | '"' ~'"'* '"';

program: statement+;

statement: assignment
         | arithmetic_operation
         | array_declaration
         | variable_declaration
         | if_statement
         | while_loop
         | for_loop
         | comment;

assignment: ID '=' expression;

arithmetic_operation: ID op=arith_op '=' expression;

array_declaration: ID '=' '[' array_elements ']';

array_elements: expression (',' expression)*;

variable_declaration: ID '=' expression;

if_statement: 'if' ( '(' condition ')' | condition ) ':' statement+ (elif_statement)* (else_statement)?;

elif_statement: 'elif' ( '(' condition ')' | condition ) ':' statement+;

else_statement: 'else' ':' statement+;

while_loop: 'while' ( '(' condition ')' | condition ) ':' statement+;

for_loop: 'for' ID 'in' expression ':' statement+;

condition: and_condition;

and_condition: or_condition (('and'|'or') or_condition)*;

or_condition: expression (relational_op expression)?;

expression: term ((ADD | SUB) term)*;

term: factor ((MUL | DIV | MOD) factor)*;

factor: INT | FLOAT | STRING | ID | '(' expression ')';

arith_op: ADD | SUB | MUL | DIV | MOD;

relational_op: '<' | '<=' | '>' | '>=' | '==' | '!=' | 'and' | 'or' | 'not';

comment: (single_line_comment | multi_line_comment);

single_line_comment: '#'+ (.)*?;

multi_line_comment: ('"""' | '\'\'\'' ) .*? ('"""' | '\'\'\'' );

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';