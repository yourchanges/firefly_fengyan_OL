# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/guild/LeaveCorps.proto',
  package='protoFile.guild.LeaveCorps',
  serialized_pb='\n protoFile/guild/LeaveCorps.proto\x12\x1aprotoFile.guild.LeaveCorps\"\x1f\n\x11LeaveCorpsRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"5\n\x12LeaveCorpsResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_LEAVECORPSREQUEST = descriptor.Descriptor(
  name='LeaveCorpsRequest',
  full_name='protoFile.guild.LeaveCorps.LeaveCorpsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.guild.LeaveCorps.LeaveCorpsRequest.id', index=0,
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
  serialized_start=64,
  serialized_end=95,
)


_LEAVECORPSRESPONSE = descriptor.Descriptor(
  name='LeaveCorpsResponse',
  full_name='protoFile.guild.LeaveCorps.LeaveCorpsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.guild.LeaveCorps.LeaveCorpsResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.guild.LeaveCorps.LeaveCorpsResponse.message', index=1,
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
  serialized_start=97,
  serialized_end=150,
)

DESCRIPTOR.message_types_by_name['LeaveCorpsRequest'] = _LEAVECORPSREQUEST
DESCRIPTOR.message_types_by_name['LeaveCorpsResponse'] = _LEAVECORPSRESPONSE

class LeaveCorpsRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEAVECORPSREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.LeaveCorps.LeaveCorpsRequest)

class LeaveCorpsResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LEAVECORPSRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.LeaveCorps.LeaveCorpsResponse)

# @@protoc_insertion_point(module_scope)
