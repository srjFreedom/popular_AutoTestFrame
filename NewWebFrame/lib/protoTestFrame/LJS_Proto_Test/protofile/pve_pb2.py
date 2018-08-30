# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import error_code_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='pve.proto',
  package='',
  serialized_pb='\n\tpve.proto\x1a\x10\x65rror_code.proto\"%\n\x0e\x63\x32s_upload_pve\x12\x13\n\x0btrigger_ids\x18\x01 \x03(\x05\"\'\n\x0es2c_upload_pve\x12\x15\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code\"\x12\n\x10\x63\x32s_download_pve\"t\n\x10s2c_download_pve\x12\x0c\n\x04main\x18\x01 \x02(\x05\x12\x0f\n\x07\x62ranch1\x18\x02 \x02(\x05\x12\x0f\n\x07\x62ranch2\x18\x03 \x02(\x05\x12\x0f\n\x07\x62ranch3\x18\x04 \x02(\x05\x12\x0f\n\x07\x62ranch4\x18\x05 \x02(\x05\x12\x0e\n\x06global\x18\x06 \x03(\x05\"2\n\x15\x63\x32s_pve_battle_reward\x12\x19\n\x06\x62\x61ttle\x18\x01 \x03(\x0b\x32\t.p_battle\"2\n\x15s2c_pve_battle_reward\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\"9\n\x08p_battle\x12\x11\n\tbattle_id\x18\x01 \x01(\x05\x12\x1a\n\x12partner_unique_ids\x18\x02 \x03(\x03\"(\n\x19\x63\x32s_upload_pve_player_pos\x12\x0b\n\x03pos\x18\x01 \x02(\x05\"6\n\x19s2c_upload_pve_player_pos\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\"@\n\x1b\x63\x32s_upload_pve_object_state\x12!\n\x04list\x18\x02 \x03(\x0b\x32\x13.p_pve_object_state\"8\n\x1bs2c_upload_pve_object_state\x12\x19\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x07.e_code:\x02ok\"X\n\x12p_pve_object_state\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0b\n\x03pos\x18\x02 \x02(\x05\x12\x0b\n\x03\x64ir\x18\x03 \x02(\x05\x12\x1c\n\x11\x63reate_or_destroy\x18\x04 \x01(\x05:\x01\x31\"\x18\n\x16\x63\x32s_download_pve_state\"H\n\x16s2c_download_pve_state\x12\x0b\n\x03pos\x18\x01 \x02(\x05\x12!\n\x04list\x18\x02 \x03(\x0b\x32\x13.p_pve_object_state')




_C2S_UPLOAD_PVE = descriptor.Descriptor(
  name='c2s_upload_pve',
  full_name='c2s_upload_pve',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='trigger_ids', full_name='c2s_upload_pve.trigger_ids', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=31,
  serialized_end=68,
)


_S2C_UPLOAD_PVE = descriptor.Descriptor(
  name='s2c_upload_pve',
  full_name='s2c_upload_pve',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_upload_pve.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=70,
  serialized_end=109,
)


_C2S_DOWNLOAD_PVE = descriptor.Descriptor(
  name='c2s_download_pve',
  full_name='c2s_download_pve',
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
  serialized_start=111,
  serialized_end=129,
)


_S2C_DOWNLOAD_PVE = descriptor.Descriptor(
  name='s2c_download_pve',
  full_name='s2c_download_pve',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='main', full_name='s2c_download_pve.main', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='branch1', full_name='s2c_download_pve.branch1', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='branch2', full_name='s2c_download_pve.branch2', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='branch3', full_name='s2c_download_pve.branch3', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='branch4', full_name='s2c_download_pve.branch4', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='global', full_name='s2c_download_pve.global', index=5,
      number=6, type=5, cpp_type=1, label=3,
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
  serialized_start=131,
  serialized_end=247,
)


_C2S_PVE_BATTLE_REWARD = descriptor.Descriptor(
  name='c2s_pve_battle_reward',
  full_name='c2s_pve_battle_reward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='battle', full_name='c2s_pve_battle_reward.battle', index=0,
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
  serialized_start=249,
  serialized_end=299,
)


_S2C_PVE_BATTLE_REWARD = descriptor.Descriptor(
  name='s2c_pve_battle_reward',
  full_name='s2c_pve_battle_reward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_pve_battle_reward.code', index=0,
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
  serialized_start=301,
  serialized_end=351,
)


_P_BATTLE = descriptor.Descriptor(
  name='p_battle',
  full_name='p_battle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='battle_id', full_name='p_battle.battle_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='partner_unique_ids', full_name='p_battle.partner_unique_ids', index=1,
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
  serialized_start=353,
  serialized_end=410,
)


_C2S_UPLOAD_PVE_PLAYER_POS = descriptor.Descriptor(
  name='c2s_upload_pve_player_pos',
  full_name='c2s_upload_pve_player_pos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pos', full_name='c2s_upload_pve_player_pos.pos', index=0,
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
  serialized_start=412,
  serialized_end=452,
)


_S2C_UPLOAD_PVE_PLAYER_POS = descriptor.Descriptor(
  name='s2c_upload_pve_player_pos',
  full_name='s2c_upload_pve_player_pos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_upload_pve_player_pos.code', index=0,
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
  serialized_start=454,
  serialized_end=508,
)


_C2S_UPLOAD_PVE_OBJECT_STATE = descriptor.Descriptor(
  name='c2s_upload_pve_object_state',
  full_name='c2s_upload_pve_object_state',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='list', full_name='c2s_upload_pve_object_state.list', index=0,
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
  serialized_start=510,
  serialized_end=574,
)


_S2C_UPLOAD_PVE_OBJECT_STATE = descriptor.Descriptor(
  name='s2c_upload_pve_object_state',
  full_name='s2c_upload_pve_object_state',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='code', full_name='s2c_upload_pve_object_state.code', index=0,
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
  serialized_start=576,
  serialized_end=632,
)


_P_PVE_OBJECT_STATE = descriptor.Descriptor(
  name='p_pve_object_state',
  full_name='p_pve_object_state',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='p_pve_object_state.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pos', full_name='p_pve_object_state.pos', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dir', full_name='p_pve_object_state.dir', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='create_or_destroy', full_name='p_pve_object_state.create_or_destroy', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=634,
  serialized_end=722,
)


_C2S_DOWNLOAD_PVE_STATE = descriptor.Descriptor(
  name='c2s_download_pve_state',
  full_name='c2s_download_pve_state',
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
  serialized_start=724,
  serialized_end=748,
)


_S2C_DOWNLOAD_PVE_STATE = descriptor.Descriptor(
  name='s2c_download_pve_state',
  full_name='s2c_download_pve_state',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='pos', full_name='s2c_download_pve_state.pos', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='list', full_name='s2c_download_pve_state.list', index=1,
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
  serialized_start=750,
  serialized_end=822,
)

_S2C_UPLOAD_PVE.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_C2S_PVE_BATTLE_REWARD.fields_by_name['battle'].message_type = _P_BATTLE
_S2C_PVE_BATTLE_REWARD.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_UPLOAD_PVE_PLAYER_POS.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_C2S_UPLOAD_PVE_OBJECT_STATE.fields_by_name['list'].message_type = _P_PVE_OBJECT_STATE
_S2C_UPLOAD_PVE_OBJECT_STATE.fields_by_name['code'].enum_type = error_code_pb2._E_CODE
_S2C_DOWNLOAD_PVE_STATE.fields_by_name['list'].message_type = _P_PVE_OBJECT_STATE
DESCRIPTOR.message_types_by_name['c2s_upload_pve'] = _C2S_UPLOAD_PVE
DESCRIPTOR.message_types_by_name['s2c_upload_pve'] = _S2C_UPLOAD_PVE
DESCRIPTOR.message_types_by_name['c2s_download_pve'] = _C2S_DOWNLOAD_PVE
DESCRIPTOR.message_types_by_name['s2c_download_pve'] = _S2C_DOWNLOAD_PVE
DESCRIPTOR.message_types_by_name['c2s_pve_battle_reward'] = _C2S_PVE_BATTLE_REWARD
DESCRIPTOR.message_types_by_name['s2c_pve_battle_reward'] = _S2C_PVE_BATTLE_REWARD
DESCRIPTOR.message_types_by_name['p_battle'] = _P_BATTLE
DESCRIPTOR.message_types_by_name['c2s_upload_pve_player_pos'] = _C2S_UPLOAD_PVE_PLAYER_POS
DESCRIPTOR.message_types_by_name['s2c_upload_pve_player_pos'] = _S2C_UPLOAD_PVE_PLAYER_POS
DESCRIPTOR.message_types_by_name['c2s_upload_pve_object_state'] = _C2S_UPLOAD_PVE_OBJECT_STATE
DESCRIPTOR.message_types_by_name['s2c_upload_pve_object_state'] = _S2C_UPLOAD_PVE_OBJECT_STATE
DESCRIPTOR.message_types_by_name['p_pve_object_state'] = _P_PVE_OBJECT_STATE
DESCRIPTOR.message_types_by_name['c2s_download_pve_state'] = _C2S_DOWNLOAD_PVE_STATE
DESCRIPTOR.message_types_by_name['s2c_download_pve_state'] = _S2C_DOWNLOAD_PVE_STATE

class c2s_upload_pve(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_UPLOAD_PVE
  
  # @@protoc_insertion_point(class_scope:c2s_upload_pve)

class s2c_upload_pve(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_UPLOAD_PVE
  
  # @@protoc_insertion_point(class_scope:s2c_upload_pve)

class c2s_download_pve(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_DOWNLOAD_PVE
  
  # @@protoc_insertion_point(class_scope:c2s_download_pve)

class s2c_download_pve(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_DOWNLOAD_PVE
  
  # @@protoc_insertion_point(class_scope:s2c_download_pve)

class c2s_pve_battle_reward(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_PVE_BATTLE_REWARD
  
  # @@protoc_insertion_point(class_scope:c2s_pve_battle_reward)

class s2c_pve_battle_reward(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_PVE_BATTLE_REWARD
  
  # @@protoc_insertion_point(class_scope:s2c_pve_battle_reward)

class p_battle(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _P_BATTLE
  
  # @@protoc_insertion_point(class_scope:p_battle)

class c2s_upload_pve_player_pos(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_UPLOAD_PVE_PLAYER_POS
  
  # @@protoc_insertion_point(class_scope:c2s_upload_pve_player_pos)

class s2c_upload_pve_player_pos(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_UPLOAD_PVE_PLAYER_POS
  
  # @@protoc_insertion_point(class_scope:s2c_upload_pve_player_pos)

class c2s_upload_pve_object_state(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_UPLOAD_PVE_OBJECT_STATE
  
  # @@protoc_insertion_point(class_scope:c2s_upload_pve_object_state)

class s2c_upload_pve_object_state(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_UPLOAD_PVE_OBJECT_STATE
  
  # @@protoc_insertion_point(class_scope:s2c_upload_pve_object_state)

class p_pve_object_state(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _P_PVE_OBJECT_STATE
  
  # @@protoc_insertion_point(class_scope:p_pve_object_state)

class c2s_download_pve_state(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2S_DOWNLOAD_PVE_STATE
  
  # @@protoc_insertion_point(class_scope:c2s_download_pve_state)

class s2c_download_pve_state(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2C_DOWNLOAD_PVE_STATE
  
  # @@protoc_insertion_point(class_scope:s2c_download_pve_state)

# @@protoc_insertion_point(module_scope)