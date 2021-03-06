# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import error_code_pb2
import common_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='dungeon.proto',
  package='',
  serialized_pb='\n\rdungeon.proto\x1a\x10\x65rror_code.proto\x1a\x0c\x63ommon.proto\"\x16\n\x14\x63\x32s_get_dungeon_info\"9\n\x14s2c_get_dungeon_info\x12!\n\x08\x64ungeons\x18\x01 \x03(\x0b\x32\x0f.p_dungeon_info\"-\n\rc2s_challenge\x12\x0f\n\x07type_id\x18\x01 \x02(\x05\x12\x0b\n\x03pos\x18\x02 \x02(\x05\"F\n\x12\x63\x32s_save_formation\x12\x0f\n\x07type_id\x18\x01 \x02(\x05\x12\x1f\n\tformation\x18\x02 \x02(\x0b\x32\x0c.p_formation\"/\n\x12s2c_save_formation\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\"J\n\rs2c_challenge\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\x12\x1e\n\x07rewards\x18\x02 \x03(\x0b\x32\r.p_reward_msg\"\'\n\x14\x63\x32s_get_dungeon_time\x12\x0f\n\x07type_id\x18\x01 \x02(\x05\"H\n\x14s2c_get_dungeon_time\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\x12\x15\n\x04time\x18\x02 \x01(\x0b\x32\x07.p_time\"2\n\x1f\x63\x32s_buy_dungeon_challenge_count\x12\x0f\n\x07type_id\x18\x01 \x02(\x05\"<\n\x1fs2c_buy_dungeon_challenge_count\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\"\x98\x01\n\x0ep_dungeon_info\x12\x0f\n\x07type_id\x18\x01 \x02(\x05\x12\x15\n\x04time\x18\x02 \x02(\x0b\x32\x07.p_time\x12\x0e\n\x03pos\x18\x03 \x01(\x05:\x01\x31\x12\x1f\n\tformation\x18\x04 \x01(\x0b\x32\x0c.p_formation\x12\x14\n\tbuy_count\x18\x05 \x01(\x05:\x01\x30\x12\x17\n\x0f\x63hallenge_count\x18\x06 \x02(\x05\"3\n\x06p_time\x12\x14\n\topen_time\x18\x01 \x01(\x05:\x01\x30\x12\x13\n\x08\x65nd_time\x18\x02 \x01(\x05:\x01\x30')




_C2S_GET_DUNGEON_INFO = descriptor.Descriptor(
  name='c2s_get_dungeon_info',
  full_name='c2s_get_dungeon_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=49,
  serialized_end=71,
)


_S2C_GET_DUNGEON_INFO = descriptor.Descriptor(
  name='s2c_get_dungeon_info',
  full_name='s2c_get_dungeon_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='dungeons', full_name='s2c_get_dungeon_info.dungeons', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=73,
  serialized_end=130,
)


_C2S_CHALLENGE = descriptor.Descriptor(
  name='c2s_challenge',
  full_name='c2s_challenge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type_id', full_name='c2s_challenge.type_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pos', full_name='c2s_challenge.pos', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=132,
  serialized_end=177,
)


_C2S_SAVE_FORMATION = descriptor.Descriptor(
  name='c2s_save_formation',
  full_name='c2s_save_formation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type_id', full_name='c2s_save_formation.type_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='formation', full_name='c2s_save_formation.formation', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=179,
  serialized_end=249,
)


_S2C_SAVE_FORMATION = descriptor.Descriptor(
  name='s2c_save_formation',
  full_name='s2c_save_formation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_save_formation.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=251,
  serialized_end=298,
)


_S2C_CHALLENGE = descriptor.Descriptor(
  name='s2c_challenge',
  full_name='s2c_challenge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_challenge.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rewards', full_name='s2c_challenge.rewards', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=300,
  serialized_end=374,
)


_C2S_GET_DUNGEON_TIME = descriptor.Descriptor(
  name='c2s_get_dungeon_time',
  full_name='c2s_get_dungeon_time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type_id', full_name='c2s_get_dungeon_time.type_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=376,
  serialized_end=415,
)


_S2C_GET_DUNGEON_TIME = descriptor.Descriptor(
  name='s2c_get_dungeon_time',
  full_name='s2c_get_dungeon_time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_get_dungeon_time.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time', full_name='s2c_get_dungeon_time.time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=417,
  serialized_end=489,
)


_C2S_BUY_DUNGEON_CHALLENGE_COUNT = descriptor.Descriptor(
  name='c2s_buy_dungeon_challenge_count',
  full_name='c2s_buy_dungeon_challenge_count',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type_id', full_name='c2s_buy_dungeon_challenge_count.type_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=491,
  serialized_end=541,
)


_S2C_BUY_DUNGEON_CHALLENGE_COUNT = descriptor.Descriptor(
  name='s2c_buy_dungeon_challenge_count',
  full_name='s2c_buy_dungeon_challenge_count',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_buy_dungeon_challenge_count.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=543,
  serialized_end=603,
)


_P_DUNGEON_INFO = descriptor.Descriptor(
  name='p_dungeon_info',
  full_name='p_dungeon_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type_id', full_name='p_dungeon_info.type_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time', full_name='p_dungeon_info.time', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pos', full_name='p_dungeon_info.pos', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='formation', full_name='p_dungeon_info.formation', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buy_count', full_name='p_dungeon_info.buy_count', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='challenge_count', full_name='p_dungeon_info.challenge_count', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=606,
  serialized_end=758,
)


_P_TIME = descriptor.Descriptor(
  name='p_time',
  full_name='p_time',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='open_time', full_name='p_time.open_time', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_time', full_name='p_time.end_time', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=760,
  serialized_end=811,
)

_S2C_GET_DUNGEON_INFO.fields_by_name['dungeons'].message_type = _P_DUNGEON_INFO
_C2S_SAVE_FORMATION.fields_by_name['formation'].message_type = common_pb2._P_FORMATION
_S2C_SAVE_FORMATION.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_CHALLENGE.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_CHALLENGE.fields_by_name['rewards'].message_type = common_pb2._P_REWARD_MSG
_S2C_GET_DUNGEON_TIME.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_GET_DUNGEON_TIME.fields_by_name['time'].message_type = _P_TIME
_S2C_BUY_DUNGEON_CHALLENGE_COUNT.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_P_DUNGEON_INFO.fields_by_name['time'].message_type = _P_TIME
_P_DUNGEON_INFO.fields_by_name['formation'].message_type = common_pb2._P_FORMATION
DESCRIPTOR.message_types_by_name['c2s_get_dungeon_info'] = _C2S_GET_DUNGEON_INFO
DESCRIPTOR.message_types_by_name['s2c_get_dungeon_info'] = _S2C_GET_DUNGEON_INFO
DESCRIPTOR.message_types_by_name['c2s_challenge'] = _C2S_CHALLENGE
DESCRIPTOR.message_types_by_name['c2s_save_formation'] = _C2S_SAVE_FORMATION
DESCRIPTOR.message_types_by_name['s2c_save_formation'] = _S2C_SAVE_FORMATION
DESCRIPTOR.message_types_by_name['s2c_challenge'] = _S2C_CHALLENGE
DESCRIPTOR.message_types_by_name['c2s_get_dungeon_time'] = _C2S_GET_DUNGEON_TIME
DESCRIPTOR.message_types_by_name['s2c_get_dungeon_time'] = _S2C_GET_DUNGEON_TIME
DESCRIPTOR.message_types_by_name['c2s_buy_dungeon_challenge_count'] = _C2S_BUY_DUNGEON_CHALLENGE_COUNT
DESCRIPTOR.message_types_by_name['s2c_buy_dungeon_challenge_count'] = _S2C_BUY_DUNGEON_CHALLENGE_COUNT
DESCRIPTOR.message_types_by_name['p_dungeon_info'] = _P_DUNGEON_INFO
DESCRIPTOR.message_types_by_name['p_time'] = _P_TIME

class c2s_get_dungeon_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_GET_DUNGEON_INFO
  
  # @@protoc_insertion_point(class_scope:c2s_get_dungeon_info)

class s2c_get_dungeon_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_GET_DUNGEON_INFO
  
  # @@protoc_insertion_point(class_scope:s2c_get_dungeon_info)

class c2s_challenge(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_CHALLENGE
  
  # @@protoc_insertion_point(class_scope:c2s_challenge)

class c2s_save_formation(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_SAVE_FORMATION
  
  # @@protoc_insertion_point(class_scope:c2s_save_formation)

class s2c_save_formation(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_SAVE_FORMATION
  
  # @@protoc_insertion_point(class_scope:s2c_save_formation)

class s2c_challenge(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_CHALLENGE
  
  # @@protoc_insertion_point(class_scope:s2c_challenge)

class c2s_get_dungeon_time(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_GET_DUNGEON_TIME
  
  # @@protoc_insertion_point(class_scope:c2s_get_dungeon_time)

class s2c_get_dungeon_time(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_GET_DUNGEON_TIME
  
  # @@protoc_insertion_point(class_scope:s2c_get_dungeon_time)

class c2s_buy_dungeon_challenge_count(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_BUY_DUNGEON_CHALLENGE_COUNT
  
  # @@protoc_insertion_point(class_scope:c2s_buy_dungeon_challenge_count)

class s2c_buy_dungeon_challenge_count(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_BUY_DUNGEON_CHALLENGE_COUNT
  
  # @@protoc_insertion_point(class_scope:s2c_buy_dungeon_challenge_count)

class p_dungeon_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _P_DUNGEON_INFO
  
  # @@protoc_insertion_point(class_scope:p_dungeon_info)

class p_time(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _P_TIME
  
  # @@protoc_insertion_point(class_scope:p_time)

# @@protoc_insertion_point(module_scope)
