grammar Arithmetic;

INT: [0-9]+;
FLOAT: [0-9]+('.'[0-9]+)?;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\r\n]+ -> skip;
STRING: '\'' ~'\''* '\''
      | '"' ~'"'* '"';

program: statement+;

statement: assignment | arithmetic_operation | array_declaration | variable_declaration;

assignment: ID '=' expression;

arithmetic_operation: ID op=arith_op '=' expression;

array_declaration: ID '=' '[' array_elements ']';

array_elements: expression (',' expression)*;

variable_declaration: ID '=' expression;

expression: term ((ADD | SUB) term)*;

term: factor ((MUL | DIV | MOD) factor)*;

factor: INT | FLOAT | STRING | ID | '(' expression ')';

arith_op: ADD | SUB | MUL | DIV | MOD;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
