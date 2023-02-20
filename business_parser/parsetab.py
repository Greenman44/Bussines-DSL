
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTDIVACTION ADD AMOUNT AND ASSIGN BILL CATALOG CBR CBRACE COMMA COST CPAREN DATE DATE DATE DEL DESCRIP DISMISS DIV DPOINT ELSE END EQUAL FOREACH FROM GEQ GET GREATER ID IF IN INVESTS LEQ LESS LOAD METRICS METRICS METRICS METRICS METRICS MINUS MULT NAME NOT NUMBER OBR OBRACE OPAREN OR PLUS POINT PRICE SALARY SALE SAVE STAFF TYPE TYPE TYPE TYPE TYPE WHILEProgram : ListInstListInst : Instruction END ListInst\n                | Instruction ENDInstruction : instance\n                   | SAVE ID\n                   | ID GET METRICS DATE\n                   | loop_statements\n                   | IfStatement\n                   | IfStatement ELSE OBRACE ListInst CBRACE\n                   Instruction : ID ACTION SALE ID PRICE DPOINT NUMBER AMOUNT DPOINT NUMBERInstruction : ID ACTION SALE ID PRICE DPOINT ID AMOUNT DPOINT IDInstruction : ID ACTION SALE ID PRICE DPOINT operation AMOUNT DPOINT operationInstruction : ID ACTION INVESTS ID COST DPOINT NUMBER AMOUNT DPOINT NUMBERInstruction : ID ACTION INVESTS ID COST DPOINT ID AMOUNT DPOINT IDInstruction : ID ACTION INVESTS ID COST DPOINT operation AMOUNT DPOINT operationInstruction : ID ADD ID\n                   | ID ADD BILL OBRACE NUMBER COMMA DESCRIP CBRACEInstruction : ID ADD BILL OBRACE operation COMMA DESCRIP CBRACEInstruction : ID ADD BILL OBRACE ID COMMA DESCRIP CBRACE Instruction : ID ADD subTypeInstruction : ID DEL NAMEInstruction : ID DEL IDInstruction : ID DISMISS NAMEInstruction : ID DISMISS IDloop_statements : FOREACH ID IN ID OBRACE ListInst CBRACE\n                       | WHILE OPAREN condition CPAREN OBRACE ListInst CBRACEIfStatement : IF OPAREN condition CPAREN OBRACE ListInst CBRACEcondition : bool_expression\n                \n        bool_expression : NOT bool_expression\n                        | bool_expression AND bool_expression\n                        | bool_expression OR bool_expression\n                        | ID EQUAL ID\n                        | ID LEQ ID\n                        | ID GEQ ID\n                        | ID GREATER ID\n                        | ID LESS ID\n                        bool_expression : OPAREN bool_expression CPARENbool_expression : ID IN IDinstance : TYPE ID\n                | TYPE ID ASSIGN Assignable\n                | ID ASSIGN Assignable\n                 operation : operation PLUS operation\n                  | operation MINUS operation\n                  | operation DIV operation\n                  | operation MULT operation\n                  | IDoperation : NUMBER operation : OPAREN operation CPARENAssignable : subType\n                  | collection\n                  | GET NAME FROM ID\n                  | LOAD NAME\n                  | operation\n                  Assignable : GET STAFF FROM IDAssignable : GET CATALOG FROM IDAssignable : GET AMOUNT FROM IDAssignable : IDsubType : OBRACE bus CBRACE\n               | OBRACE emp CBRACE\n               | OBRACE prod CBRACE\n               collection : OBR collection_body CBRcollection_body : subType COMMA collection_body\n                       | subTypecollection_body : ID COMMA collection_body\n                       | IDbus : NAME COMMA collection COMMA collectionbus : NAME COMMA ID COMMA IDemp : NAME COMMA SALARY DPOINT NUMBERemp : NAME COMMA SALARY DPOINT IDemp : NAME COMMA SALARY DPOINT operationprod : NAME COMMA AMOUNT DPOINT NUMBER\n            | NAME prod : NAME COMMA AMOUNT DPOINT IDprod : NAME COMMA AMOUNT DPOINT operation'
    
_lr_action_items = {'SAVE':([0,13,48,116,118,127,],[5,5,5,5,5,5,]),'ID':([0,5,9,10,13,17,18,19,20,24,25,28,29,45,47,48,49,50,51,54,60,70,71,72,73,84,85,87,88,89,90,91,92,102,103,104,105,106,112,113,116,118,127,128,129,156,157,158,179,181,182,184,],[6,14,22,23,6,30,34,36,38,55,55,58,59,76,78,6,38,81,55,55,96,78,78,78,78,55,55,121,122,123,124,125,126,134,137,138,139,140,76,76,6,6,6,146,149,172,174,177,185,78,188,78,]),'TYPE':([0,13,48,116,118,127,],[9,9,9,9,9,9,]),'FOREACH':([0,13,48,116,118,127,],[10,10,10,10,10,10,]),'WHILE':([0,13,48,116,118,127,],[11,11,11,11,11,11,]),'IF':([0,13,48,116,118,127,],[12,12,12,12,12,12,]),'$end':([1,2,13,26,],[0,-1,-3,-2,]),'END':([3,4,7,8,14,22,30,33,34,35,36,37,38,39,40,41,44,46,57,69,78,80,99,100,101,107,108,109,110,111,114,115,137,138,139,140,159,160,161,168,169,170,185,186,187,188,189,190,],[13,-4,-7,-8,-5,-39,-16,-20,-22,-21,-24,-23,-46,-41,-49,-50,-53,-47,-6,-52,-46,-40,-58,-59,-60,-42,-43,-44,-45,-61,-48,-9,-51,-54,-55,-56,-25,-26,-27,-19,-17,-18,-11,-10,-12,-14,-13,-15,]),'GET':([6,20,49,],[15,42,42,]),'ACTION':([6,],[16,]),'ADD':([6,],[17,]),'DEL':([6,],[18,]),'DISMISS':([6,],[19,]),'ASSIGN':([6,22,],[20,49,]),'ELSE':([8,161,],[21,-27,]),'OPAREN':([11,12,20,24,25,47,49,51,54,60,70,71,72,73,84,85,128,129,157,158,181,184,],[24,25,47,51,51,47,47,51,51,47,47,47,47,47,51,51,47,47,47,47,47,47,]),'CBRACE':([13,26,46,61,62,63,64,78,79,107,108,109,110,111,114,143,144,145,152,153,154,171,172,173,174,175,176,177,178,],[-3,-2,-47,99,100,101,-72,-46,115,-42,-43,-44,-45,-61,-48,159,160,161,168,169,170,-66,-67,-47,-46,-70,-47,-46,-74,]),'METRICS':([15,],[27,]),'SALE':([16,],[28,]),'INVESTS':([16,],[29,]),'BILL':([17,],[31,]),'OBRACE':([17,20,21,31,45,49,81,83,93,112,113,],[32,32,48,60,32,32,116,118,127,32,32,]),'NAME':([18,19,32,42,43,],[35,37,64,65,69,]),'LOAD':([20,49,],[43,43,]),'OBR':([20,49,102,155,],[45,45,45,45,]),'NUMBER':([20,47,49,60,70,71,72,73,128,129,157,158,180,181,183,184,],[46,46,46,97,46,46,46,46,147,150,173,176,186,46,189,46,]),'IN':([23,55,],[50,92,]),'NOT':([24,25,51,54,84,85,],[54,54,54,54,54,54,]),'DATE':([27,],[57,]),'PLUS':([38,44,46,77,78,96,97,98,107,108,109,110,114,146,147,148,149,150,151,173,174,175,176,177,178,187,190,],[-46,70,-47,70,-46,-46,-47,70,-42,-43,-44,-45,-48,-46,-47,70,-46,-47,70,-47,-46,70,-47,-46,70,70,70,]),'MINUS':([38,44,46,77,78,96,97,98,107,108,109,110,114,146,147,148,149,150,151,173,174,175,176,177,178,187,190,],[-46,71,-47,71,-46,-46,-47,71,-42,-43,-44,-45,-48,-46,-47,71,-46,-47,71,-47,-46,71,-47,-46,71,71,71,]),'DIV':([38,44,46,77,78,96,97,98,107,108,109,110,114,146,147,148,149,150,151,173,174,175,176,177,178,187,190,],[-46,72,-47,72,-46,-46,-47,72,72,72,-44,-45,-48,-46,-47,72,-46,-47,72,-47,-46,72,-47,-46,72,72,72,]),'MULT':([38,44,46,77,78,96,97,98,107,108,109,110,114,146,147,148,149,150,151,173,174,175,176,177,178,187,190,],[-46,73,-47,73,-46,-46,-47,73,73,73,-44,-45,-48,-46,-47,73,-46,-47,73,-47,-46,73,-47,-46,73,73,73,]),'STAFF':([42,],[66,]),'CATALOG':([42,],[67,]),'AMOUNT':([42,46,78,102,107,108,109,110,114,146,147,148,149,150,151,],[68,-47,-46,136,-42,-43,-44,-45,-48,162,163,164,165,166,167,]),'CPAREN':([46,52,53,56,77,78,82,86,107,108,109,110,114,117,119,120,121,122,123,124,125,126,],[-47,83,-28,93,114,-46,117,-29,-42,-43,-44,-45,-48,-37,-30,-31,-32,-33,-34,-35,-36,-38,]),'COMMA':([46,64,75,76,78,96,97,98,99,100,101,107,108,109,110,111,114,133,134,],[-47,102,112,113,-46,130,131,132,-58,-59,-60,-42,-43,-44,-45,-61,-48,155,156,]),'AND':([53,82,86,117,119,120,121,122,123,124,125,126,],[84,84,84,-37,84,84,-32,-33,-34,-35,-36,-38,]),'OR':([53,82,86,117,119,120,121,122,123,124,125,126,],[85,85,85,-37,85,85,-32,-33,-34,-35,-36,-38,]),'EQUAL':([55,],[87,]),'LEQ':([55,],[88,]),'GEQ':([55,],[89,]),'GREATER':([55,],[90,]),'LESS':([55,],[91,]),'PRICE':([58,],[94,]),'COST':([59,],[95,]),'FROM':([65,66,67,68,],[103,104,105,106,]),'CBR':([74,75,76,99,100,101,141,142,],[111,-63,-65,-58,-59,-60,-62,-64,]),'DPOINT':([94,95,135,136,162,163,164,165,166,167,],[128,129,157,158,179,180,181,182,183,184,]),'SALARY':([102,],[135,]),'DESCRIP':([130,131,132,],[152,153,154,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'ListInst':([0,13,48,116,118,127,],[2,26,79,143,144,145,]),'Instruction':([0,13,48,116,118,127,],[3,3,3,3,3,3,]),'instance':([0,13,48,116,118,127,],[4,4,4,4,4,4,]),'loop_statements':([0,13,48,116,118,127,],[7,7,7,7,7,7,]),'IfStatement':([0,13,48,116,118,127,],[8,8,8,8,8,8,]),'subType':([17,20,45,49,112,113,],[33,40,75,40,75,75,]),'Assignable':([20,49,],[39,80,]),'collection':([20,49,102,155,],[41,41,133,171,]),'operation':([20,47,49,60,70,71,72,73,128,129,157,158,181,184,],[44,77,44,98,107,108,109,110,148,151,175,178,187,190,]),'condition':([24,25,],[52,56,]),'bool_expression':([24,25,51,54,84,85,],[53,53,82,86,119,120,]),'bus':([32,],[61,]),'emp':([32,],[62,]),'prod':([32,],[63,]),'collection_body':([45,112,113,],[74,141,142,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> ListInst','Program',1,'p_program','parser_rules.py',13),
  ('ListInst -> Instruction END ListInst','ListInst',3,'p_list_instructions','parser_rules.py',18),
  ('ListInst -> Instruction END','ListInst',2,'p_list_instructions','parser_rules.py',19),
  ('Instruction -> instance','Instruction',1,'p_instruction','parser_rules.py',27),
  ('Instruction -> SAVE ID','Instruction',2,'p_instruction','parser_rules.py',28),
  ('Instruction -> ID GET METRICS DATE','Instruction',4,'p_instruction','parser_rules.py',29),
  ('Instruction -> loop_statements','Instruction',1,'p_instruction','parser_rules.py',30),
  ('Instruction -> IfStatement','Instruction',1,'p_instruction','parser_rules.py',31),
  ('Instruction -> IfStatement ELSE OBRACE ListInst CBRACE','Instruction',5,'p_instruction','parser_rules.py',32),
  ('Instruction -> ID ACTION SALE ID PRICE DPOINT NUMBER AMOUNT DPOINT NUMBER','Instruction',10,'p_instruction_sale','parser_rules.py',45),
  ('Instruction -> ID ACTION SALE ID PRICE DPOINT ID AMOUNT DPOINT ID','Instruction',10,'p_instruction_sale_ID','parser_rules.py',49),
  ('Instruction -> ID ACTION SALE ID PRICE DPOINT operation AMOUNT DPOINT operation','Instruction',10,'p_instruction_sale_operation','parser_rules.py',53),
  ('Instruction -> ID ACTION INVESTS ID COST DPOINT NUMBER AMOUNT DPOINT NUMBER','Instruction',10,'p_instruction_invests','parser_rules.py',57),
  ('Instruction -> ID ACTION INVESTS ID COST DPOINT ID AMOUNT DPOINT ID','Instruction',10,'p_instruction_invests_ID','parser_rules.py',61),
  ('Instruction -> ID ACTION INVESTS ID COST DPOINT operation AMOUNT DPOINT operation','Instruction',10,'p_instruction_invests_operation','parser_rules.py',65),
  ('Instruction -> ID ADD ID','Instruction',3,'p_instruction_add','parser_rules.py',69),
  ('Instruction -> ID ADD BILL OBRACE NUMBER COMMA DESCRIP CBRACE','Instruction',8,'p_instruction_add','parser_rules.py',70),
  ('Instruction -> ID ADD BILL OBRACE operation COMMA DESCRIP CBRACE','Instruction',8,'p_instruction_Bill_oper','parser_rules.py',77),
  ('Instruction -> ID ADD BILL OBRACE ID COMMA DESCRIP CBRACE','Instruction',8,'p_instruction_Bill_ID','parser_rules.py',81),
  ('Instruction -> ID ADD subType','Instruction',3,'p_instruction_add_ID','parser_rules.py',85),
  ('Instruction -> ID DEL NAME','Instruction',3,'p_instruction_del','parser_rules.py',90),
  ('Instruction -> ID DEL ID','Instruction',3,'p_instruction_del_ID','parser_rules.py',94),
  ('Instruction -> ID DISMISS NAME','Instruction',3,'p_instruction_dismiss','parser_rules.py',98),
  ('Instruction -> ID DISMISS ID','Instruction',3,'p_instruction_dismiss_ID','parser_rules.py',102),
  ('loop_statements -> FOREACH ID IN ID OBRACE ListInst CBRACE','loop_statements',7,'p_loops_statements','parser_rules.py',106),
  ('loop_statements -> WHILE OPAREN condition CPAREN OBRACE ListInst CBRACE','loop_statements',7,'p_loops_statements','parser_rules.py',107),
  ('IfStatement -> IF OPAREN condition CPAREN OBRACE ListInst CBRACE','IfStatement',7,'p_IfStatement','parser_rules.py',114),
  ('condition -> bool_expression','condition',1,'p_condition','parser_rules.py',118),
  ('bool_expression -> NOT bool_expression','bool_expression',2,'p_bool_expression','parser_rules.py',128),
  ('bool_expression -> bool_expression AND bool_expression','bool_expression',3,'p_bool_expression','parser_rules.py',129),
  ('bool_expression -> bool_expression OR bool_expression','bool_expression',3,'p_bool_expression','parser_rules.py',130),
  ('bool_expression -> ID EQUAL ID','bool_expression',3,'p_bool_expression','parser_rules.py',131),
  ('bool_expression -> ID LEQ ID','bool_expression',3,'p_bool_expression','parser_rules.py',132),
  ('bool_expression -> ID GEQ ID','bool_expression',3,'p_bool_expression','parser_rules.py',133),
  ('bool_expression -> ID GREATER ID','bool_expression',3,'p_bool_expression','parser_rules.py',134),
  ('bool_expression -> ID LESS ID','bool_expression',3,'p_bool_expression','parser_rules.py',135),
  ('bool_expression -> OPAREN bool_expression CPAREN','bool_expression',3,'p_bool_expression_Paren','parser_rules.py',144),
  ('bool_expression -> ID IN ID','bool_expression',3,'p_bool_expression_in','parser_rules.py',151),
  ('instance -> TYPE ID','instance',2,'p_instance','parser_rules.py',155),
  ('instance -> TYPE ID ASSIGN Assignable','instance',4,'p_instance','parser_rules.py',156),
  ('instance -> ID ASSIGN Assignable','instance',3,'p_instance','parser_rules.py',157),
  ('operation -> operation PLUS operation','operation',3,'p_oper','parser_rules.py',170),
  ('operation -> operation MINUS operation','operation',3,'p_oper','parser_rules.py',171),
  ('operation -> operation DIV operation','operation',3,'p_oper','parser_rules.py',172),
  ('operation -> operation MULT operation','operation',3,'p_oper','parser_rules.py',173),
  ('operation -> ID','operation',1,'p_oper','parser_rules.py',174),
  ('operation -> NUMBER','operation',1,'p_oper_Number','parser_rules.py',181),
  ('operation -> OPAREN operation CPAREN','operation',3,'p_oper_PAREN','parser_rules.py',185),
  ('Assignable -> subType','Assignable',1,'p_Assignable','parser_rules.py',190),
  ('Assignable -> collection','Assignable',1,'p_Assignable','parser_rules.py',191),
  ('Assignable -> GET NAME FROM ID','Assignable',4,'p_Assignable','parser_rules.py',192),
  ('Assignable -> LOAD NAME','Assignable',2,'p_Assignable','parser_rules.py',193),
  ('Assignable -> operation','Assignable',1,'p_Assignable','parser_rules.py',194),
  ('Assignable -> GET STAFF FROM ID','Assignable',4,'p_Assignable_Staff','parser_rules.py',205),
  ('Assignable -> GET CATALOG FROM ID','Assignable',4,'p_Assignable_Catalog','parser_rules.py',209),
  ('Assignable -> GET AMOUNT FROM ID','Assignable',4,'p_Assignable_Amount','parser_rules.py',213),
  ('Assignable -> ID','Assignable',1,'p_Assignable_ID','parser_rules.py',217),
  ('subType -> OBRACE bus CBRACE','subType',3,'p_subType','parser_rules.py',221),
  ('subType -> OBRACE emp CBRACE','subType',3,'p_subType','parser_rules.py',222),
  ('subType -> OBRACE prod CBRACE','subType',3,'p_subType','parser_rules.py',223),
  ('collection -> OBR collection_body CBR','collection',3,'p_collection','parser_rules.py',228),
  ('collection_body -> subType COMMA collection_body','collection_body',3,'p_collection_body','parser_rules.py',233),
  ('collection_body -> subType','collection_body',1,'p_collection_body','parser_rules.py',234),
  ('collection_body -> ID COMMA collection_body','collection_body',3,'p_collection_body_ID','parser_rules.py',241),
  ('collection_body -> ID','collection_body',1,'p_collection_body_ID','parser_rules.py',242),
  ('bus -> NAME COMMA collection COMMA collection','bus',5,'p_bus','parser_rules.py',249),
  ('bus -> NAME COMMA ID COMMA ID','bus',5,'p_bus_ID','parser_rules.py',253),
  ('emp -> NAME COMMA SALARY DPOINT NUMBER','emp',5,'p_emp','parser_rules.py',257),
  ('emp -> NAME COMMA SALARY DPOINT ID','emp',5,'p_emp_ID','parser_rules.py',261),
  ('emp -> NAME COMMA SALARY DPOINT operation','emp',5,'p_emp_Oper','parser_rules.py',265),
  ('prod -> NAME COMMA AMOUNT DPOINT NUMBER','prod',5,'p_prod','parser_rules.py',269),
  ('prod -> NAME','prod',1,'p_prod','parser_rules.py',270),
  ('prod -> NAME COMMA AMOUNT DPOINT ID','prod',5,'p_prod_ID','parser_rules.py',277),
  ('prod -> NAME COMMA AMOUNT DPOINT operation','prod',5,'p_prod_Oper','parser_rules.py',281),
]
