# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import error_code_pb2
import common_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='active.proto',
  package='',
  serialized_pb='\n\x0c\x61\x63tive.proto\x1a\x10\x65rror_code.proto\x1a\x0c\x63ommon.proto\"\x19\n\x17\x63\x32s_get_choose_get_info\"y\n\x17s2c_get_choose_get_info\x12\x11\n\x06\x63hoose\x18\x01 \x01(\x05:\x01\x30\x12\x12\n\nt_end_time\x18\x02 \x02(\x05\x12\x10\n\x08\x65nd_time\x18\x03 \x02(\x05\x12\x0b\n\x03\x64\x61y\x18\x04 \x02(\x05\x12\x18\n\ris_email_send\x18\x05 \x01(\x05:\x01\x30\"\'\n\x15\x63\x32s_choose_get_choose\x12\x0e\n\x06\x63hoose\x18\x01 \x02(\x05\"2\n\x15s2c_choose_get_choose\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\"\x1c\n\x1a\x63\x32s_get_choose_get_history\"D\n\x1as2c_get_choose_get_history\x12&\n\x07history\x18\x01 \x03(\x0b\x32\x15.p_choose_get_history\"`\n\x14p_choose_get_history\x12\x0c\n\x04year\x18\x01 \x02(\x05\x12\r\n\x05month\x18\x02 \x02(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x02(\x05\x12\x0e\n\x06\x64\x61y_th\x18\x04 \x02(\x05\x12\x0e\n\x06\x63hoose\x18\x05 \x02(\x05')




_C2S_GET_CHOOSE_GET_INFO = descriptor.Descriptor(
  name='c2s_get_choose_get_info',
  full_name='c2s_get_choose_get_info',
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
  serialized_start=48,
  serialized_end=73,
)


_S2C_GET_CHOOSE_GET_INFO = descriptor.Descriptor(
  name='s2c_get_choose_get_info',
  full_name='s2c_get_choose_get_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='choose', full_name='s2c_get_choose_get_info.choose', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='t_end_time', full_name='s2c_get_choose_get_info.t_end_time', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_time', full_name='s2c_get_choose_get_info.end_time', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='day', full_name='s2c_get_choose_get_info.day', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_email_send', full_name='s2c_get_choose_get_info.is_email_send', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=75,
  serialized_end=196,
)


_C2S_CHOOSE_GET_CHOOSE = descriptor.Descriptor(
  name='c2s_choose_get_choose',
  full_name='c2s_choose_get_choose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='choose', full_name='c2s_choose_get_choose.choose', index=0,
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
  serialized_start=198,
  serialized_end=237,
)


_S2C_CHOOSE_GET_CHOOSE = descriptor.Descriptor(
  name='s2c_choose_get_choose',
  full_name='s2c_choose_get_choose',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_choose_get_choose.code', index=0,
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
  serialized_start=239,
  serialized_end=289,
)


_C2S_GET_CHOOSE_GET_HISTORY = descriptor.Descriptor(
  name='c2s_get_choose_get_history',
  full_name='c2s_get_choose_get_history',
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
  serialized_start=291,
  serialized_end=319,
)


_S2C_GET_CHOOSE_GET_HISTORY = descriptor.Descriptor(
  name='s2c_get_choose_get_history',
  full_name='s2c_get_choose_get_history',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='history', full_name='s2c_get_choose_get_history.history', index=0,
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
  serialized_start=321,
  serialized_end=389,
)


_P_CHOOSE_GET_HISTORY = descriptor.Descriptor(
  name='p_choose_get_history',
  full_name='p_choose_get_history',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='year', full_name='p_choose_get_history.year', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='month', full_name='p_choose_get_history.month', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='day', full_name='p_choose_get_history.day', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='day_th', full_name='p_choose_get_history.day_th', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='choose', full_name='p_choose_get_history.choose', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_start=391,
  serialized_end=487,
)

_S2C_CHOOSE_GET_CHOOSE.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_GET_CHOOSE_GET_HISTORY.fields_by_name['history'].message_type = _P_CHOOSE_GET_HISTORY
DESCRIPTOR.message_types_by_name['c2s_get_choose_get_info'] = _C2S_GET_CHOOSE_GET_INFO
DESCRIPTOR.message_types_by_name['s2c_get_choose_get_info'] = _S2C_GET_CHOOSE_GET_INFO
DESCRIPTOR.message_types_by_name['c2s_choose_get_choose'] = _C2S_CHOOSE_GET_CHOOSE
DESCRIPTOR.message_types_by_name['s2c_choose_get_choose'] = _S2C_CHOOSE_GET_CHOOSE
DESCRIPTOR.message_types_by_name['c2s_get_choose_get_history'] = _C2S_GET_CHOOSE_GET_HISTORY
DESCRIPTOR.message_types_by_name['s2c_get_choose_get_history'] = _S2C_GET_CHOOSE_GET_HISTORY
DESCRIPTOR.message_types_by_name['p_choose_get_history'] = _P_CHOOSE_GET_HISTORY

class c2s_get_choose_get_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_GET_CHOOSE_GET_INFO
  
  # @@protoc_insertion_point(class_scope:c2s_get_choose_get_info)

class s2c_get_choose_get_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_GET_CHOOSE_GET_INFO
  
  # @@protoc_insertion_point(class_scope:s2c_get_choose_get_info)

class c2s_choose_get_choose(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_CHOOSE_GET_CHOOSE
  
  # @@protoc_insertion_point(class_scope:c2s_choose_get_choose)

class s2c_choose_get_choose(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_CHOOSE_GET_CHOOSE
  
  # @@protoc_insertion_point(class_scope:s2c_choose_get_choose)

class c2s_get_choose_get_history(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_GET_CHOOSE_GET_HISTORY
  
  # @@protoc_insertion_point(class_scope:c2s_get_choose_get_history)

class s2c_get_choose_get_history(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_GET_CHOOSE_GET_HISTORY
  
  # @@protoc_insertion_point(class_scope:s2c_get_choose_get_history)

class p_choose_get_history(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _P_CHOOSE_GET_HISTORY
  
  # @@protoc_insertion_point(class_scope:p_choose_get_history)

# @@protoc_insertion_point(module_scope)