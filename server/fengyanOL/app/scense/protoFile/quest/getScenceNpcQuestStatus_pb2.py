# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/quest/getScenceNpcQuestStatus.proto',
  package='protoFile.quest.getScenceNpcQuestStatus',
  serialized_pb='\n-protoFile/quest/getScenceNpcQuestStatus.proto\x12\'protoFile.quest.getScenceNpcQuestStatus\",\n\x1egetScenceNpcQuestStatusRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"v\n\x1fgetScenceNpcQuestStatusResponse\x12S\n\x12NPCQuestStatusList\x18\x01 \x03(\x0b\x32\x37.protoFile.quest.getScenceNpcQuestStatus.NPCQuestStatus\".\n\x0eNPCQuestStatus\x12\r\n\x05npcID\x18\x01 \x01(\x05\x12\r\n\x05statu\x18\x02 \x01(\x05')




_GETSCENCENPCQUESTSTATUSREQUEST = descriptor.Descriptor(
  name='getScenceNpcQuestStatusRequest',
  full_name='protoFile.quest.getScenceNpcQuestStatus.getScenceNpcQuestStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.quest.getScenceNpcQuestStatus.getScenceNpcQuestStatusRequest.id', index=0,
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
  serialized_start=90,
  serialized_end=134,
)


_GETSCENCENPCQUESTSTATUSRESPONSE = descriptor.Descriptor(
  name='getScenceNpcQuestStatusResponse',
  full_name='protoFile.quest.getScenceNpcQuestStatus.getScenceNpcQuestStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='NPCQuestStatusList', full_name='protoFile.quest.getScenceNpcQuestStatus.getScenceNpcQuestStatusResponse.NPCQuestStatusList', index=0,
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
  serialized_start=136,
  serialized_end=254,
)


_NPCQUESTSTATUS = descriptor.Descriptor(
  name='NPCQuestStatus',
  full_name='protoFile.quest.getScenceNpcQuestStatus.NPCQuestStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='npcID', full_name='protoFile.quest.getScenceNpcQuestStatus.NPCQuestStatus.npcID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='statu', full_name='protoFile.quest.getScenceNpcQuestStatus.NPCQuestStatus.statu', index=1,
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
  serialized_start=256,
  serialized_end=302,
)

_GETSCENCENPCQUESTSTATUSRESPONSE.fields_by_name['NPCQuestStatusList'].message_type = _NPCQUESTSTATUS
DESCRIPTOR.message_types_by_name['getScenceNpcQuestStatusRequest'] = _GETSCENCENPCQUESTSTATUSREQUEST
DESCRIPTOR.message_types_by_name['getScenceNpcQuestStatusResponse'] = _GETSCENCENPCQUESTSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['NPCQuestStatus'] = _NPCQUESTSTATUS

class getScenceNpcQuestStatusRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSCENCENPCQUESTSTATUSREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.getScenceNpcQuestStatus.getScenceNpcQuestStatusRequest)

class getScenceNpcQuestStatusResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETSCENCENPCQUESTSTATUSRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.getScenceNpcQuestStatus.getScenceNpcQuestStatusResponse)

class NPCQuestStatus(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NPCQUESTSTATUS
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.getScenceNpcQuestStatus.NPCQuestStatus)

# @@protoc_insertion_point(module_scope)