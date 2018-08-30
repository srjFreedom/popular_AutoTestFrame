# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import error_code_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='compose.proto',
  package='',
  serialized_pb='\n\rcompose.proto\x1a\x10\x65rror_code.proto\"G\n\x13\x63\x32s_compose_partner\x12\x10\n\x08goods_id\x18\x01 \x02(\x05\x12\x1e\n\x16partner_unique_id_list\x18\x02 \x03(\x03\"U\n\x13s2c_compose_partner\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\x12#\n\x18reward_partner_unique_id\x18\x02 \x01(\x03:\x01\x30\"%\n\x11\x63\x32s_compose_trump\x12\x10\n\x08goods_id\x18\x01 \x02(\x05\"J\n\x11s2c_compose_trump\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\x12\x1a\n\x0fgoods_unique_id\x18\x02 \x01(\x05:\x01\x30')




_C2S_COMPOSE_PARTNER = descriptor.Descriptor(
  name='c2s_compose_partner',
  full_name='c2s_compose_partner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='goods_id', full_name='c2s_compose_partner.goods_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='partner_unique_id_list', full_name='c2s_compose_partner.partner_unique_id_list', index=1,
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
  serialized_start=35,
  serialized_end=106,
)


_S2C_COMPOSE_PARTNER = descriptor.Descriptor(
  name='s2c_compose_partner',
  full_name='s2c_compose_partner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_compose_partner.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reward_partner_unique_id', full_name='s2c_compose_partner.reward_partner_unique_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=108,
  serialized_end=193,
)


_C2S_COMPOSE_TRUMP = descriptor.Descriptor(
  name='c2s_compose_trump',
  full_name='c2s_compose_trump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='goods_id', full_name='c2s_compose_trump.goods_id', index=0,
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
  serialized_start=195,
  serialized_end=232,
)


_S2C_COMPOSE_TRUMP = descriptor.Descriptor(
  name='s2c_compose_trump',
  full_name='s2c_compose_trump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_compose_trump.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='goods_unique_id', full_name='s2c_compose_trump.goods_unique_id', index=1,
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
  serialized_start=234,
  serialized_end=308,
)

_S2C_COMPOSE_PARTNER.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_COMPOSE_TRUMP.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
DESCRIPTOR.message_types_by_name['c2s_compose_partner'] = _C2S_COMPOSE_PARTNER
DESCRIPTOR.message_types_by_name['s2c_compose_partner'] = _S2C_COMPOSE_PARTNER
DESCRIPTOR.message_types_by_name['c2s_compose_trump'] = _C2S_COMPOSE_TRUMP
DESCRIPTOR.message_types_by_name['s2c_compose_trump'] = _S2C_COMPOSE_TRUMP

class c2s_compose_partner(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_COMPOSE_PARTNER
  
  # @@protoc_insertion_point(class_scope:c2s_compose_partner)

class s2c_compose_partner(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_COMPOSE_PARTNER
  
  # @@protoc_insertion_point(class_scope:s2c_compose_partner)

class c2s_compose_trump(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_COMPOSE_TRUMP
  
  # @@protoc_insertion_point(class_scope:c2s_compose_trump)

class s2c_compose_trump(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_COMPOSE_TRUMP
  
  # @@protoc_insertion_point(class_scope:s2c_compose_trump)

# @@protoc_insertion_point(module_scope)