# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enigma_event.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='enigma_event.proto',
  package='enigma.event',
  serialized_pb='\n\x12\x65nigma_event.proto\x12\x0c\x65nigma.event\"O\n\x0e\x45nigmaEnvelope\x12\x13\n\x0b\x65vent_topic\x18\x01 \x02(\t\x12\x12\n\nevent_data\x18\x02 \x02(\x0c\x12\x14\n\x0cis_heartbeat\x18\x03 \x01(\x08\"-\n\tHeartbeat\x12\x11\n\ttimestamp\x18\x01 \x02(\x04\x12\r\n\x05\x63ount\x18\x02 \x02(\x04\"\xa0\x01\n\x08Location\x12\x10\n\x08\x61\x64\x64ress1\x18\x01 \x01(\t\x12\x10\n\x08\x61\x64\x64ress2\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\x12\r\n\x05state\x18\x04 \x01(\t\x12\x0b\n\x03zip\x18\x05 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x06 \x01(\t\x12\x10\n\x08latitude\x18\x07 \x01(\x01\x12\x11\n\tlongitude\x18\x08 \x01(\x01\x12\x10\n\x08\x64ma_code\x18\t \x01(\x05\"\x82\x01\n\nSLLocation\x12(\n\x08location\x18\x01 \x01(\x0b\x32\x16.enigma.event.Location\x12\x19\n\x11sl_location_index\x18\x02 \x01(\x05\x12\x0f\n\x07sl_json\x18\x03 \x01(\t\x12\x1e\n\x16sl_adjusted_confidence\x18\x04 \x01(\x05\"k\n\x05XadId\x12\x13\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\t\x12\x12\n\nadgroup_id\x18\x02 \x01(\t\x12\x13\n\x0blocation_id\x18\x03 \x01(\t\x12\x13\n\x0b\x63reative_id\x18\x04 \x01(\t\x12\x0f\n\x07term_id\x18\x05 \x01(\t\"Y\n\x06Header\x12\x12\n\nrequest_id\x18\x01 \x02(\t\x12\x11\n\ttimestamp\x18\x02 \x02(\x12\x12\x13\n\x0blog_version\x18\x03 \x02(\t\x12\x13\n\x0br_timestamp\x18\x04 \x02(\x12\x42&\n\x0e\x63om.xad.enigmaB\x14\x45nigmaEventFramework')




_ENIGMAENVELOPE = _descriptor.Descriptor(
  name='EnigmaEnvelope',
  full_name='enigma.event.EnigmaEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_topic', full_name='enigma.event.EnigmaEnvelope.event_topic', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_data', full_name='enigma.event.EnigmaEnvelope.event_data', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_heartbeat', full_name='enigma.event.EnigmaEnvelope.is_heartbeat', index=2,
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
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=36,
  serialized_end=115,
)


_HEARTBEAT = _descriptor.Descriptor(
  name='Heartbeat',
  full_name='enigma.event.Heartbeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='enigma.event.Heartbeat.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='enigma.event.Heartbeat.count', index=1,
      number=2, type=4, cpp_type=4, label=2,
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
  serialized_start=117,
  serialized_end=162,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='enigma.event.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address1', full_name='enigma.event.Location.address1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='address2', full_name='enigma.event.Location.address2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city', full_name='enigma.event.Location.city', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='enigma.event.Location.state', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='zip', full_name='enigma.event.Location.zip', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country', full_name='enigma.event.Location.country', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='enigma.event.Location.latitude', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='enigma.event.Location.longitude', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dma_code', full_name='enigma.event.Location.dma_code', index=8,
      number=9, type=5, cpp_type=1, label=1,
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
  serialized_start=165,
  serialized_end=325,
)


_SLLOCATION = _descriptor.Descriptor(
  name='SLLocation',
  full_name='enigma.event.SLLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='enigma.event.SLLocation.location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sl_location_index', full_name='enigma.event.SLLocation.sl_location_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sl_json', full_name='enigma.event.SLLocation.sl_json', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sl_adjusted_confidence', full_name='enigma.event.SLLocation.sl_adjusted_confidence', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=328,
  serialized_end=458,
)


_XADID = _descriptor.Descriptor(
  name='XadId',
  full_name='enigma.event.XadId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='campaign_id', full_name='enigma.event.XadId.campaign_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adgroup_id', full_name='enigma.event.XadId.adgroup_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location_id', full_name='enigma.event.XadId.location_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creative_id', full_name='enigma.event.XadId.creative_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='term_id', full_name='enigma.event.XadId.term_id', index=4,
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
  serialized_start=460,
  serialized_end=567,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='enigma.event.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_id', full_name='enigma.event.Header.request_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='enigma.event.Header.timestamp', index=1,
      number=2, type=18, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='log_version', full_name='enigma.event.Header.log_version', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='r_timestamp', full_name='enigma.event.Header.r_timestamp', index=3,
      number=4, type=18, cpp_type=2, label=2,
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
  serialized_start=569,
  serialized_end=658,
)

_SLLOCATION.fields_by_name['location'].message_type = _LOCATION
DESCRIPTOR.message_types_by_name['EnigmaEnvelope'] = _ENIGMAENVELOPE
DESCRIPTOR.message_types_by_name['Heartbeat'] = _HEARTBEAT
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['SLLocation'] = _SLLOCATION
DESCRIPTOR.message_types_by_name['XadId'] = _XADID
DESCRIPTOR.message_types_by_name['Header'] = _HEADER

class EnigmaEnvelope(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ENIGMAENVELOPE

  # @@protoc_insertion_point(class_scope:enigma.event.EnigmaEnvelope)

class Heartbeat(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEARTBEAT

  # @@protoc_insertion_point(class_scope:enigma.event.Heartbeat)

class Location(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOCATION

  # @@protoc_insertion_point(class_scope:enigma.event.Location)

class SLLocation(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SLLOCATION

  # @@protoc_insertion_point(class_scope:enigma.event.SLLocation)

class XadId(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _XADID

  # @@protoc_insertion_point(class_scope:enigma.event.XadId)

class Header(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEADER

  # @@protoc_insertion_point(class_scope:enigma.event.Header)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\016com.xad.enigmaB\024EnigmaEventFramework')
# @@protoc_insertion_point(module_scope)
