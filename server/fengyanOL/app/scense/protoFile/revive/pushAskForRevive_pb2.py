# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/revive/pushAskForRevive.proto',
  package='protoFile.revive.pushAskForRevive',
  serialized_pb='\n\'protoFile/revive/pushAskForRevive.proto\x12!protoFile.revive.pushAskForRevive\"<\n\x10pushAskForRevive\x12\x12\n\nvictimerId\x18\x01 \x02(\x05\x12\x14\n\x0cvictimerName\x18\x02 \x02(\t')




_PUSHASKFORREVIVE = descriptor.Descriptor(
  name='pushAskForRevive',
  full_name='protoFile.revive.pushAskForRevive.pushAskForRevive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='victimerId', full_name='protoFile.revive.pushAskForRevive.pushAskForRevive.victimerId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='victimerName', full_name='protoFile.revive.pushAskForRevive.pushAskForRevive.victimerName', index=1,
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
  serialized_start=78,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['pushAskForRevive'] = _PUSHASKFORREVIVE

class pushAskForRevive(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PUSHASKFORREVIVE
  
  # @@protoc_insertion_point(class_scope:protoFile.revive.pushAskForRevive.pushAskForRevive)

# @@protoc_insertion_point(module_scope)