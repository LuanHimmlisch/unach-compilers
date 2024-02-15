
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DUAL END EQUALS ID INT LBRACKET LPAREN MINUS MULTIPLY NUMBER OPERATORS PLUS RBRACKET READ RESERVED RPAREN SEMICOLON SIMBOLS\n    assignment :  ID EQUALS NUMBER\n           |  ID EQUALS expression\n    expression : expression OPERATORS expression\n           | LPAREN expression RPAREN\n           | NUMBER\n           | ID\n    '
    
_lr_action_items = {'ID':([0,3,7,8,],[2,4,4,4,]),'$end':([1,4,5,6,10,11,12,],[0,-6,-1,-2,-5,-3,-4,]),'EQUALS':([2,],[3,]),'NUMBER':([3,7,8,],[5,10,10,]),'LPAREN':([3,7,8,],[7,7,7,]),'OPERATORS':([4,5,6,9,10,11,12,],[-6,-5,8,8,-5,8,-4,]),'RPAREN':([4,9,10,11,12,],[-6,12,-5,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignment':([0,],[1,]),'expression':([3,7,8,],[6,9,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assignment","S'",1,None,None,None),
  ('assignment -> ID EQUALS NUMBER','assignment',3,'p_variable','examen.py',72),
  ('assignment -> ID EQUALS expression','assignment',3,'p_variable','examen.py',73),
  ('expression -> expression OPERATORS expression','expression',3,'p_variable','examen.py',74),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_variable','examen.py',75),
  ('expression -> NUMBER','expression',1,'p_variable','examen.py',76),
  ('expression -> ID','expression',1,'p_variable','examen.py',77),
]
