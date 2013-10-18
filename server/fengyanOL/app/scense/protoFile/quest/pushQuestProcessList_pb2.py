# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/quest/pushQuestProcessList.proto',
  package='protoFile.quest.pushQuestProcessList',
  serialized_pb='\n*protoFile/quest/pushQuestProcessList.proto\x12$protoFile.quest.pushQuestProcessList\"\x96\x01\n\x14pushQuestProcessList\x12L\n\x10questprocesslist\x18\x01 \x03(\x0b\x32\x32.protoFile.quest.pushQuestProcessList.QuestProcess\x12\x18\n\x10\x63irculatingCount\x18\x02 \x01(\x05\x12\x16\n\x0e\x63irculatingNum\x18\x03 \x01(\x05\"\xba\x01\n\x0cQuestProcess\x12\x0e\n\x06taskId\x18\x01 \x01(\x05\x12\x10\n\x08taskname\x18\x02 \x01(\t\x12\x13\n\x0bhasFinished\x18\x03 \x01(\x05\x12J\n\x0fprocessinfolist\x18\x04 \x03(\x0b\x32\x31.protoFile.quest.pushQuestProcessList.ProcessInfo\x12\x10\n\x08tasktype\x18\x05 \x01(\x05\x12\x15\n\rfinishedNpcId\x18\x06 \x01(\x05\"n\n\x0bProcessInfo\x12\x13\n\x0bquestGoalId\x18\x01 \x01(\x05\x12\x12\n\nrequireNum\x18\x02 \x01(\x05\x12\x12\n\nachieveNum\x18\x03 \x01(\x05\x12\x11\n\ttrackDesc\x18\x04 \x01(\t\x12\x0f\n\x07trackID\x18\x05 \x01(\x05')




_PUSHQUESTPROCESSLIST = descriptor.Descriptor(
  name='pushQuestProcessList',
  full_name='protoFile.quest.pushQuestProcessList.pushQuestProcessList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='questprocesslist', full_name='protoFile.quest.pushQuestProcessList.pushQuestProcessList.questprocesslist', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='circulatingCount', full_name='protoFile.quest.pushQuestProcessList.pushQuestProcessList.circulatingCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='circulatingNum', full_name='protoFile.quest.pushQuestProcessList.pushQuestProcessList.circulatingNum', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=85,
  serialized_end=235,
)


_QUESTPROCESS = descriptor.Descriptor(
  name='QuestProcess',
  full_name='protoFile.quest.pushQuestProcessList.QuestProcess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='taskId', full_name='protoFile.quest.pushQuestProcessList.QuestProcess.taskId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='taskname', full_name='protoFile.quest.pushQuestProcessList.QuestProcess.taskname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hasFinished', full_name='protoFile.quest.pushQuestProcessList.QuestProcess.hasFinished', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='processinfolist', full_name='protoFile.quest.pushQuestProcessList.QuestProcess.processinfolist', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tasktype', full_name='protoFile.quest.pushQuestProcessList.QuestProcess.tasktype', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='finishedNpcId', full_name='protoFile.quest.pushQuestProcessList.QuestProcess.finishedNpcId', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=238,
  serialized_end=424,
)


_PROCESSINFO = descriptor.Descriptor(
  name='ProcessInfo',
  full_name='protoFile.quest.pushQuestProcessList.ProcessInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='questGoalId', full_name='protoFile.quest.pushQuestProcessList.ProcessInfo.questGoalId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='requireNum', full_name='protoFile.quest.pushQuestProcessList.ProcessInfo.requireNum', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='achieveNum', full_name='protoFile.quest.pushQuestProcessList.ProcessInfo.achieveNum', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='trackDesc', full_name='protoFile.quest.pushQuestProcessList.ProcessInfo.trackDesc', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='trackID', full_name='protoFile.quest.pushQuestProcessList.ProcessInfo.trackID', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=426,
  serialized_end=536,
)

_PUSHQUESTPROCESSLIST.fields_by_name['questprocesslist'].message_type = _QUESTPROCESS
_QUESTPROCESS.fields_by_name['processinfolist'].message_type = _PROCESSINFO
DESCRIPTOR.message_types_by_name['pushQuestProcessList'] = _PUSHQUESTPROCESSLIST
DESCRIPTOR.message_types_by_name['QuestProcess'] = _QUESTPROCESS
DESCRIPTOR.message_types_by_name['ProcessInfo'] = _PROCESSINFO

class pushQuestProcessList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PUSHQUESTPROCESSLIST
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.pushQuestProcessList.pushQuestProcessList)

class QuestProcess(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUESTPROCESS
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.pushQuestProcessList.QuestProcess)

class ProcessInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROCESSINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.pushQuestProcessList.ProcessInfo)

# @@protoc_insertion_point(module_scope)