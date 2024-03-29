# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chess_game.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chess_game.proto',
  package='chess_game',
  syntax='proto3',
  serialized_options=b'P\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x63hess_game.proto\x12\nchess_game\"\x1a\n\tGameState\x12\r\n\x05state\x18\x01 \x01(\t\"\x13\n\x03row\x12\x0c\n\x04item\x18\x01 \x03(\t\"+\n\x05\x62oard\x12\"\n\tboard_row\x18\x01 \x03(\x0b\x32\x0f.chess_game.row\"*\n\x08new_move\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08new_move\x18\x02 \x01(\t\"\x91\x02\n\x0b\x61\x63knowledge\x12\x12\n\x05state\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06moving\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x12\n\x05legal\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x12\n\x05moved\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x12\n\x05\x63heck\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x15\n\x08location\x18\x06 \x01(\tH\x05\x88\x01\x01\x12\x19\n\x0cnew_location\x18\x07 \x01(\tH\x06\x88\x01\x01\x12\x11\n\x04kill\x18\x08 \x01(\x08H\x07\x88\x01\x01\x42\x08\n\x06_stateB\t\n\x07_movingB\x08\n\x06_legalB\x08\n\x06_movedB\x08\n\x06_checkB\x0b\n\t_locationB\x0f\n\r_new_locationB\x07\n\x05_kill\"\x16\n\x05Guess\x12\r\n\x05guess\x18\x01 \x01(\x05\"\x18\n\x08\x46\x65\x65\x64\x62\x61\x63k\x12\x0c\n\x04\x66\x65\x65\x64\x18\x01 \x01(\t\"\x14\n\x04Name\x12\x0c\n\x04name\x18\x01 \x01(\t2\xac\x02\n\tChessGame\x12:\n\x0b\x63heck_state\x12\x10.chess_game.Name\x1a\x17.chess_game.acknowledge\"\x00\x12;\n\x0cupdate_state\x12\x10.chess_game.Name\x1a\x17.chess_game.acknowledge\"\x00\x12:\n\x0bprint_board\x12\x10.chess_game.Name\x1a\x17.chess_game.acknowledge\"\x00\x12\x31\n\tset_piece\x12\x10.chess_game.Name\x1a\x10.chess_game.Name\"\x00\x12\x37\n\x04move\x12\x14.chess_game.new_move\x1a\x17.chess_game.acknowledge\"\x00\x42\x02P\x01\x62\x06proto3'
)




_GAMESTATE = _descriptor.Descriptor(
  name='GameState',
  full_name='chess_game.GameState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='chess_game.GameState.state', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=58,
)


_ROW = _descriptor.Descriptor(
  name='row',
  full_name='chess_game.row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='chess_game.row.item', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=79,
)


_BOARD = _descriptor.Descriptor(
  name='board',
  full_name='chess_game.board',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='board_row', full_name='chess_game.board.board_row', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=124,
)


_NEW_MOVE = _descriptor.Descriptor(
  name='new_move',
  full_name='chess_game.new_move',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chess_game.new_move.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_move', full_name='chess_game.new_move.new_move', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=168,
)


_ACKNOWLEDGE = _descriptor.Descriptor(
  name='acknowledge',
  full_name='chess_game.acknowledge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='chess_game.acknowledge.state', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='moving', full_name='chess_game.acknowledge.moving', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='legal', full_name='chess_game.acknowledge.legal', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='moved', full_name='chess_game.acknowledge.moved', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='check', full_name='chess_game.acknowledge.check', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='chess_game.acknowledge.location', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_location', full_name='chess_game.acknowledge.new_location', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kill', full_name='chess_game.acknowledge.kill', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_state', full_name='chess_game.acknowledge._state',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_moving', full_name='chess_game.acknowledge._moving',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_legal', full_name='chess_game.acknowledge._legal',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_moved', full_name='chess_game.acknowledge._moved',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_check', full_name='chess_game.acknowledge._check',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_location', full_name='chess_game.acknowledge._location',
      index=5, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_new_location', full_name='chess_game.acknowledge._new_location',
      index=6, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_kill', full_name='chess_game.acknowledge._kill',
      index=7, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=171,
  serialized_end=444,
)


_GUESS = _descriptor.Descriptor(
  name='Guess',
  full_name='chess_game.Guess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='guess', full_name='chess_game.Guess.guess', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=446,
  serialized_end=468,
)


_FEEDBACK = _descriptor.Descriptor(
  name='Feedback',
  full_name='chess_game.Feedback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='feed', full_name='chess_game.Feedback.feed', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=470,
  serialized_end=494,
)


_NAME = _descriptor.Descriptor(
  name='Name',
  full_name='chess_game.Name',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='chess_game.Name.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=496,
  serialized_end=516,
)

_BOARD.fields_by_name['board_row'].message_type = _ROW
_ACKNOWLEDGE.oneofs_by_name['_state'].fields.append(
  _ACKNOWLEDGE.fields_by_name['state'])
_ACKNOWLEDGE.fields_by_name['state'].containing_oneof = _ACKNOWLEDGE.oneofs_by_name['_state']
_ACKNOWLEDGE.oneofs_by_name['_moving'].fields.append(
  _ACKNOWLEDGE.fields_by_name['moving'])
_ACKNOWLEDGE.fields_by_name['moving'].containing_oneof = _ACKNOWLEDGE.oneofs_by_name['_moving']
_ACKNOWLEDGE.oneofs_by_name['_legal'].fields.append(
  _ACKNOWLEDGE.fields_by_name['legal'])
_ACKNOWLEDGE.fields_by_name['legal'].containing_oneof = _ACKNOWLEDGE.oneofs_by_name['_legal']
_ACKNOWLEDGE.oneofs_by_name['_moved'].fields.append(
  _ACKNOWLEDGE.fields_by_name['moved'])
_ACKNOWLEDGE.fields_by_name['moved'].containing_oneof = _ACKNOWLEDGE.oneofs_by_name['_moved']
_ACKNOWLEDGE.oneofs_by_name['_check'].fields.append(
  _ACKNOWLEDGE.fields_by_name['check'])
_ACKNOWLEDGE.fields_by_name['check'].containing_oneof = _ACKNOWLEDGE.oneofs_by_name['_check']
_ACKNOWLEDGE.oneofs_by_name['_location'].fields.append(
  _ACKNOWLEDGE.fields_by_name['location'])
_ACKNOWLEDGE.fields_by_name['location'].containing_oneof = _ACKNOWLEDGE.oneofs_by_name['_location']
_ACKNOWLEDGE.oneofs_by_name['_new_location'].fields.append(
  _ACKNOWLEDGE.fields_by_name['new_location'])
_ACKNOWLEDGE.fields_by_name['new_location'].containing_oneof = _ACKNOWLEDGE.oneofs_by_name['_new_location']
_ACKNOWLEDGE.oneofs_by_name['_kill'].fields.append(
  _ACKNOWLEDGE.fields_by_name['kill'])
_ACKNOWLEDGE.fields_by_name['kill'].containing_oneof = _ACKNOWLEDGE.oneofs_by_name['_kill']
DESCRIPTOR.message_types_by_name['GameState'] = _GAMESTATE
DESCRIPTOR.message_types_by_name['row'] = _ROW
DESCRIPTOR.message_types_by_name['board'] = _BOARD
DESCRIPTOR.message_types_by_name['new_move'] = _NEW_MOVE
DESCRIPTOR.message_types_by_name['acknowledge'] = _ACKNOWLEDGE
DESCRIPTOR.message_types_by_name['Guess'] = _GUESS
DESCRIPTOR.message_types_by_name['Feedback'] = _FEEDBACK
DESCRIPTOR.message_types_by_name['Name'] = _NAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameState = _reflection.GeneratedProtocolMessageType('GameState', (_message.Message,), {
  'DESCRIPTOR' : _GAMESTATE,
  '__module__' : 'chess_game_pb2'
  # @@protoc_insertion_point(class_scope:chess_game.GameState)
  })
_sym_db.RegisterMessage(GameState)

row = _reflection.GeneratedProtocolMessageType('row', (_message.Message,), {
  'DESCRIPTOR' : _ROW,
  '__module__' : 'chess_game_pb2'
  # @@protoc_insertion_point(class_scope:chess_game.row)
  })
_sym_db.RegisterMessage(row)

board = _reflection.GeneratedProtocolMessageType('board', (_message.Message,), {
  'DESCRIPTOR' : _BOARD,
  '__module__' : 'chess_game_pb2'
  # @@protoc_insertion_point(class_scope:chess_game.board)
  })
_sym_db.RegisterMessage(board)

new_move = _reflection.GeneratedProtocolMessageType('new_move', (_message.Message,), {
  'DESCRIPTOR' : _NEW_MOVE,
  '__module__' : 'chess_game_pb2'
  # @@protoc_insertion_point(class_scope:chess_game.new_move)
  })
_sym_db.RegisterMessage(new_move)

acknowledge = _reflection.GeneratedProtocolMessageType('acknowledge', (_message.Message,), {
  'DESCRIPTOR' : _ACKNOWLEDGE,
  '__module__' : 'chess_game_pb2'
  # @@protoc_insertion_point(class_scope:chess_game.acknowledge)
  })
_sym_db.RegisterMessage(acknowledge)

Guess = _reflection.GeneratedProtocolMessageType('Guess', (_message.Message,), {
  'DESCRIPTOR' : _GUESS,
  '__module__' : 'chess_game_pb2'
  # @@protoc_insertion_point(class_scope:chess_game.Guess)
  })
_sym_db.RegisterMessage(Guess)

Feedback = _reflection.GeneratedProtocolMessageType('Feedback', (_message.Message,), {
  'DESCRIPTOR' : _FEEDBACK,
  '__module__' : 'chess_game_pb2'
  # @@protoc_insertion_point(class_scope:chess_game.Feedback)
  })
_sym_db.RegisterMessage(Feedback)

Name = _reflection.GeneratedProtocolMessageType('Name', (_message.Message,), {
  'DESCRIPTOR' : _NAME,
  '__module__' : 'chess_game_pb2'
  # @@protoc_insertion_point(class_scope:chess_game.Name)
  })
_sym_db.RegisterMessage(Name)


DESCRIPTOR._options = None

_CHESSGAME = _descriptor.ServiceDescriptor(
  name='ChessGame',
  full_name='chess_game.ChessGame',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=519,
  serialized_end=819,
  methods=[
  _descriptor.MethodDescriptor(
    name='check_state',
    full_name='chess_game.ChessGame.check_state',
    index=0,
    containing_service=None,
    input_type=_NAME,
    output_type=_ACKNOWLEDGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update_state',
    full_name='chess_game.ChessGame.update_state',
    index=1,
    containing_service=None,
    input_type=_NAME,
    output_type=_ACKNOWLEDGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='print_board',
    full_name='chess_game.ChessGame.print_board',
    index=2,
    containing_service=None,
    input_type=_NAME,
    output_type=_ACKNOWLEDGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='set_piece',
    full_name='chess_game.ChessGame.set_piece',
    index=3,
    containing_service=None,
    input_type=_NAME,
    output_type=_NAME,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='move',
    full_name='chess_game.ChessGame.move',
    index=4,
    containing_service=None,
    input_type=_NEW_MOVE,
    output_type=_ACKNOWLEDGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHESSGAME)

DESCRIPTOR.services_by_name['ChessGame'] = _CHESSGAME

# @@protoc_insertion_point(module_scope)
