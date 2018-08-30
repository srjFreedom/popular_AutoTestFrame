# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import error_code_pb2
import common_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='sign.proto',
  package='',
  serialized_pb='\n\nsign.proto\x1a\x10\x65rror_code.proto\x1a\x0c\x63ommon.proto\"\x13\n\x11\x63\x32s_get_sign_info\"[\n\x11s2c_get_sign_info\x12\x0e\n\x03\x64\x61y\x18\x01 \x01(\x05:\x01\x31\x12\x12\n\x07is_sign\x18\x02 \x01(\x05:\x01\x31\x12\"\n\x0breward_list\x18\x03 \x03(\x0b\x32\r.p_reward_day\"\n\n\x08\x63\x32s_sign\"%\n\x08s2c_sign\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\"-\n\x0cp_reward_day\x12\x1d\n\x06reward\x18\x01 \x03(\x0b\x32\r.p_reward_msg')




_C2S_GET_SIGN_INFO = descriptor.Descriptor(
  name='c2s_get_sign_info',
  full_name='c2s_get_sign_info',
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
  serialized_start=46,
  serialized_end=65,
)


_S2C_GET_SIGN_INFO = descriptor.Descriptor(
  name='s2c_get_sign_info',
  full_name='s2c_get_sign_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='day', full_name='s2c_get_sign_info.day', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_sign', full_name='s2c_get_sign_info.is_sign', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reward_list', full_name='s2c_get_sign_info.reward_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=67,
  serialized_end=158,
)


_C2S_SIGN = descriptor.Descriptor(
  name='c2s_sign',
  full_name='c2s_sign',
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
  serialized_start=160,
  serialized_end=170,
)


_S2C_SIGN = descriptor.Descriptor(
  name='s2c_sign',
  full_name='s2c_sign',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_sign.code', index=0,
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
  serialized_start=172,
  serialized_end=209,
)


_P_REWARD_DAY = descriptor.Descriptor(
  name='p_reward_day',
  full_name='p_reward_day',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='reward', full_name='p_reward_day.reward', index=0,
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
  serialized_start=211,
  serialized_end=256,
)

_S2C_GET_SIGN_INFO.fields_by_name['reward_list'].message_type = _P_REWARD_DAY
_S2C_SIGN.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_P_REWARD_DAY.fields_by_name['reward'].message_type = common_pb2._P_REWARD_MSG
DESCRIPTOR.message_types_by_name['c2s_get_sign_info'] = _C2S_GET_SIGN_INFO
DESCRIPTOR.message_types_by_name['s2c_get_sign_info'] = _S2C_GET_SIGN_INFO
DESCRIPTOR.message_types_by_name['c2s_sign'] = _C2S_SIGN
DESCRIPTOR.message_types_by_name['s2c_sign'] = _S2C_SIGN
DESCRIPTOR.message_types_by_name['p_reward_day'] = _P_REWARD_DAY

class c2s_get_sign_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_GET_SIGN_INFO
  
  # @@protoc_insertion_point(class_scope:c2s_get_sign_info)

class s2c_get_sign_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_GET_SIGN_INFO
  
  # @@protoc_insertion_point(class_scope:s2c_get_sign_info)

class c2s_sign(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_SIGN
  
  # @@protoc_insertion_point(class_scope:c2s_sign)

class s2c_sign(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_SIGN
  
  # @@protoc_insertion_point(class_scope:s2c_sign)

class p_reward_day(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _P_REWARD_DAY
  
  # @@protoc_insertion_point(class_scope:p_reward_day)

# @@protoc_insertion_point(module_scope)