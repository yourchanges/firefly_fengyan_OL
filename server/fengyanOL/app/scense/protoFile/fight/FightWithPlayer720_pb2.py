# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/fight/FightWithPlayer720.proto',
  package='proto.battle.battle720',
  serialized_pb='\n(protoFile/fight/FightWithPlayer720.proto\x12\x16proto.battle.battle720\")\n\x0e\x46ightPkRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0b\n\x03tid\x18\x02 \x02(\x05\"2\n\x0f\x46ightPkResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_FIGHTPKREQUEST = descriptor.Descriptor(
  name='FightPkRequest',
  full_name='proto.battle.battle720.FightPkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='proto.battle.battle720.FightPkRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tid', full_name='proto.battle.battle720.FightPkRequest.tid', index=1,
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
  serialized_start=68,
  serialized_end=109,
)


_FIGHTPKRESPONSE = descriptor.Descriptor(
  name='FightPkResponse',
  full_name='proto.battle.battle720.FightPkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='proto.battle.battle720.FightPkResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='proto.battle.battle720.FightPkResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=111,
  serialized_end=161,
)

DESCRIPTOR.message_types_by_name['FightPkRequest'] = _FIGHTPKREQUEST
DESCRIPTOR.message_types_by_name['FightPkResponse'] = _FIGHTPKRESPONSE

class FightPkRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIGHTPKREQUEST
  
  # @@protoc_insertion_point(class_scope:proto.battle.battle720.FightPkRequest)

class FightPkResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIGHTPKRESPONSE
  
  # @@protoc_insertion_point(class_scope:proto.battle.battle720.FightPkResponse)

# @@protoc_insertion_point(module_scope)
