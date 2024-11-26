
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programleftCOMMArightEQUALSleftORleftANDleftEQNEleftLTLEGTGEleftPLUSMINUSleftTIMESDIVIDEMODrightNOTAND ASSERT BREAK CHAR CHAR_CONST COMMA DIVIDE ELSE EQ EQUALS FOR GE GT ID IF INT INT_CONST LBRACE LBRACKET LE LPAREN LT MINUS MOD NE NOT OR PLUS PRINT RBRACE RBRACKET READ RETURN RPAREN SEMI STRING_LITERAL TIMES VOID WHILEprogram  : global_declaration_listglobal_declaration_list : global_declaration\n| global_declaration_list global_declaration\nglobal_declaration    : declarationglobal_declaration    : function_definitionfunction_definition   : type_specifier declarator compound_statementtype_specifier : VOID\n| CHAR\n| INT\ndeclarator : IDdeclarator : LPAREN declarator RPARENdeclarator : declarator LBRACKET constant_expression_opt RBRACKETdeclarator : declarator LPAREN parameter_list_opt RPARENconstant_expression_opt : constant_expression\n| empty\nconstant_expression : binary_expressionbinary_expression : unary_expression\n| binary_expression TIMES  binary_expression\n| binary_expression DIVIDE binary_expression\n| binary_expression MOD    binary_expression\n| binary_expression PLUS   binary_expression\n| binary_expression MINUS  binary_expression\n| binary_expression LT     binary_expression\n| binary_expression LE     binary_expression\n| binary_expression GT     binary_expression\n| binary_expression GE     binary_expression\n| binary_expression EQ     binary_expression\n| binary_expression NE     binary_expression\n| binary_expression AND    binary_expression\n| binary_expression OR     binary_expression\nunary_expression : postfix_expression\n| unary_operator unary_expression\npostfix_expression : primary_expression\n        postfix_expression : postfix_expression LBRACKET expression RBRACKET\n        postfix_expression : postfix_expression LPAREN argument_expression_opt RPAREN\n        primary_expression : ID\n        primary_expression : constant\n        primary_expression : STRING_LITERAL\n        primary_expression : LPAREN expression RPAREN\n        constant : INT_CONST\n        constant : CHAR_CONST\n        expression_opt : expression\n| empty\nexpression  : assignment_expression\n| expression COMMA assignment_expression\nargument_expression_opt : argument_expression\n| empty\nargument_expression : assignment_expression\n| argument_expression COMMA assignment_expression\nassignment_expression : binary_expression\n| unary_expression EQUALS assignment_expression\nunary_operator   : PLUS\n| MINUS\n| NOT\nparameter_list_opt : parameter_list\n| empty\nparameter_list   : parameter_declaration\n| parameter_list COMMA parameter_declaration\nparameter_declaration  : type_specifier declarator\n        declaration_star : declaration_star declaration\n| empty\ndeclaration   : type_specifier init_declarator_list_opt SEMIinit_declarator_list_opt : init_declarator_list\n| empty\ninit_declarator_list : init_declarator\n| init_declarator_list COMMA init_declarator\ninit_declarator : declarator\n| declarator EQUALS initializer\ninitializer : assignment_expression\n| LBRACE initializer_list_opt      RBRACE\n| LBRACE initializer_list    COMMA RBRACE\ninitializer_list_opt : initializer_list\n| empty\ninitializer_list : initializer\n| initializer_list COMMA initializer\ncompound_statement : LBRACE declaration_star statement_star RBRACEstatement_star : statement_star statement\n| empty\nstatement : expression_statementstatement : compound_statementstatement : selection_statementstatement : iteration_statementstatement : jump_statementstatement : assert_statementstatement : print_statementstatement : read_statementexpression_statement : expression_opt SEMIselection_statement : IF LPAREN expression RPAREN statement\n| IF LPAREN expression RPAREN statement ELSE statement\njump_statement  : BREAK SEMI\n        jump_statement  : RETURN expression_opt SEMI\n        iteration_statement : WHILE LPAREN expression RPAREN statement\n| FOR LPAREN expression_opt             SEMI expression_opt SEMI expression_opt RPAREN statement\n| FOR LPAREN declaration expression_opt SEMI expression_opt RPAREN statement\nassert_statement : ASSERT expression SEMI\n        print_statement : PRINT LPAREN expression_opt RPAREN SEMIread_statement : READ LPAREN argument_expression RPAREN SEMIempty :'
    
_lr_action_items = {'VOID':([0,2,3,4,5,10,18,19,21,23,53,54,78,86,113,143,],[7,7,-2,-4,-5,-3,-62,-6,7,-98,7,-61,7,-60,-76,7,]),'CHAR':([0,2,3,4,5,10,18,19,21,23,53,54,78,86,113,143,],[8,8,-2,-4,-5,-3,-62,-6,8,-98,8,-61,8,-60,-76,8,]),'INT':([0,2,3,4,5,10,18,19,21,23,53,54,78,86,113,143,],[9,9,-2,-4,-5,-3,-62,-6,9,-98,9,-61,9,-60,-76,9,]),'$end':([1,2,3,4,5,10,18,19,113,],[0,-1,-2,-4,-5,-3,-62,-6,-76,]),'ID':([6,7,8,9,16,18,20,22,23,24,31,32,34,36,37,47,50,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,84,85,86,87,88,108,111,113,114,115,116,117,118,119,120,121,122,129,130,136,140,141,142,143,144,147,148,153,154,155,158,159,160,164,165,167,168,169,170,171,173,175,176,177,178,],[15,-7,-8,-9,15,-62,38,38,-98,15,-52,-53,38,38,-54,15,38,-98,-61,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-60,-78,15,38,38,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,38,38,38,-87,38,38,38,-90,38,38,38,-91,-95,38,38,38,-88,-92,38,-96,-97,38,38,-89,38,38,-94,-93,]),'LPAREN':([6,7,8,9,12,15,16,18,20,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,47,50,53,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,77,79,84,85,86,87,88,107,108,111,113,114,115,116,117,118,119,120,121,122,124,126,127,129,130,131,132,134,135,136,140,141,142,143,144,147,148,153,154,155,158,159,160,164,165,167,168,169,170,171,173,175,176,177,178,],[16,-7,-8,-9,21,-10,16,-62,36,36,-98,16,21,-52,-53,73,36,-33,36,-54,-36,-37,-38,-40,-41,16,36,-98,-61,21,-11,-12,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-13,21,36,36,-60,-78,16,-39,36,36,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,141,142,143,36,36,147,148,-34,-35,36,-87,36,36,36,-90,36,36,36,-91,-95,36,36,36,-88,-92,36,-96,-97,36,36,-89,36,36,-94,-93,]),'SEMI':([6,7,8,9,11,12,13,14,15,17,18,23,30,33,35,38,39,40,41,42,48,49,51,52,53,54,55,56,57,58,74,76,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,107,110,112,113,114,115,116,117,118,119,120,121,122,123,125,128,129,133,134,135,137,138,140,143,144,145,146,152,153,154,155,158,159,160,161,162,163,164,165,166,168,169,170,173,175,176,177,178,],[-98,-7,-8,-9,18,-67,-63,-64,-10,-65,-62,-98,-17,-31,-33,-36,-37,-38,-40,-41,-68,-69,-50,-17,-98,-61,-66,-67,-11,-12,-32,-44,-13,-98,-60,-78,-98,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-39,-70,-51,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,140,-42,144,-98,-43,-34,-35,-45,-71,-87,-98,-90,154,155,160,-98,-91,-95,-98,-98,-98,167,168,169,-88,-92,171,-96,-97,-98,-89,-98,-98,-94,-93,]),'LBRACKET':([12,15,25,33,35,38,39,40,41,42,56,57,58,77,79,107,134,135,],[20,-10,20,72,-33,-36,-37,-38,-40,-41,20,-11,-12,-13,20,-39,-34,-35,]),'COMMA':([12,13,15,17,30,33,35,38,39,40,41,42,44,46,48,49,51,52,55,56,57,58,74,75,76,77,79,81,83,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,106,107,109,110,112,125,134,135,137,138,139,146,149,150,151,157,],[-67,24,-10,-65,-17,-31,-33,-36,-37,-38,-40,-41,78,-57,-68,-69,-50,-17,-66,-67,-11,-12,-32,108,-44,-13,-59,111,-74,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,108,136,-48,-39,-58,-70,-51,108,-34,-35,-45,-71,-75,108,-49,108,108,136,]),'EQUALS':([12,15,33,35,38,39,40,41,42,52,56,57,58,74,77,107,134,135,],[22,-10,-31,-33,-36,-37,-38,-40,-41,84,22,-11,-12,-32,-13,-39,-34,-35,]),'LBRACE':([12,15,18,22,23,50,53,54,57,58,77,85,86,87,111,113,114,115,116,117,118,119,120,121,122,140,144,154,155,158,159,164,165,168,169,170,173,175,176,177,178,],[23,-10,-62,50,-98,50,-98,-61,-11,-12,-13,23,-60,-78,50,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,-87,-90,-91,-95,23,23,-88,-92,-96,-97,23,-89,23,23,-94,-93,]),'RPAREN':([15,21,25,30,33,35,38,39,40,41,42,43,44,45,46,51,52,57,58,73,74,75,76,77,79,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,105,106,107,109,112,125,133,134,135,137,147,149,150,151,156,157,167,171,172,174,],[-10,-98,57,-17,-31,-33,-36,-37,-38,-40,-41,77,-55,-56,-57,-50,-17,-11,-12,-98,-32,107,-44,-13,-59,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,135,-46,-47,-48,-39,-58,-51,-42,-43,-34,-35,-45,-98,-49,158,159,162,163,-98,-98,175,176,]),'RBRACE':([18,23,30,33,35,38,39,40,41,42,49,50,51,52,53,54,74,80,81,82,83,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,107,110,111,112,113,114,115,116,117,118,119,120,121,122,134,135,138,139,140,144,154,155,164,165,168,169,173,177,178,],[-62,-98,-17,-31,-33,-36,-37,-38,-40,-41,-69,-98,-50,-17,-98,-61,-32,110,-72,-73,-74,113,-60,-78,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-39,-70,138,-51,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,-34,-35,-71,-75,-87,-90,-91,-95,-88,-92,-96,-97,-89,-94,-93,]),'IF':([18,23,53,54,85,86,87,113,114,115,116,117,118,119,120,121,122,140,144,154,155,158,159,164,165,168,169,170,173,175,176,177,178,],[-62,-98,-98,-61,124,-60,-78,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,-87,-90,-91,-95,124,124,-88,-92,-96,-97,124,-89,124,124,-94,-93,]),'WHILE':([18,23,53,54,85,86,87,113,114,115,116,117,118,119,120,121,122,140,144,154,155,158,159,164,165,168,169,170,173,175,176,177,178,],[-62,-98,-98,-61,126,-60,-78,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,-87,-90,-91,-95,126,126,-88,-92,-96,-97,126,-89,126,126,-94,-93,]),'FOR':([18,23,53,54,85,86,87,113,114,115,116,117,118,119,120,121,122,140,144,154,155,158,159,164,165,168,169,170,173,175,176,177,178,],[-62,-98,-98,-61,127,-60,-78,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,-87,-90,-91,-95,127,127,-88,-92,-96,-97,127,-89,127,127,-94,-93,]),'BREAK':([18,23,53,54,85,86,87,113,114,115,116,117,118,119,120,121,122,140,144,154,155,158,159,164,165,168,169,170,173,175,176,177,178,],[-62,-98,-98,-61,128,-60,-78,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,-87,-90,-91,-95,128,128,-88,-92,-96,-97,128,-89,128,128,-94,-93,]),'RETURN':([18,23,53,54,85,86,87,113,114,115,116,117,118,119,120,121,122,140,144,154,155,158,159,164,165,168,169,170,173,175,176,177,178,],[-62,-98,-98,-61,129,-60,-78,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,-87,-90,-91,-95,129,129,-88,-92,-96,-97,129,-89,129,129,-94,-93,]),'ASSERT':([18,23,53,54,85,86,87,113,114,115,116,117,118,119,120,121,122,140,144,154,155,158,159,164,165,168,169,170,173,175,176,177,178,],[-62,-98,-98,-61,130,-60,-78,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,-87,-90,-91,-95,130,130,-88,-92,-96,-97,130,-89,130,130,-94,-93,]),'PRINT':([18,23,53,54,85,86,87,113,114,115,116,117,118,119,120,121,122,140,144,154,155,158,159,164,165,168,169,170,173,175,176,177,178,],[-62,-98,-98,-61,131,-60,-78,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,-87,-90,-91,-95,131,131,-88,-92,-96,-97,131,-89,131,131,-94,-93,]),'READ':([18,23,53,54,85,86,87,113,114,115,116,117,118,119,120,121,122,140,144,154,155,158,159,164,165,168,169,170,173,175,176,177,178,],[-62,-98,-98,-61,132,-60,-78,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,-87,-90,-91,-95,132,132,-88,-92,-96,-97,132,-89,132,132,-94,-93,]),'PLUS':([18,20,22,23,29,30,31,32,33,34,35,36,37,38,39,40,41,42,50,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,107,108,111,113,114,115,116,117,118,119,120,121,122,129,130,134,135,136,140,141,142,143,144,147,148,153,154,155,158,159,160,164,165,167,168,169,170,171,173,175,176,177,178,],[-62,31,31,-98,62,-17,-52,-53,-31,31,-33,31,-54,-36,-37,-38,-40,-41,31,62,-17,-98,-61,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-32,31,31,-60,-78,-18,-19,-20,-21,-22,62,62,62,62,62,62,62,62,-39,31,31,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,31,31,-34,-35,31,-87,31,31,31,-90,31,31,31,-91,-95,31,31,31,-88,-92,31,-96,-97,31,31,-89,31,31,-94,-93,]),'MINUS':([18,20,22,23,29,30,31,32,33,34,35,36,37,38,39,40,41,42,50,51,52,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,84,85,86,87,89,90,91,92,93,94,95,96,97,98,99,100,101,107,108,111,113,114,115,116,117,118,119,120,121,122,129,130,134,135,136,140,141,142,143,144,147,148,153,154,155,158,159,160,164,165,167,168,169,170,171,173,175,176,177,178,],[-62,32,32,-98,63,-17,-52,-53,-31,32,-33,32,-54,-36,-37,-38,-40,-41,32,63,-17,-98,-61,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-32,32,32,-60,-78,-18,-19,-20,-21,-22,63,63,63,63,63,63,63,63,-39,32,32,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,32,32,-34,-35,32,-87,32,32,32,-90,32,32,32,-91,-95,32,32,32,-88,-92,32,-96,-97,32,32,-89,32,32,-94,-93,]),'NOT':([18,20,22,23,31,32,34,36,37,50,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,84,85,86,87,108,111,113,114,115,116,117,118,119,120,121,122,129,130,136,140,141,142,143,144,147,148,153,154,155,158,159,160,164,165,167,168,169,170,171,173,175,176,177,178,],[-62,37,37,-98,-52,-53,37,37,-54,37,-98,-61,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-60,-78,37,37,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,37,37,37,-87,37,37,37,-90,37,37,37,-91,-95,37,37,37,-88,-92,37,-96,-97,37,37,-89,37,37,-94,-93,]),'STRING_LITERAL':([18,20,22,23,31,32,34,36,37,50,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,84,85,86,87,108,111,113,114,115,116,117,118,119,120,121,122,129,130,136,140,141,142,143,144,147,148,153,154,155,158,159,160,164,165,167,168,169,170,171,173,175,176,177,178,],[-62,40,40,-98,-52,-53,40,40,-54,40,-98,-61,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-60,-78,40,40,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,40,40,40,-87,40,40,40,-90,40,40,40,-91,-95,40,40,40,-88,-92,40,-96,-97,40,40,-89,40,40,-94,-93,]),'INT_CONST':([18,20,22,23,31,32,34,36,37,50,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,84,85,86,87,108,111,113,114,115,116,117,118,119,120,121,122,129,130,136,140,141,142,143,144,147,148,153,154,155,158,159,160,164,165,167,168,169,170,171,173,175,176,177,178,],[-62,41,41,-98,-52,-53,41,41,-54,41,-98,-61,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-60,-78,41,41,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,41,41,41,-87,41,41,41,-90,41,41,41,-91,-95,41,41,41,-88,-92,41,-96,-97,41,41,-89,41,41,-94,-93,]),'CHAR_CONST':([18,20,22,23,31,32,34,36,37,50,53,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,84,85,86,87,108,111,113,114,115,116,117,118,119,120,121,122,129,130,136,140,141,142,143,144,147,148,153,154,155,158,159,160,164,165,167,168,169,170,171,173,175,176,177,178,],[-62,42,42,-98,-52,-53,42,42,-54,42,-98,-61,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-60,-78,42,42,-76,-77,-79,-80,-81,-82,-83,-84,-85,-86,42,42,42,-87,42,42,42,-90,42,42,42,-91,-95,42,42,42,-88,-92,42,-96,-97,42,42,-89,42,42,-94,-93,]),'RBRACKET':([20,26,27,28,29,30,33,35,38,39,40,41,42,51,52,74,76,89,90,91,92,93,94,95,96,97,98,99,100,101,102,107,112,134,135,137,],[-98,58,-14,-15,-16,-17,-31,-33,-36,-37,-38,-40,-41,-50,-17,-32,-44,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,134,-39,-51,-34,-35,-45,]),'TIMES':([29,30,33,35,38,39,40,41,42,51,52,74,89,90,91,92,93,94,95,96,97,98,99,100,101,107,134,135,],[59,-17,-31,-33,-36,-37,-38,-40,-41,59,-17,-32,-18,-19,-20,59,59,59,59,59,59,59,59,59,59,-39,-34,-35,]),'DIVIDE':([29,30,33,35,38,39,40,41,42,51,52,74,89,90,91,92,93,94,95,96,97,98,99,100,101,107,134,135,],[60,-17,-31,-33,-36,-37,-38,-40,-41,60,-17,-32,-18,-19,-20,60,60,60,60,60,60,60,60,60,60,-39,-34,-35,]),'MOD':([29,30,33,35,38,39,40,41,42,51,52,74,89,90,91,92,93,94,95,96,97,98,99,100,101,107,134,135,],[61,-17,-31,-33,-36,-37,-38,-40,-41,61,-17,-32,-18,-19,-20,61,61,61,61,61,61,61,61,61,61,-39,-34,-35,]),'LT':([29,30,33,35,38,39,40,41,42,51,52,74,89,90,91,92,93,94,95,96,97,98,99,100,101,107,134,135,],[64,-17,-31,-33,-36,-37,-38,-40,-41,64,-17,-32,-18,-19,-20,-21,-22,-23,-24,-25,-26,64,64,64,64,-39,-34,-35,]),'LE':([29,30,33,35,38,39,40,41,42,51,52,74,89,90,91,92,93,94,95,96,97,98,99,100,101,107,134,135,],[65,-17,-31,-33,-36,-37,-38,-40,-41,65,-17,-32,-18,-19,-20,-21,-22,-23,-24,-25,-26,65,65,65,65,-39,-34,-35,]),'GT':([29,30,33,35,38,39,40,41,42,51,52,74,89,90,91,92,93,94,95,96,97,98,99,100,101,107,134,135,],[66,-17,-31,-33,-36,-37,-38,-40,-41,66,-17,-32,-18,-19,-20,-21,-22,-23,-24,-25,-26,66,66,66,66,-39,-34,-35,]),'GE':([29,30,33,35,38,39,40,41,42,51,52,74,89,90,91,92,93,94,95,96,97,98,99,100,101,107,134,135,],[67,-17,-31,-33,-36,-37,-38,-40,-41,67,-17,-32,-18,-19,-20,-21,-22,-23,-24,-25,-26,67,67,67,67,-39,-34,-35,]),'EQ':([29,30,33,35,38,39,40,41,42,51,52,74,89,90,91,92,93,94,95,96,97,98,99,100,101,107,134,135,],[68,-17,-31,-33,-36,-37,-38,-40,-41,68,-17,-32,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,68,68,-39,-34,-35,]),'NE':([29,30,33,35,38,39,40,41,42,51,52,74,89,90,91,92,93,94,95,96,97,98,99,100,101,107,134,135,],[69,-17,-31,-33,-36,-37,-38,-40,-41,69,-17,-32,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,69,69,-39,-34,-35,]),'AND':([29,30,33,35,38,39,40,41,42,51,52,74,89,90,91,92,93,94,95,96,97,98,99,100,101,107,134,135,],[70,-17,-31,-33,-36,-37,-38,-40,-41,70,-17,-32,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,70,-39,-34,-35,]),'OR':([29,30,33,35,38,39,40,41,42,51,52,74,89,90,91,92,93,94,95,96,97,98,99,100,101,107,134,135,],[71,-17,-31,-33,-36,-37,-38,-40,-41,71,-17,-32,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-39,-34,-35,]),'ELSE':([113,115,116,117,118,119,120,121,122,140,144,154,155,164,165,168,169,173,177,178,],[-76,-79,-80,-81,-82,-83,-84,-85,-86,-87,-90,-91,-95,170,-92,-96,-97,-89,-94,-93,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'global_declaration_list':([0,],[2,]),'global_declaration':([0,2,],[3,10,]),'declaration':([0,2,53,143,],[4,4,86,153,]),'function_definition':([0,2,],[5,5,]),'type_specifier':([0,2,21,53,78,143,],[6,6,47,88,47,88,]),'init_declarator_list_opt':([6,88,],[11,11,]),'declarator':([6,16,24,47,88,],[12,25,56,79,56,]),'init_declarator_list':([6,88,],[13,13,]),'empty':([6,20,21,23,50,53,73,85,88,129,143,147,153,158,159,160,167,170,171,175,176,],[14,28,45,54,82,87,105,133,14,133,133,133,133,133,133,133,133,133,133,133,133,]),'init_declarator':([6,24,88,],[17,55,17,]),'compound_statement':([12,85,158,159,170,175,176,],[19,116,116,116,116,116,116,]),'constant_expression_opt':([20,],[26,]),'constant_expression':([20,],[27,]),'binary_expression':([20,22,36,50,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,84,85,108,111,129,130,136,141,142,143,147,148,153,158,159,160,167,170,171,175,176,],[29,51,51,51,89,90,91,92,93,94,95,96,97,98,99,100,101,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'unary_expression':([20,22,34,36,50,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,84,85,108,111,129,130,136,141,142,143,147,148,153,158,159,160,167,170,171,175,176,],[30,52,74,52,52,30,30,30,30,30,30,30,30,30,30,30,30,30,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'postfix_expression':([20,22,34,36,50,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,84,85,108,111,129,130,136,141,142,143,147,148,153,158,159,160,167,170,171,175,176,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'unary_operator':([20,22,34,36,50,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,84,85,108,111,129,130,136,141,142,143,147,148,153,158,159,160,167,170,171,175,176,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'primary_expression':([20,22,34,36,50,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,84,85,108,111,129,130,136,141,142,143,147,148,153,158,159,160,167,170,171,175,176,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'constant':([20,22,34,36,50,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,84,85,108,111,129,130,136,141,142,143,147,148,153,158,159,160,167,170,171,175,176,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'parameter_list_opt':([21,],[43,]),'parameter_list':([21,],[44,]),'parameter_declaration':([21,78,],[46,109,]),'initializer':([22,50,111,],[48,83,139,]),'assignment_expression':([22,36,50,72,73,84,85,108,111,129,130,136,141,142,143,147,148,153,158,159,160,167,170,171,175,176,],[49,76,49,76,106,112,76,137,49,76,76,149,76,76,76,76,106,76,76,76,76,76,76,76,76,76,]),'declaration_star':([23,],[53,]),'expression':([36,72,85,129,130,141,142,143,147,153,158,159,160,167,170,171,175,176,],[75,102,125,125,146,150,151,125,125,125,125,125,125,125,125,125,125,125,]),'initializer_list_opt':([50,],[80,]),'initializer_list':([50,],[81,]),'statement_star':([53,],[85,]),'argument_expression_opt':([73,],[103,]),'argument_expression':([73,148,],[104,157,]),'statement':([85,158,159,170,175,176,],[114,164,165,173,177,178,]),'expression_statement':([85,158,159,170,175,176,],[115,115,115,115,115,115,]),'selection_statement':([85,158,159,170,175,176,],[117,117,117,117,117,117,]),'iteration_statement':([85,158,159,170,175,176,],[118,118,118,118,118,118,]),'jump_statement':([85,158,159,170,175,176,],[119,119,119,119,119,119,]),'assert_statement':([85,158,159,170,175,176,],[120,120,120,120,120,120,]),'print_statement':([85,158,159,170,175,176,],[121,121,121,121,121,121,]),'read_statement':([85,158,159,170,175,176,],[122,122,122,122,122,122,]),'expression_opt':([85,129,143,147,153,158,159,160,167,170,171,175,176,],[123,145,152,156,161,123,123,166,172,123,174,123,123,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> global_declaration_list','program',1,'p_program','uc_parser.py',110),
  ('global_declaration_list -> global_declaration','global_declaration_list',1,'p_global_declaration_list','uc_parser.py',114),
  ('global_declaration_list -> global_declaration_list global_declaration','global_declaration_list',2,'p_global_declaration_list','uc_parser.py',115),
  ('global_declaration -> declaration','global_declaration',1,'p_global_declaration_1','uc_parser.py',120),
  ('global_declaration -> function_definition','global_declaration',1,'p_global_declaration_2','uc_parser.py',124),
  ('function_definition -> type_specifier declarator compound_statement','function_definition',3,'p_function_definition','uc_parser.py',128),
  ('type_specifier -> VOID','type_specifier',1,'p_type_specifier','uc_parser.py',134),
  ('type_specifier -> CHAR','type_specifier',1,'p_type_specifier','uc_parser.py',135),
  ('type_specifier -> INT','type_specifier',1,'p_type_specifier','uc_parser.py',136),
  ('declarator -> ID','declarator',1,'p_declarator_id','uc_parser.py',143),
  ('declarator -> LPAREN declarator RPAREN','declarator',3,'p_declarator_paren','uc_parser.py',151),
  ('declarator -> declarator LBRACKET constant_expression_opt RBRACKET','declarator',4,'p_declarator_constant_expression','uc_parser.py',155),
  ('declarator -> declarator LPAREN parameter_list_opt RPAREN','declarator',4,'p_declarator_parameter_list','uc_parser.py',160),
  ('constant_expression_opt -> constant_expression','constant_expression_opt',1,'p_constant_expression_opt','uc_parser.py',165),
  ('constant_expression_opt -> empty','constant_expression_opt',1,'p_constant_expression_opt','uc_parser.py',166),
  ('constant_expression -> binary_expression','constant_expression',1,'p_constant_expression','uc_parser.py',171),
  ('binary_expression -> unary_expression','binary_expression',1,'p_binary_expression','uc_parser.py',175),
  ('binary_expression -> binary_expression TIMES binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',176),
  ('binary_expression -> binary_expression DIVIDE binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',177),
  ('binary_expression -> binary_expression MOD binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',178),
  ('binary_expression -> binary_expression PLUS binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',179),
  ('binary_expression -> binary_expression MINUS binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',180),
  ('binary_expression -> binary_expression LT binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',181),
  ('binary_expression -> binary_expression LE binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',182),
  ('binary_expression -> binary_expression GT binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',183),
  ('binary_expression -> binary_expression GE binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',184),
  ('binary_expression -> binary_expression EQ binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',185),
  ('binary_expression -> binary_expression NE binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',186),
  ('binary_expression -> binary_expression AND binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',187),
  ('binary_expression -> binary_expression OR binary_expression','binary_expression',3,'p_binary_expression','uc_parser.py',188),
  ('unary_expression -> postfix_expression','unary_expression',1,'p_unary_expression','uc_parser.py',196),
  ('unary_expression -> unary_operator unary_expression','unary_expression',2,'p_unary_expression','uc_parser.py',197),
  ('postfix_expression -> primary_expression','postfix_expression',1,'p_postfix_expression_primary','uc_parser.py',205),
  ('postfix_expression -> postfix_expression LBRACKET expression RBRACKET','postfix_expression',4,'p_postfix_expression_array_ref','uc_parser.py',210),
  ('postfix_expression -> postfix_expression LPAREN argument_expression_opt RPAREN','postfix_expression',4,'p_postfix_expression_func_call','uc_parser.py',215),
  ('primary_expression -> ID','primary_expression',1,'p_primary_expression_id','uc_parser.py',220),
  ('primary_expression -> constant','primary_expression',1,'p_primary_expression_constant','uc_parser.py',225),
  ('primary_expression -> STRING_LITERAL','primary_expression',1,'p_primary_expression_string_literal','uc_parser.py',230),
  ('primary_expression -> LPAREN expression RPAREN','primary_expression',3,'p_primary_expression_lparen_expression_rparen','uc_parser.py',236),
  ('constant -> INT_CONST','constant',1,'p_constant_int','uc_parser.py',242),
  ('constant -> CHAR_CONST','constant',1,'p_constant_char','uc_parser.py',247),
  ('expression_opt -> expression','expression_opt',1,'p_expression_opt','uc_parser.py',253),
  ('expression_opt -> empty','expression_opt',1,'p_expression_opt','uc_parser.py',254),
  ('expression -> assignment_expression','expression',1,'p_expression','uc_parser.py',259),
  ('expression -> expression COMMA assignment_expression','expression',3,'p_expression','uc_parser.py',260),
  ('argument_expression_opt -> argument_expression','argument_expression_opt',1,'p_argument_expression_opt','uc_parser.py',273),
  ('argument_expression_opt -> empty','argument_expression_opt',1,'p_argument_expression_opt','uc_parser.py',274),
  ('argument_expression -> assignment_expression','argument_expression',1,'p_argument_expression','uc_parser.py',279),
  ('argument_expression -> argument_expression COMMA assignment_expression','argument_expression',3,'p_argument_expression','uc_parser.py',280),
  ('assignment_expression -> binary_expression','assignment_expression',1,'p_assignment_expression','uc_parser.py',293),
  ('assignment_expression -> unary_expression EQUALS assignment_expression','assignment_expression',3,'p_assignment_expression','uc_parser.py',294),
  ('unary_operator -> PLUS','unary_operator',1,'p_unary_operator','uc_parser.py',302),
  ('unary_operator -> MINUS','unary_operator',1,'p_unary_operator','uc_parser.py',303),
  ('unary_operator -> NOT','unary_operator',1,'p_unary_operator','uc_parser.py',304),
  ('parameter_list_opt -> parameter_list','parameter_list_opt',1,'p_parameter_list_opt','uc_parser.py',309),
  ('parameter_list_opt -> empty','parameter_list_opt',1,'p_parameter_list_opt','uc_parser.py',310),
  ('parameter_list -> parameter_declaration','parameter_list',1,'p_parameter_list','uc_parser.py',315),
  ('parameter_list -> parameter_list COMMA parameter_declaration','parameter_list',3,'p_parameter_list','uc_parser.py',316),
  ('parameter_declaration -> type_specifier declarator','parameter_declaration',2,'p_parameter_declaration','uc_parser.py',325),
  ('declaration_star -> declaration_star declaration','declaration_star',2,'p_declaration_star','uc_parser.py',332),
  ('declaration_star -> empty','declaration_star',1,'p_declaration_star','uc_parser.py',333),
  ('declaration -> type_specifier init_declarator_list_opt SEMI','declaration',3,'p_declaration','uc_parser.py',342),
  ('init_declarator_list_opt -> init_declarator_list','init_declarator_list_opt',1,'p_init_declarator_list_opt','uc_parser.py',349),
  ('init_declarator_list_opt -> empty','init_declarator_list_opt',1,'p_init_declarator_list_opt','uc_parser.py',350),
  ('init_declarator_list -> init_declarator','init_declarator_list',1,'p_init_declarator_list','uc_parser.py',355),
  ('init_declarator_list -> init_declarator_list COMMA init_declarator','init_declarator_list',3,'p_init_declarator_list','uc_parser.py',356),
  ('init_declarator -> declarator','init_declarator',1,'p_init_declarator','uc_parser.py',365),
  ('init_declarator -> declarator EQUALS initializer','init_declarator',3,'p_init_declarator','uc_parser.py',366),
  ('initializer -> assignment_expression','initializer',1,'p_initializer','uc_parser.py',376),
  ('initializer -> LBRACE initializer_list_opt RBRACE','initializer',3,'p_initializer','uc_parser.py',377),
  ('initializer -> LBRACE initializer_list COMMA RBRACE','initializer',4,'p_initializer','uc_parser.py',378),
  ('initializer_list_opt -> initializer_list','initializer_list_opt',1,'p_initializer_list_opt','uc_parser.py',386),
  ('initializer_list_opt -> empty','initializer_list_opt',1,'p_initializer_list_opt','uc_parser.py',387),
  ('initializer_list -> initializer','initializer_list',1,'p_initializer_list','uc_parser.py',392),
  ('initializer_list -> initializer_list COMMA initializer','initializer_list',3,'p_initializer_list','uc_parser.py',393),
  ('compound_statement -> LBRACE declaration_star statement_star RBRACE','compound_statement',4,'p_compound_statement','uc_parser.py',403),
  ('statement_star -> statement_star statement','statement_star',2,'p_statement_star','uc_parser.py',407),
  ('statement_star -> empty','statement_star',1,'p_statement_star','uc_parser.py',408),
  ('statement -> expression_statement','statement',1,'p_statement_expression_statement','uc_parser.py',417),
  ('statement -> compound_statement','statement',1,'p_statement_compound_statement','uc_parser.py',421),
  ('statement -> selection_statement','statement',1,'p_statement_selection_statement','uc_parser.py',425),
  ('statement -> iteration_statement','statement',1,'p_statement_iteration_statement','uc_parser.py',429),
  ('statement -> jump_statement','statement',1,'p_statement_jump_statement','uc_parser.py',433),
  ('statement -> assert_statement','statement',1,'p_statement_assert_statement','uc_parser.py',437),
  ('statement -> print_statement','statement',1,'p_statement_print_statement','uc_parser.py',441),
  ('statement -> read_statement','statement',1,'p_statement_read_statement','uc_parser.py',445),
  ('expression_statement -> expression_opt SEMI','expression_statement',2,'p_expression_statement','uc_parser.py',449),
  ('selection_statement -> IF LPAREN expression RPAREN statement','selection_statement',5,'p_selection_statement','uc_parser.py',453),
  ('selection_statement -> IF LPAREN expression RPAREN statement ELSE statement','selection_statement',7,'p_selection_statement','uc_parser.py',454),
  ('jump_statement -> BREAK SEMI','jump_statement',2,'p_jump_statement_break','uc_parser.py',463),
  ('jump_statement -> RETURN expression_opt SEMI','jump_statement',3,'p_jump_statement_return','uc_parser.py',468),
  ('iteration_statement -> WHILE LPAREN expression RPAREN statement','iteration_statement',5,'p_iteration_statement','uc_parser.py',473),
  ('iteration_statement -> FOR LPAREN expression_opt SEMI expression_opt SEMI expression_opt RPAREN statement','iteration_statement',9,'p_iteration_statement','uc_parser.py',474),
  ('iteration_statement -> FOR LPAREN declaration expression_opt SEMI expression_opt RPAREN statement','iteration_statement',8,'p_iteration_statement','uc_parser.py',475),
  ('assert_statement -> ASSERT expression SEMI','assert_statement',3,'p_assert_statement','uc_parser.py',486),
  ('print_statement -> PRINT LPAREN expression_opt RPAREN SEMI','print_statement',5,'p_print_statement','uc_parser.py',491),
  ('read_statement -> READ LPAREN argument_expression RPAREN SEMI','read_statement',5,'p_read_statement','uc_parser.py',495),
  ('empty -> <empty>','empty',0,'p_empty','uc_parser.py',499),
]
