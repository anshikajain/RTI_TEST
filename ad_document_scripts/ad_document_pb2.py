# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ad_document.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ad_document.proto',
  package='enigma.event',
  serialized_pb='\n\x11\x61\x64_document.proto\x12\x0c\x65nigma.event\"7\n\x10\x44ocumentEnvelope\x12\x11\n\tdoc_level\x18\x01 \x02(\r\x12\x10\n\x08\x64oc_data\x18\x02 \x02(\x0c\"=\n\x10\x43\x61mpaignDocument\x12)\n\x07\x61\x64_docs\x18\x01 \x03(\x0b\x32\x18.enigma.event.AdDocument\"\x90\x0e\n\nAdDocument\x12\x11\n\ttenant_id\x18\x01 \x01(\x04\x12\x13\n\x0b\x63\x61mpaign_id\x18\x02 \x01(\x04\x12\x12\n\nadgroup_id\x18\x03 \x01(\x04\x12\x0f\n\x07\x61\x64omain\x18\x04 \x01(\t\x12\x11\n\tcategory1\x18\x05 \x01(\t\x12\x11\n\tcategory2\x18\x06 \x01(\t\x12\x13\n\x0b\x62\x61nner_size\x18\x07 \x01(\t\x12\x15\n\rcreative_type\x18\x08 \x01(\t\x12\r\n\x05instl\x18\t \x01(\x08\x12\x16\n\x0eproximity_mode\x18\n \x01(\t\x12\x34\n\tcreatives\x18\x0b \x03(\x0b\x32!.enigma.event.AdDocument.Creative\x12?\n\x0ftarget_profiles\x18\x0c \x03(\x0b\x32&.enigma.event.AdDocument.TargetProfile\x12\x36\n\ngeotargets\x18\r \x03(\x0b\x32\".enigma.event.AdDocument.Geotarget\x12\x36\n\npublishers\x18\x0e \x03(\x0b\x32\".enigma.event.AdDocument.Publisher\x12/\n\x06status\x18\x0f \x01(\x0e\x32\x1f.enigma.event.AdDocument.Status\x12\x0b\n\x03\x64\x65l\x18\x10 \x01(\x08\x12:\n\x08rti_mode\x18\x11 \x01(\x0e\x32 .enigma.event.AdDocument.RTIMode:\x06STREAM\x12\x15\n\radv_bid_rates\x18\x12 \x01(\t\x12\x11\n\tis_secure\x18\x13 \x01(\x08\x12\x12\n\nsession_id\x18\x14 \x01(\x04\x12\x15\n\rpub_bid_rates\x18\x15 \x01(\x02\x12\x0f\n\x07kpi_ctr\x18\x16 \x01(\x02\x12\x0f\n\x07kpi_sar\x18\x17 \x01(\x02\x12\x0e\n\x06kpi_or\x18\x18 \x01(\x02\x1a\x63\n\x08\x43reative\x12\x0b\n\x03\x61pi\x18\x01 \x01(\t\x12\x0c\n\x04\x61ttr\x18\x02 \x01(\t\x12\x0c\n\x04mime\x18\x03 \x01(\t\x12\x16\n\x0evideo_duration\x18\x04 \x01(\t\x12\x16\n\x0evideo_protocol\x18\x05 \x01(\r\x1a\xb8\x04\n\rTargetProfile\x12\x46\n\x0btarget_type\x18\x01 \x01(\x0e\x32\x31.enigma.event.AdDocument.TargetProfile.TargetType\x12\x13\n\x0b\x63onstraints\x18\x02 \x01(\t\x12\x0f\n\x07\x65xclude\x18\x03 \x01(\x08\"\xb8\x03\n\nTargetType\x12\x07\n\x03\x41GE\x10\x00\x12\n\n\x06GENDER\x10\x01\x12\x0e\n\nDAYPARTING\x10\x02\x12\x0b\n\x07\x43\x41RRIER\x10\x03\x12\x06\n\x02OS\x10\x04\x12\x08\n\x04TYPE\x10\x05\x12\x11\n\rPUBLISHERTYPE\x10\x06\x12\x11\n\rPRECISELATLNG\x10\x07\x12\x0c\n\x08\x43HANNELS\x10\x08\x12\x12\n\x0e\x42LOCKEDDOMAINS\x10\t\x12\x0c\n\x08\x41UDIENCE\x10\n\x12\x10\n\x0c\x42LOCKEDNAMES\x10\x0b\x12\x0c\n\x08SEGMENTS\x10\x0c\x12\x14\n\x10PRIVACYSAFEIDFAS\x10\r\x12\x13\n\x0f\x46OOTPRINTSBRAND\x10\x0e\x12\x15\n\x11\x46OOTPRINTSSICCODE\x10\x0f\x12\x15\n\x11MOBILECOUNTRYCODE\x10\x10\x12\x15\n\x11\x44\x45VICECOUNTRYCODE\x10\x11\x12\x15\n\x11\x44\x45VICEVENDORMODEL\x10\x12\x12\x15\n\x11\x44\x45VICERELEASEYEAR\x10\x13\x12\x0f\n\x0bWIFICARRIER\x10\x14\x12\x15\n\x11REQUESTTHROTTLING\x10\x15\x12\x0f\n\x0bLOCAUDBRAND\x10\x17\x12\r\n\tLOCAUDSIC\x10\x18\x12\n\n\x06\x42\x45HAUD\x10\x1c\x1a\x8d\x02\n\tGeotarget\x12H\n\x0egeotarget_type\x18\x01 \x01(\x0e\x32\x30.enigma.event.AdDocument.Geotarget.GeotargetType\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\x12\r\n\x05state\x18\x03 \x01(\t\x12\x0b\n\x03zip\x18\x04 \x01(\t\x12\x0b\n\x03\x64ma\x18\x05 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x06 \x01(\t\x12\x0f\n\x07\x65xclude\x18\x07 \x01(\x08\"]\n\rGeotargetType\x12\x0b\n\x07\x41\x44\x44RESS\x10\x00\x12\n\n\x06LATLNG\x10\x01\x12\x07\n\x03ZIP\x10\x02\x12\x08\n\x04\x43ITY\x10\x03\x12\x07\n\x03\x44MA\x10\x04\x12\t\n\x05STATE\x10\x05\x12\x0c\n\x08NATIONAL\x10\x06\x1a!\n\tPublisher\x12\x14\n\x0cpublisher_id\x18\x01 \x01(\x04\"_\n\x06Status\x12\x0b\n\x07PENDING\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0b\n\x07\x45XPIRED\x10\x04\x12\x0b\n\x07\x44\x45LETED\x10\x05\x12\x0b\n\x07UNKNOWN\x10\x06\" \n\x07RTIMode\x12\n\n\x06STREAM\x10\x00\x12\t\n\x05\x42\x41TCH\x10\x01\x42!\n\x0e\x63om.xad.enigmaB\x0f\x41\x64\x44ocumentTopic')



_ADDOCUMENT_TARGETPROFILE_TARGETTYPE = _descriptor.EnumDescriptor(
  name='TargetType',
  full_name='enigma.event.AdDocument.TargetProfile.TargetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AGE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENDER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DAYPARTING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARRIER', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OS', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUBLISHERTYPE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRECISELATLNG', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHANNELS', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCKEDDOMAINS', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUDIENCE', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCKEDNAMES', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEGMENTS', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRIVACYSAFEIDFAS', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOOTPRINTSBRAND', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOOTPRINTSSICCODE', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOBILECOUNTRYCODE', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICECOUNTRYCODE', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICEVENDORMODEL', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICERELEASEYEAR', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WIFICARRIER', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUESTTHROTTLING', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAUDBRAND', index=22, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAUDSIC', index=23, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEHAUD', index=24, number=28,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1086,
  serialized_end=1526,
)

_ADDOCUMENT_GEOTARGET_GEOTARGETTYPE = _descriptor.EnumDescriptor(
  name='GeotargetType',
  full_name='enigma.event.AdDocument.Geotarget.GeotargetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADDRESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LATLNG', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZIP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DMA', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NATIONAL', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1705,
  serialized_end=1798,
)

_ADDOCUMENT_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='enigma.event.AdDocument.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAUSED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPIRED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1835,
  serialized_end=1930,
)

_ADDOCUMENT_RTIMODE = _descriptor.EnumDescriptor(
  name='RTIMode',
  full_name='enigma.event.AdDocument.RTIMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STREAM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATCH', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1932,
  serialized_end=1964,
)


_DOCUMENTENVELOPE = _descriptor.Descriptor(
  name='DocumentEnvelope',
  full_name='enigma.event.DocumentEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='doc_level', full_name='enigma.event.DocumentEnvelope.doc_level', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc_data', full_name='enigma.event.DocumentEnvelope.doc_data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
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
  serialized_start=35,
  serialized_end=90,
)


_CAMPAIGNDOCUMENT = _descriptor.Descriptor(
  name='CampaignDocument',
  full_name='enigma.event.CampaignDocument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ad_docs', full_name='enigma.event.CampaignDocument.ad_docs', index=0,
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
  serialized_start=92,
  serialized_end=153,
)


_ADDOCUMENT_CREATIVE = _descriptor.Descriptor(
  name='Creative',
  full_name='enigma.event.AdDocument.Creative',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api', full_name='enigma.event.AdDocument.Creative.api', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attr', full_name='enigma.event.AdDocument.Creative.attr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mime', full_name='enigma.event.AdDocument.Creative.mime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_duration', full_name='enigma.event.AdDocument.Creative.video_duration', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video_protocol', full_name='enigma.event.AdDocument.Creative.video_protocol', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=856,
  serialized_end=955,
)

_ADDOCUMENT_TARGETPROFILE = _descriptor.Descriptor(
  name='TargetProfile',
  full_name='enigma.event.AdDocument.TargetProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_type', full_name='enigma.event.AdDocument.TargetProfile.target_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='enigma.event.AdDocument.TargetProfile.constraints', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exclude', full_name='enigma.event.AdDocument.TargetProfile.exclude', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADDOCUMENT_TARGETPROFILE_TARGETTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=958,
  serialized_end=1526,
)

_ADDOCUMENT_GEOTARGET = _descriptor.Descriptor(
  name='Geotarget',
  full_name='enigma.event.AdDocument.Geotarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='geotarget_type', full_name='enigma.event.AdDocument.Geotarget.geotarget_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city', full_name='enigma.event.AdDocument.Geotarget.city', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='enigma.event.AdDocument.Geotarget.state', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zip', full_name='enigma.event.AdDocument.Geotarget.zip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dma', full_name='enigma.event.AdDocument.Geotarget.dma', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country', full_name='enigma.event.AdDocument.Geotarget.country', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exclude', full_name='enigma.event.AdDocument.Geotarget.exclude', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADDOCUMENT_GEOTARGET_GEOTARGETTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1529,
  serialized_end=1798,
)

_ADDOCUMENT_PUBLISHER = _descriptor.Descriptor(
  name='Publisher',
  full_name='enigma.event.AdDocument.Publisher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='publisher_id', full_name='enigma.event.AdDocument.Publisher.publisher_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=1800,
  serialized_end=1833,
)

_ADDOCUMENT = _descriptor.Descriptor(
  name='AdDocument',
  full_name='enigma.event.AdDocument',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tenant_id', full_name='enigma.event.AdDocument.tenant_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='campaign_id', full_name='enigma.event.AdDocument.campaign_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adgroup_id', full_name='enigma.event.AdDocument.adgroup_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adomain', full_name='enigma.event.AdDocument.adomain', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category1', full_name='enigma.event.AdDocument.category1', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category2', full_name='enigma.event.AdDocument.category2', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='banner_size', full_name='enigma.event.AdDocument.banner_size', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creative_type', full_name='enigma.event.AdDocument.creative_type', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instl', full_name='enigma.event.AdDocument.instl', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proximity_mode', full_name='enigma.event.AdDocument.proximity_mode', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creatives', full_name='enigma.event.AdDocument.creatives', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_profiles', full_name='enigma.event.AdDocument.target_profiles', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='geotargets', full_name='enigma.event.AdDocument.geotargets', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='publishers', full_name='enigma.event.AdDocument.publishers', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='enigma.event.AdDocument.status', index=14,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='del', full_name='enigma.event.AdDocument.del', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rti_mode', full_name='enigma.event.AdDocument.rti_mode', index=16,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adv_bid_rates', full_name='enigma.event.AdDocument.adv_bid_rates', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_secure', full_name='enigma.event.AdDocument.is_secure', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session_id', full_name='enigma.event.AdDocument.session_id', index=19,
      number=20, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pub_bid_rates', full_name='enigma.event.AdDocument.pub_bid_rates', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kpi_ctr', full_name='enigma.event.AdDocument.kpi_ctr', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kpi_sar', full_name='enigma.event.AdDocument.kpi_sar', index=22,
      number=23, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kpi_or', full_name='enigma.event.AdDocument.kpi_or', index=23,
      number=24, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ADDOCUMENT_CREATIVE, _ADDOCUMENT_TARGETPROFILE, _ADDOCUMENT_GEOTARGET, _ADDOCUMENT_PUBLISHER, ],
  enum_types=[
    _ADDOCUMENT_STATUS,
    _ADDOCUMENT_RTIMODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=156,
  serialized_end=1964,
)

_CAMPAIGNDOCUMENT.fields_by_name['ad_docs'].message_type = _ADDOCUMENT
_ADDOCUMENT_CREATIVE.containing_type = _ADDOCUMENT;
_ADDOCUMENT_TARGETPROFILE.fields_by_name['target_type'].enum_type = _ADDOCUMENT_TARGETPROFILE_TARGETTYPE
_ADDOCUMENT_TARGETPROFILE.containing_type = _ADDOCUMENT;
_ADDOCUMENT_TARGETPROFILE_TARGETTYPE.containing_type = _ADDOCUMENT_TARGETPROFILE;
_ADDOCUMENT_GEOTARGET.fields_by_name['geotarget_type'].enum_type = _ADDOCUMENT_GEOTARGET_GEOTARGETTYPE
_ADDOCUMENT_GEOTARGET.containing_type = _ADDOCUMENT;
_ADDOCUMENT_GEOTARGET_GEOTARGETTYPE.containing_type = _ADDOCUMENT_GEOTARGET;
_ADDOCUMENT_PUBLISHER.containing_type = _ADDOCUMENT;
_ADDOCUMENT.fields_by_name['creatives'].message_type = _ADDOCUMENT_CREATIVE
_ADDOCUMENT.fields_by_name['target_profiles'].message_type = _ADDOCUMENT_TARGETPROFILE
_ADDOCUMENT.fields_by_name['geotargets'].message_type = _ADDOCUMENT_GEOTARGET
_ADDOCUMENT.fields_by_name['publishers'].message_type = _ADDOCUMENT_PUBLISHER
_ADDOCUMENT.fields_by_name['status'].enum_type = _ADDOCUMENT_STATUS
_ADDOCUMENT.fields_by_name['rti_mode'].enum_type = _ADDOCUMENT_RTIMODE
_ADDOCUMENT_STATUS.containing_type = _ADDOCUMENT;
_ADDOCUMENT_RTIMODE.containing_type = _ADDOCUMENT;
DESCRIPTOR.message_types_by_name['DocumentEnvelope'] = _DOCUMENTENVELOPE
DESCRIPTOR.message_types_by_name['CampaignDocument'] = _CAMPAIGNDOCUMENT
DESCRIPTOR.message_types_by_name['AdDocument'] = _ADDOCUMENT

class DocumentEnvelope(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DOCUMENTENVELOPE

  # @@protoc_insertion_point(class_scope:enigma.event.DocumentEnvelope)

class CampaignDocument(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CAMPAIGNDOCUMENT

  # @@protoc_insertion_point(class_scope:enigma.event.CampaignDocument)

class AdDocument(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Creative(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ADDOCUMENT_CREATIVE

    # @@protoc_insertion_point(class_scope:enigma.event.AdDocument.Creative)

  class TargetProfile(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ADDOCUMENT_TARGETPROFILE

    # @@protoc_insertion_point(class_scope:enigma.event.AdDocument.TargetProfile)

  class Geotarget(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ADDOCUMENT_GEOTARGET

    # @@protoc_insertion_point(class_scope:enigma.event.AdDocument.Geotarget)

  class Publisher(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ADDOCUMENT_PUBLISHER

    # @@protoc_insertion_point(class_scope:enigma.event.AdDocument.Publisher)
  DESCRIPTOR = _ADDOCUMENT

  # @@protoc_insertion_point(class_scope:enigma.event.AdDocument)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\016com.xad.enigmaB\017AdDocumentTopic')
# @@protoc_insertion_point(module_scope)