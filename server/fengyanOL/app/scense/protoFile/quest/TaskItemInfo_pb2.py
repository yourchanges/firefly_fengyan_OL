# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/quest/TaskItemInfo.proto',
  package='protoFile.quest',
  serialized_pb='\n\"protoFile/quest/TaskItemInfo.proto\x12\x0fprotoFile.quest\"\x81\x03\n\x0cTaskItemInfo\x12\x0f\n\x07task_id\x18\x01 \x02(\x05\x12\x11\n\ttask_type\x18\x02 \x02(\x05\x12\x12\n\ntask_state\x18\x03 \x02(\x05\x12\x18\n\x10task_price_coins\x18\x04 \x02(\x05\x12\x17\n\x0ftask_price_zuan\x18\x05 \x02(\x05\x12\x10\n\x08task_exp\x18\x06 \x02(\x05\x12\x11\n\ttask_name\x18\x07 \x02(\t\x12\x15\n\rtask_is_track\x18\x08 \x01(\x05\x12\x0f\n\x07task_lv\x18\t \x01(\x05\x12\x16\n\x0etask_type_name\x18\n \x01(\t\x12\x13\n\x0btask_ui_des\x18\x0b \x01(\t\x12\x17\n\x0ftask_runing_des\x18\x0c \x01(\t\x12\x12\n\ntask_taget\x18\r \x01(\t\x12+\n\x08task_des\x18\x0e \x03(\x0b\x32\x19.protoFile.quest.TaskTalk\x12\x32\n\x0ftask_price_item\x18\x0f \x03(\x0b\x32\x19.protoFile.quest.ItemInfo\".\n\x08TaskTalk\x12\x10\n\x08roleType\x18\x01 \x01(\t\x12\x10\n\x08task_des\x18\x02 \x01(\t\")\n\x08ItemInfo\x12\x0e\n\x06itemId\x18\x01 \x01(\x05\x12\r\n\x05stack\x18\x02 \x01(\x05*M\n\tTaskState\x12\t\n\x05\x45RROR\x10\x00\x12\x0f\n\x0b\x41\x43\x43\x45RT_ABLE\x10\x01\x12\n\n\x06RUNING\x10\x02\x12\x0c\n\x08\x43OMPLETE\x10\x03\x12\n\n\x06\x45XCUTE\x10\x04*8\n\x08TaskType\x12\x13\n\x0fTASK_TYPE_ERROR\x10\x00\x12\x08\n\x04MAIN\x10\x01\x12\r\n\tExtension\x10\x02')

_TASKSTATE = descriptor.EnumDescriptor(
  name='TaskState',
  full_name='protoFile.quest.TaskState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='ERROR', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ACCERT_ABLE', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='RUNING', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='COMPLETE', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXCUTE', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=534,
  serialized_end=611,
)


_TASKTYPE = descriptor.EnumDescriptor(
  name='TaskType',
  full_name='protoFile.quest.TaskType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='TASK_TYPE_ERROR', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MAIN', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Extension', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=613,
  serialized_end=669,
)


ERROR = 0
ACCERT_ABLE = 1
RUNING = 2
COMPLETE = 3
EXCUTE = 4
TASK_TYPE_ERROR = 0
MAIN = 1
Extension = 2



_TASKITEMINFO = descriptor.Descriptor(
  name='TaskItemInfo',
  full_name='protoFile.quest.TaskItemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='task_id', full_name='protoFile.quest.TaskItemInfo.task_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_type', full_name='protoFile.quest.TaskItemInfo.task_type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_state', full_name='protoFile.quest.TaskItemInfo.task_state', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_price_coins', full_name='protoFile.quest.TaskItemInfo.task_price_coins', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_price_zuan', full_name='protoFile.quest.TaskItemInfo.task_price_zuan', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_exp', full_name='protoFile.quest.TaskItemInfo.task_exp', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_name', full_name='protoFile.quest.TaskItemInfo.task_name', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_is_track', full_name='protoFile.quest.TaskItemInfo.task_is_track', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_lv', full_name='protoFile.quest.TaskItemInfo.task_lv', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_type_name', full_name='protoFile.quest.TaskItemInfo.task_type_name', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_ui_des', full_name='protoFile.quest.TaskItemInfo.task_ui_des', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_runing_des', full_name='protoFile.quest.TaskItemInfo.task_runing_des', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_taget', full_name='protoFile.quest.TaskItemInfo.task_taget', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_des', full_name='protoFile.quest.TaskItemInfo.task_des', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_price_item', full_name='protoFile.quest.TaskItemInfo.task_price_item', index=14,
      number=15, type=11, cpp_type=10, label=3,
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
  serialized_start=56,
  serialized_end=441,
)


_TASKTALK = descriptor.Descriptor(
  name='TaskTalk',
  full_name='protoFile.quest.TaskTalk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roleType', full_name='protoFile.quest.TaskTalk.roleType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='task_des', full_name='protoFile.quest.TaskTalk.task_des', index=1,
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
  serialized_start=443,
  serialized_end=489,
)


_ITEMINFO = descriptor.Descriptor(
  name='ItemInfo',
  full_name='protoFile.quest.ItemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='itemId', full_name='protoFile.quest.ItemInfo.itemId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stack', full_name='protoFile.quest.ItemInfo.stack', index=1,
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
  serialized_start=491,
  serialized_end=532,
)

_TASKITEMINFO.fields_by_name['task_des'].message_type = _TASKTALK
_TASKITEMINFO.fields_by_name['task_price_item'].message_type = _ITEMINFO
DESCRIPTOR.message_types_by_name['TaskItemInfo'] = _TASKITEMINFO
DESCRIPTOR.message_types_by_name['TaskTalk'] = _TASKTALK
DESCRIPTOR.message_types_by_name['ItemInfo'] = _ITEMINFO

class TaskItemInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKITEMINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.TaskItemInfo)

class TaskTalk(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TASKTALK
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.TaskTalk)

class ItemInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.ItemInfo)

# @@protoc_insertion_point(module_scope)