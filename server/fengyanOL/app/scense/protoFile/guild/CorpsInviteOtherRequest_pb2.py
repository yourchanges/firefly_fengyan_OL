# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/guild/CorpsInviteOtherRequest.proto',
  package='protoFile.guild.CorpsInviteOtherRequest',
  serialized_pb='\n-protoFile/guild/CorpsInviteOtherRequest.proto\x12\'protoFile.guild.CorpsInviteOtherRequest\"H\n\x17UnionInviteOtherRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07otherid\x18\x02 \x01(\x05\x12\x10\n\x08otername\x18\x03 \x01(\t\"^\n\x18UnionInviteOtherResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07otherid\x18\x02 \x01(\x05\x12\x10\n\x08otername\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t')




_UNIONINVITEOTHERREQUEST = descriptor.Descriptor(
  name='UnionInviteOtherRequest',
  full_name='protoFile.guild.CorpsInviteOtherRequest.UnionInviteOtherRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.guild.CorpsInviteOtherRequest.UnionInviteOtherRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='otherid', full_name='protoFile.guild.CorpsInviteOtherRequest.UnionInviteOtherRequest.otherid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='otername', full_name='protoFile.guild.CorpsInviteOtherRequest.UnionInviteOtherRequest.otername', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=90,
  serialized_end=162,
)


_UNIONINVITEOTHERRESPONSE = descriptor.Descriptor(
  name='UnionInviteOtherResponse',
  full_name='protoFile.guild.CorpsInviteOtherRequest.UnionInviteOtherResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.guild.CorpsInviteOtherRequest.UnionInviteOtherResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='otherid', full_name='protoFile.guild.CorpsInviteOtherRequest.UnionInviteOtherResponse.otherid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='otername', full_name='protoFile.guild.CorpsInviteOtherRequest.UnionInviteOtherResponse.otername', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.guild.CorpsInviteOtherRequest.UnionInviteOtherResponse.message', index=3,
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
  serialized_start=164,
  serialized_end=258,
)

DESCRIPTOR.message_types_by_name['UnionInviteOtherRequest'] = _UNIONINVITEOTHERREQUEST
DESCRIPTOR.message_types_by_name['UnionInviteOtherResponse'] = _UNIONINVITEOTHERRESPONSE

class UnionInviteOtherRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNIONINVITEOTHERREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.CorpsInviteOtherRequest.UnionInviteOtherRequest)

class UnionInviteOtherResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _UNIONINVITEOTHERRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.CorpsInviteOtherRequest.UnionInviteOtherResponse)

# @@protoc_insertion_point(module_scope)
