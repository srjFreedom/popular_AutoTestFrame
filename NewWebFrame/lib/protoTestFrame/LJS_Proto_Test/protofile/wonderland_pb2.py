# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import error_code_pb2
import common_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='wonderland.proto',
  package='',
  serialized_pb='\n\x10wonderland.proto\x1a\x10\x65rror_code.proto\x1a\x0c\x63ommon.proto\"b\n\x17\x63\x32s_wonderland_register\x12\x15\n\rwonderland_id\x18\x01 \x02(\x05\x12\x1e\n\x16partner_unique_id_list\x18\x02 \x03(\x03\x12\x10\n\x08major_id\x18\x03 \x02(\x05\"_\n\x17s2c_wonderland_register\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\x12\x14\n\x0copened_boxes\x18\x02 \x03(\x05\x12\x13\n\x0bpass_reward\x18\x03 \x01(\x05\",\n\x13\x63\x32s_wonderland_pass\x12\x15\n\rwonderland_id\x18\x01 \x02(\x05\"G\n\x13s2c_wonderland_pass\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\x12\x15\n\rwonderland_id\x18\x02 \x01(\x05\"@\n\x17\x63\x32s_wonderland_open_box\x12\x15\n\rwonderland_id\x18\x01 \x02(\x05\x12\x0e\n\x06\x62ox_id\x18\x02 \x02(\x05\"4\n\x17s2c_wonderland_open_box\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\"\x19\n\x17\x63\x32s_get_wonderland_list\"A\n\x17s2c_get_wonderland_list\x12&\n\x0fwonderland_list\x18\x01 \x03(\x0b\x32\r.p_wonderland\"S\n\x0cp_wonderland\x12\x15\n\rwonderland_id\x18\x01 \x02(\x05\x12\x14\n\x0copened_boxes\x18\x02 \x03(\x05\x12\x16\n\x0bpass_reward\x18\x03 \x01(\x05:\x01\x31')




_C2S_WONDERLAND_REGISTER = descriptor.Descriptor(
  name='c2s_wonderland_register',
  full_name='c2s_wonderland_register',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='wonderland_id', full_name='c2s_wonderland_register.wonderland_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='partner_unique_id_list', full_name='c2s_wonderland_register.partner_unique_id_list', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='major_id', full_name='c2s_wonderland_register.major_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=52,
  serialized_end=150,
)


_S2C_WONDERLAND_REGISTER = descriptor.Descriptor(
  name='s2c_wonderland_register',
  full_name='s2c_wonderland_register',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_wonderland_register.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='opened_boxes', full_name='s2c_wonderland_register.opened_boxes', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pass_reward', full_name='s2c_wonderland_register.pass_reward', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=152,
  serialized_end=247,
)


_C2S_WONDERLAND_PASS = descriptor.Descriptor(
  name='c2s_wonderland_pass',
  full_name='c2s_wonderland_pass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='wonderland_id', full_name='c2s_wonderland_pass.wonderland_id', index=0,
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
  serialized_start=249,
  serialized_end=293,
)


_S2C_WONDERLAND_PASS = descriptor.Descriptor(
  name='s2c_wonderland_pass',
  full_name='s2c_wonderland_pass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_wonderland_pass.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wonderland_id', full_name='s2c_wonderland_pass.wonderland_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=295,
  serialized_end=366,
)


_C2S_WONDERLAND_OPEN_BOX = descriptor.Descriptor(
  name='c2s_wonderland_open_box',
  full_name='c2s_wonderland_open_box',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='wonderland_id', full_name='c2s_wonderland_open_box.wonderland_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='box_id', full_name='c2s_wonderland_open_box.box_id', index=1,
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
  serialized_start=368,
  serialized_end=432,
)


_S2C_WONDERLAND_OPEN_BOX = descriptor.Descriptor(
  name='s2c_wonderland_open_box',
  full_name='s2c_wonderland_open_box',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_wonderland_open_box.code', index=0,
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
  serialized_start=434,
  serialized_end=486,
)


_C2S_GET_WONDERLAND_LIST = descriptor.Descriptor(
  name='c2s_get_wonderland_list',
  full_name='c2s_get_wonderland_list',
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
  serialized_start=488,
  serialized_end=513,
)


_S2C_GET_WONDERLAND_LIST = descriptor.Descriptor(
  name='s2c_get_wonderland_list',
  full_name='s2c_get_wonderland_list',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='wonderland_list', full_name='s2c_get_wonderland_list.wonderland_list', index=0,
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
  serialized_start=515,
  serialized_end=580,
)


_P_WONDERLAND = descriptor.Descriptor(
  name='p_wonderland',
  full_name='p_wonderland',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='wonderland_id', full_name='p_wonderland.wonderland_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='opened_boxes', full_name='p_wonderland.opened_boxes', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pass_reward', full_name='p_wonderland.pass_reward', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=582,
  serialized_end=665,
)

_S2C_WONDERLAND_REGISTER.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_WONDERLAND_PASS.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_WONDERLAND_OPEN_BOX.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_GET_WONDERLAND_LIST.fields_by_name['wonderland_list'].message_type = _P_WONDERLAND
DESCRIPTOR.message_types_by_name['c2s_wonderland_register'] = _C2S_WONDERLAND_REGISTER
DESCRIPTOR.message_types_by_name['s2c_wonderland_register'] = _S2C_WONDERLAND_REGISTER
DESCRIPTOR.message_types_by_name['c2s_wonderland_pass'] = _C2S_WONDERLAND_PASS
DESCRIPTOR.message_types_by_name['s2c_wonderland_pass'] = _S2C_WONDERLAND_PASS
DESCRIPTOR.message_types_by_name['c2s_wonderland_open_box'] = _C2S_WONDERLAND_OPEN_BOX
DESCRIPTOR.message_types_by_name['s2c_wonderland_open_box'] = _S2C_WONDERLAND_OPEN_BOX
DESCRIPTOR.message_types_by_name['c2s_get_wonderland_list'] = _C2S_GET_WONDERLAND_LIST
DESCRIPTOR.message_types_by_name['s2c_get_wonderland_list'] = _S2C_GET_WONDERLAND_LIST
DESCRIPTOR.message_types_by_name['p_wonderland'] = _P_WONDERLAND

class c2s_wonderland_register(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_WONDERLAND_REGISTER
  
  # @@protoc_insertion_point(class_scope:c2s_wonderland_register)

class s2c_wonderland_register(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_WONDERLAND_REGISTER
  
  # @@protoc_insertion_point(class_scope:s2c_wonderland_register)

class c2s_wonderland_pass(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_WONDERLAND_PASS
  
  # @@protoc_insertion_point(class_scope:c2s_wonderland_pass)

class s2c_wonderland_pass(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_WONDERLAND_PASS
  
  # @@protoc_insertion_point(class_scope:s2c_wonderland_pass)

class c2s_wonderland_open_box(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_WONDERLAND_OPEN_BOX
  
  # @@protoc_insertion_point(class_scope:c2s_wonderland_open_box)

class s2c_wonderland_open_box(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_WONDERLAND_OPEN_BOX
  
  # @@protoc_insertion_point(class_scope:s2c_wonderland_open_box)

class c2s_get_wonderland_list(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_GET_WONDERLAND_LIST
  
  # @@protoc_insertion_point(class_scope:c2s_get_wonderland_list)

class s2c_get_wonderland_list(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_GET_WONDERLAND_LIST
  
  # @@protoc_insertion_point(class_scope:s2c_get_wonderland_list)

class p_wonderland(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _P_WONDERLAND
  
  # @@protoc_insertion_point(class_scope:p_wonderland)

# @@protoc_insertion_point(module_scope)
