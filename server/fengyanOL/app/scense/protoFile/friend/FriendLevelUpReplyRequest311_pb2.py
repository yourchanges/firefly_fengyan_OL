# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/friend/FriendLevelUpReplyRequest311.proto',
  package='protoFile.friend.FriendLevelUpReplyRequest311',
  serialized_pb='\n3protoFile/friend/FriendLevelUpReplyRequest311.proto\x12-protoFile.friend.FriendLevelUpReplyRequest311\"O\n\x19\x46riendLevelupReplyRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x11\n\tfriend_id\x18\x02 \x02(\x05\x12\x13\n\x0bhandle_type\x18\x03 \x02(\x05\"z\n\x1a\x46riendLevelupReplyResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x11\n\tfriend_id\x18\x02 \x02(\x05\x12\x13\n\x0b\x66riend_name\x18\x03 \x02(\t\x12\x13\n\x0bhandle_type\x18\x04 \x01(\x05\x12\x0f\n\x07message\x18\x05 \x01(\t')




_FRIENDLEVELUPREPLYREQUEST = descriptor.Descriptor(
  name='FriendLevelupReplyRequest',
  full_name='protoFile.friend.FriendLevelUpReplyRequest311.FriendLevelupReplyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.friend.FriendLevelUpReplyRequest311.FriendLevelupReplyRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='friend_id', full_name='protoFile.friend.FriendLevelUpReplyRequest311.FriendLevelupReplyRequest.friend_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='handle_type', full_name='protoFile.friend.FriendLevelUpReplyRequest311.FriendLevelupReplyRequest.handle_type', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=102,
  serialized_end=181,
)


_FRIENDLEVELUPREPLYRESPONSE = descriptor.Descriptor(
  name='FriendLevelupReplyResponse',
  full_name='protoFile.friend.FriendLevelUpReplyRequest311.FriendLevelupReplyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.friend.FriendLevelUpReplyRequest311.FriendLevelupReplyResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='friend_id', full_name='protoFile.friend.FriendLevelUpReplyRequest311.FriendLevelupReplyResponse.friend_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='friend_name', full_name='protoFile.friend.FriendLevelUpReplyRequest311.FriendLevelupReplyResponse.friend_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='handle_type', full_name='protoFile.friend.FriendLevelUpReplyRequest311.FriendLevelupReplyResponse.handle_type', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.friend.FriendLevelUpReplyRequest311.FriendLevelupReplyResponse.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=183,
  serialized_end=305,
)

DESCRIPTOR.message_types_by_name['FriendLevelupReplyRequest'] = _FRIENDLEVELUPREPLYREQUEST
DESCRIPTOR.message_types_by_name['FriendLevelupReplyResponse'] = _FRIENDLEVELUPREPLYRESPONSE

class FriendLevelupReplyRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIENDLEVELUPREPLYREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.friend.FriendLevelUpReplyRequest311.FriendLevelupReplyRequest)

class FriendLevelupReplyResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIENDLEVELUPREPLYRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.friend.FriendLevelUpReplyRequest311.FriendLevelupReplyResponse)

# @@protoc_insertion_point(module_scope)