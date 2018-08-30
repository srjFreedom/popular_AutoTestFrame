# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import error_code_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='guide.proto',
  package='',
  serialized_pb='\n\x0bguide.proto\x1a\x10\x65rror_code.proto\";\n\x18\x63\x32s_update_system_active\x12\x1f\n\x07\x61\x63tives\x18\x01 \x03(\x0b\x32\x0e.system_active\"5\n\x18s2c_update_system_active\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\"+\n\x11\x63\x32s_update_guides\x12\x16\n\x06guide1\x18\x01 \x03(\x0b\x32\x06.guide\".\n\x11s2c_update_guides\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\"\x19\n\x17\x63\x32s_download_guide_info\"R\n\x17s2c_download_guide_info\x12\x1f\n\x07\x61\x63tives\x18\x01 \x03(\x0b\x32\x0e.system_active\x12\x16\n\x06guide1\x18\x02 \x03(\x0b\x32\x06.guide\" \n\x12\x63\x32s_guides_changed\x12\n\n\x02id\x18\x01 \x02(\x05\"+\n\rsystem_active\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06\x65\x66\x66\x65\x63t\x18\x02 \x02(\x05\"\"\n\x05guide\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05state\x18\x02 \x02(\t')




_C2S_UPDATE_SYSTEM_ACTIVE = descriptor.Descriptor(
  name='c2s_update_system_active',
  full_name='c2s_update_system_active',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='actives', full_name='c2s_update_system_active.actives', index=0,
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
  serialized_start=33,
  serialized_end=92,
)


_S2C_UPDATE_SYSTEM_ACTIVE = descriptor.Descriptor(
  name='s2c_update_system_active',
  full_name='s2c_update_system_active',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_update_system_active.code', index=0,
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
  serialized_start=94,
  serialized_end=147,
)


_C2S_UPDATE_GUIDES = descriptor.Descriptor(
  name='c2s_update_guides',
  full_name='c2s_update_guides',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='guide1', full_name='c2s_update_guides.guide1', index=0,
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
  serialized_start=149,
  serialized_end=192,
)


_S2C_UPDATE_GUIDES = descriptor.Descriptor(
  name='s2c_update_guides',
  full_name='s2c_update_guides',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_update_guides.code', index=0,
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
  serialized_start=194,
  serialized_end=240,
)


_C2S_DOWNLOAD_GUIDE_INFO = descriptor.Descriptor(
  name='c2s_download_guide_info',
  full_name='c2s_download_guide_info',
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
  serialized_start=242,
  serialized_end=267,
)


_S2C_DOWNLOAD_GUIDE_INFO = descriptor.Descriptor(
  name='s2c_download_guide_info',
  full_name='s2c_download_guide_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='actives', full_name='s2c_download_guide_info.actives', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='guide1', full_name='s2c_download_guide_info.guide1', index=1,
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
  serialized_start=269,
  serialized_end=351,
)


_C2S_GUIDES_CHANGED = descriptor.Descriptor(
  name='c2s_guides_changed',
  full_name='c2s_guides_changed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='c2s_guides_changed.id', index=0,
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
  serialized_start=353,
  serialized_end=385,
)


_SYSTEM_ACTIVE = descriptor.Descriptor(
  name='system_active',
  full_name='system_active',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='system_active.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='effect', full_name='system_active.effect', index=1,
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
  serialized_start=387,
  serialized_end=430,
)


_GUIDE = descriptor.Descriptor(
  name='guide',
  full_name='guide',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='guide.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='state', full_name='guide.state', index=1,
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
  serialized_start=432,
  serialized_end=466,
)

_C2S_UPDATE_SYSTEM_ACTIVE.fields_by_name['actives'].message_type = _SYSTEM_ACTIVE
_S2C_UPDATE_SYSTEM_ACTIVE.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_C2S_UPDATE_GUIDES.fields_by_name['guide1'].message_type = _GUIDE
_S2C_UPDATE_GUIDES.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_DOWNLOAD_GUIDE_INFO.fields_by_name['actives'].message_type = _SYSTEM_ACTIVE
_S2C_DOWNLOAD_GUIDE_INFO.fields_by_name['guide1'].message_type = _GUIDE
DESCRIPTOR.message_types_by_name['c2s_update_system_active'] = _C2S_UPDATE_SYSTEM_ACTIVE
DESCRIPTOR.message_types_by_name['s2c_update_system_active'] = _S2C_UPDATE_SYSTEM_ACTIVE
DESCRIPTOR.message_types_by_name['c2s_update_guides'] = _C2S_UPDATE_GUIDES
DESCRIPTOR.message_types_by_name['s2c_update_guides'] = _S2C_UPDATE_GUIDES
DESCRIPTOR.message_types_by_name['c2s_download_guide_info'] = _C2S_DOWNLOAD_GUIDE_INFO
DESCRIPTOR.message_types_by_name['s2c_download_guide_info'] = _S2C_DOWNLOAD_GUIDE_INFO
DESCRIPTOR.message_types_by_name['c2s_guides_changed'] = _C2S_GUIDES_CHANGED
DESCRIPTOR.message_types_by_name['system_active'] = _SYSTEM_ACTIVE
DESCRIPTOR.message_types_by_name['guide'] = _GUIDE

class c2s_update_system_active(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_UPDATE_SYSTEM_ACTIVE
  
  # @@protoc_insertion_point(class_scope:c2s_update_system_active)

class s2c_update_system_active(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_UPDATE_SYSTEM_ACTIVE
  
  # @@protoc_insertion_point(class_scope:s2c_update_system_active)

class c2s_update_guides(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_UPDATE_GUIDES
  
  # @@protoc_insertion_point(class_scope:c2s_update_guides)

class s2c_update_guides(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_UPDATE_GUIDES
  
  # @@protoc_insertion_point(class_scope:s2c_update_guides)

class c2s_download_guide_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_DOWNLOAD_GUIDE_INFO
  
  # @@protoc_insertion_point(class_scope:c2s_download_guide_info)

class s2c_download_guide_info(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_DOWNLOAD_GUIDE_INFO
  
  # @@protoc_insertion_point(class_scope:s2c_download_guide_info)

class c2s_guides_changed(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_GUIDES_CHANGED
  
  # @@protoc_insertion_point(class_scope:c2s_guides_changed)

class system_active(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYSTEM_ACTIVE
  
  # @@protoc_insertion_point(class_scope:system_active)

class guide(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GUIDE
  
  # @@protoc_insertion_point(class_scope:guide)

# @@protoc_insertion_point(module_scope)
