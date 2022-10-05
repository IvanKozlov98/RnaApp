# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rservice.proto\"\x06\n\x04Null\"*\n\x0cHumanGenetic\x12\x0b\n\x03\x44NA\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\"\x18\n\x06Health\x12\x0e\n\x06health\x18\x01 \x01(\t22\n\x0bTestService\x12#\n\tGetHealth\x12\r.HumanGenetic\x1a\x07.Healthb\x06proto3'
)




_NULL = _descriptor.Descriptor(
  name='Null',
  full_name='Null',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=23,
)


_HUMANGENETIC = _descriptor.Descriptor(
  name='HumanGenetic',
  full_name='HumanGenetic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='DNA', full_name='HumanGenetic.DNA', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='HumanGenetic.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=67,
)


_HEALTH = _descriptor.Descriptor(
  name='Health',
  full_name='Health',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='health', full_name='Health.health', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=93,
)

DESCRIPTOR.message_types_by_name['Null'] = _NULL
DESCRIPTOR.message_types_by_name['HumanGenetic'] = _HUMANGENETIC
DESCRIPTOR.message_types_by_name['Health'] = _HEALTH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Null = _reflection.GeneratedProtocolMessageType('Null', (_message.Message,), {
  'DESCRIPTOR' : _NULL,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Null)
  })
_sym_db.RegisterMessage(Null)

HumanGenetic = _reflection.GeneratedProtocolMessageType('HumanGenetic', (_message.Message,), {
  'DESCRIPTOR' : _HUMANGENETIC,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:HumanGenetic)
  })
_sym_db.RegisterMessage(HumanGenetic)

Health = _reflection.GeneratedProtocolMessageType('Health', (_message.Message,), {
  'DESCRIPTOR' : _HEALTH,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Health)
  })
_sym_db.RegisterMessage(Health)



_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=95,
  serialized_end=145,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetHealth',
    full_name='TestService.GetHealth',
    index=0,
    containing_service=None,
    input_type=_HUMANGENETIC,
    output_type=_HEALTH,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE

# @@protoc_insertion_point(module_scope)
