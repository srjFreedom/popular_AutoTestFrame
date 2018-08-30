# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import error_code_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='draw.proto',
  package='',
  serialized_pb='\n\ndraw.proto\x1a\x10\x65rror_code.proto\"5\n\x08\x63\x32s_draw\x12\x0f\n\x07pool_id\x18\x01 \x02(\x05\x12\x18\n\x04type\x18\x02 \x02(\x0e\x32\n.draw_type\"A\n\x08s2c_draw\x12\x15\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code\x12\x1e\n\x16partner_unique_id_list\x18\x02 \x03(\x03\"\x10\n\x0e\x63\x32s_enter_draw*\'\n\tdraw_type\x12\x0c\n\x08\x64raw_one\x10\x01\x12\x0c\n\x08\x64raw_ten\x10\n')

_DRAW_TYPE = descriptor.EnumDescriptor(
  name='draw_type',
  full_name='draw_type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='draw_one', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='draw_ten', index=1, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=172,
  serialized_end=211,
)


draw_one = 1
draw_ten = 10



_C2S_DRAW = descriptor.Descriptor(
  name='c2s_draw',
  full_name='c2s_draw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pool_id', full_name='c2s_draw.pool_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='c2s_draw.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
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
  serialized_start=32,
  serialized_end=85,
)


_S2C_DRAW = descriptor.Descriptor(
  name='s2c_draw',
  full_name='s2c_draw',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_draw.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='partner_unique_id_list', full_name='s2c_draw.partner_unique_id_list', index=1,
      number=2, type=3, cpp_type=2, label=3,
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
  serialized_start=87,
  serialized_end=152,
)


_C2S_ENTER_DRAW = descriptor.Descriptor(
  name='c2s_enter_draw',
  full_name='c2s_enter_draw',
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
  serialized_start=154,
  serialized_end=170,
)

_C2S_DRAW.fields_by_name['type'].enum_type = _DRAW_TYPE
_S2C_DRAW.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
DESCRIPTOR.message_types_by_name['c2s_draw'] = _C2S_DRAW
DESCRIPTOR.message_types_by_name['s2c_draw'] = _S2C_DRAW
DESCRIPTOR.message_types_by_name['c2s_enter_draw'] = _C2S_ENTER_DRAW

class c2s_draw(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_DRAW
  
  # @@protoc_insertion_point(class_scope:c2s_draw)

class s2c_draw(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_DRAW
  
  # @@protoc_insertion_point(class_scope:s2c_draw)

class c2s_enter_draw(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_ENTER_DRAW
  
  # @@protoc_insertion_point(class_scope:c2s_enter_draw)

# @@protoc_insertion_point(module_scope)