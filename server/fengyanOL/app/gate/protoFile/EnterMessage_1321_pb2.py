# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/EnterMessage_1321.proto',
  package='protoFile.EnterMessage_1321',
  serialized_pb='\n!protoFile/EnterMessage_1321.proto\x12\x1bprotoFile.EnterMessage_1321\")\n\x0c\x45nterMessage\x12\x0c\n\x04type\x18\x01 \x02(\x05\x12\x0b\n\x03msg\x18\x02 \x02(\t')




_ENTERMESSAGE = descriptor.Descriptor(
  name='EnterMessage',
  full_name='protoFile.EnterMessage_1321.EnterMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='protoFile.EnterMessage_1321.EnterMessage.type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='msg', full_name='protoFile.EnterMessage_1321.EnterMessage.msg', index=1,
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
  serialized_start=66,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['EnterMessage'] = _ENTERMESSAGE

class EnterMessage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENTERMESSAGE
  
  # @@protoc_insertion_point(class_scope:protoFile.EnterMessage_1321.EnterMessage)

# @@protoc_insertion_point(module_scope)
