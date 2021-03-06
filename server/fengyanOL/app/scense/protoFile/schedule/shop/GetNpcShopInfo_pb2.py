# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import protoFile.itemInfo_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/shop/GetNpcShopInfo.proto',
  package='protoFile.shop.GetNpcShopInfo',
  serialized_pb='\n#protoFile/shop/GetNpcShopInfo.proto\x12\x1dprotoFile.shop.GetNpcShopInfo\x1a\x18protoFile/itemInfo.proto\"H\n\x15getNpcShopInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\r\n\x05npcId\x18\x02 \x02(\x05\x12\x14\n\x0cshopCategory\x18\x03 \x02(\x05\"p\n\x16getNpcShopInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x35\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\'.protoFile.shop.GetNpcShopInfo.ShopInfo\"e\n\x08ShopInfo\x12\x43\n\x0fpackageItemInfo\x18\x01 \x03(\x0b\x32*.protoFile.shop.GetNpcShopInfo.PackageInfo\x12\x14\n\x0cshopCategory\x18\x02 \x01(\x05\"I\n\x0bPackageInfo\x12&\n\x08itemInfo\x18\x01 \x01(\x0b\x32\x14.protoFile.ItemsInfo\x12\x12\n\nremainTime\x18\x02 \x01(\x03')




_GETNPCSHOPINFOREQUEST = descriptor.Descriptor(
  name='getNpcShopInfoRequest',
  full_name='protoFile.shop.GetNpcShopInfo.getNpcShopInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.shop.GetNpcShopInfo.getNpcShopInfoRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='npcId', full_name='protoFile.shop.GetNpcShopInfo.getNpcShopInfoRequest.npcId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='shopCategory', full_name='protoFile.shop.GetNpcShopInfo.getNpcShopInfoRequest.shopCategory', index=2,
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
  serialized_start=96,
  serialized_end=168,
)


_GETNPCSHOPINFORESPONSE = descriptor.Descriptor(
  name='getNpcShopInfoResponse',
  full_name='protoFile.shop.GetNpcShopInfo.getNpcShopInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.shop.GetNpcShopInfo.getNpcShopInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.shop.GetNpcShopInfo.getNpcShopInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.shop.GetNpcShopInfo.getNpcShopInfoResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=170,
  serialized_end=282,
)


_SHOPINFO = descriptor.Descriptor(
  name='ShopInfo',
  full_name='protoFile.shop.GetNpcShopInfo.ShopInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='packageItemInfo', full_name='protoFile.shop.GetNpcShopInfo.ShopInfo.packageItemInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='shopCategory', full_name='protoFile.shop.GetNpcShopInfo.ShopInfo.shopCategory', index=1,
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
  serialized_start=284,
  serialized_end=385,
)


_PACKAGEINFO = descriptor.Descriptor(
  name='PackageInfo',
  full_name='protoFile.shop.GetNpcShopInfo.PackageInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='itemInfo', full_name='protoFile.shop.GetNpcShopInfo.PackageInfo.itemInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='remainTime', full_name='protoFile.shop.GetNpcShopInfo.PackageInfo.remainTime', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=387,
  serialized_end=460,
)

_GETNPCSHOPINFORESPONSE.fields_by_name['data'].message_type = _SHOPINFO
_SHOPINFO.fields_by_name['packageItemInfo'].message_type = _PACKAGEINFO
_PACKAGEINFO.fields_by_name['itemInfo'].message_type = protoFile.itemInfo_pb2._ITEMSINFO
DESCRIPTOR.message_types_by_name['getNpcShopInfoRequest'] = _GETNPCSHOPINFOREQUEST
DESCRIPTOR.message_types_by_name['getNpcShopInfoResponse'] = _GETNPCSHOPINFORESPONSE
DESCRIPTOR.message_types_by_name['ShopInfo'] = _SHOPINFO
DESCRIPTOR.message_types_by_name['PackageInfo'] = _PACKAGEINFO

class getNpcShopInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETNPCSHOPINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.GetNpcShopInfo.getNpcShopInfoRequest)

class getNpcShopInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETNPCSHOPINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.GetNpcShopInfo.getNpcShopInfoResponse)

class ShopInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SHOPINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.GetNpcShopInfo.ShopInfo)

class PackageInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PACKAGEINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.shop.GetNpcShopInfo.PackageInfo)

# @@protoc_insertion_point(module_scope)
