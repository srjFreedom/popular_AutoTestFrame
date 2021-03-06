# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import error_code_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='accname.proto',
  package='',
  serialized_pb='\n\raccname.proto\x1a\x10\x65rror_code.proto\"n\n\tc2s_login\x12\r\n\x05token\x18\x01 \x02(\t\x12\x15\n\nplatformID\x18\x02 \x01(\x05:\x01\x30\x12\x13\n\tchannelID\x18\x03 \x01(\t:\x00\x12\x14\n\ndeviceIMEI\x18\x04 \x01(\t:\x00\x12\x10\n\x06\x63lient\x18\x05 \x01(\t:\x00\"4\n\ts2c_login\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\x12\x0c\n\x04time\x18\x02 \x02(\x05\"/\n\x0c\x63\x32s_register\x12\r\n\x05token\x18\x01 \x02(\t\x12\x10\n\x08nickname\x18\x02 \x02(\t\")\n\x0cs2c_register\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\"\x14\n\x12\x63\x32s_get_login_host\"W\n\x12s2c_get_login_host\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x0c\n\x04sign\x18\x04 \x01(\t')




_C2S_LOGIN = descriptor.Descriptor(
  name='c2s_login',
  full_name='c2s_login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='token', full_name='c2s_login.token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='platformID', full_name='c2s_login.platformID', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='channelID', full_name='c2s_login.channelID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='deviceIMEI', full_name='c2s_login.deviceIMEI', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='client', full_name='c2s_login.client', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
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
  serialized_end=145,
)


_S2C_LOGIN = descriptor.Descriptor(
  name='s2c_login',
  full_name='s2c_login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_login.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time', full_name='s2c_login.time', index=1,
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
  serialized_start=147,
  serialized_end=199,
)


_C2S_REGISTER = descriptor.Descriptor(
  name='c2s_register',
  full_name='c2s_register',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='token', full_name='c2s_register.token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nickname', full_name='c2s_register.nickname', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=201,
  serialized_end=248,
)


_S2C_REGISTER = descriptor.Descriptor(
  name='s2c_register',
  full_name='s2c_register',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_register.code', index=0,
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
  serialized_start=250,
  serialized_end=291,
)


_C2S_GET_LOGIN_HOST = descriptor.Descriptor(
  name='c2s_get_login_host',
  full_name='c2s_get_login_host',
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
  serialized_start=293,
  serialized_end=313,
)


_S2C_GET_LOGIN_HOST = descriptor.Descriptor(
  name='s2c_get_login_host',
  full_name='s2c_get_login_host',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_get_login_host.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ip', full_name='s2c_get_login_host.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='port', full_name='s2c_get_login_host.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sign', full_name='s2c_get_login_host.sign', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=315,
  serialized_end=402,
)

_S2C_LOGIN.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_REGISTER.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_GET_LOGIN_HOST.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
DESCRIPTOR.message_types_by_name['c2s_login'] = _C2S_LOGIN
DESCRIPTOR.message_types_by_name['s2c_login'] = _S2C_LOGIN
DESCRIPTOR.message_types_by_name['c2s_register'] = _C2S_REGISTER
DESCRIPTOR.message_types_by_name['s2c_register'] = _S2C_REGISTER
DESCRIPTOR.message_types_by_name['c2s_get_login_host'] = _C2S_GET_LOGIN_HOST
DESCRIPTOR.message_types_by_name['s2c_get_login_host'] = _S2C_GET_LOGIN_HOST

class c2s_login(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_LOGIN
  
  # @@protoc_insertion_point(class_scope:c2s_login)

class s2c_login(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_LOGIN
  
  # @@protoc_insertion_point(class_scope:s2c_login)

class c2s_register(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_REGISTER
  
  # @@protoc_insertion_point(class_scope:c2s_register)

class s2c_register(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_REGISTER
  
  # @@protoc_insertion_point(class_scope:s2c_register)

class c2s_get_login_host(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_GET_LOGIN_HOST
  
  # @@protoc_insertion_point(class_scope:c2s_get_login_host)

class s2c_get_login_host(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_GET_LOGIN_HOST
  
  # @@protoc_insertion_point(class_scope:s2c_get_login_host)

# @@protoc_insertion_point(module_scope)
