# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trade_agent_protobuf/src/trade_agent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*trade_agent_protobuf/src/trade_agent.proto\x12\x14trade_agent_protobuf\"B\n\rStockResponse\x12\x31\n\x05stock\x18\x01 \x03(\x0b\x32\".trade_agent_protobuf.StockMessage\"\x89\x01\n\x0cStockMessage\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x11\n\treference\x18\x05 \x01(\x01\x12\x13\n\x0bupdate_date\x18\x06 \x01(\t\x12\x11\n\tday_trade\x18\x07 \x01(\t\"G\n\x10SnapshotResponse\x12\x33\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32%.trade_agent_protobuf.SnapshotMessage\"\xab\x03\n\x0fSnapshotMessage\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x10\n\x08\x65xchange\x18\x03 \x01(\t\x12\x0c\n\x04open\x18\x04 \x01(\x01\x12\x0c\n\x04high\x18\x05 \x01(\x01\x12\x0b\n\x03low\x18\x06 \x01(\x01\x12\r\n\x05\x63lose\x18\x07 \x01(\x01\x12\x11\n\ttick_type\x18\x08 \x01(\t\x12\x14\n\x0c\x63hange_price\x18\t \x01(\x01\x12\x13\n\x0b\x63hange_rate\x18\n \x01(\x01\x12\x13\n\x0b\x63hange_type\x18\x0b \x01(\t\x12\x15\n\raverage_price\x18\x0c \x01(\x01\x12\x0e\n\x06volume\x18\r \x01(\x03\x12\x14\n\x0ctotal_volume\x18\x0e \x01(\x03\x12\x0e\n\x06\x61mount\x18\x0f \x01(\x03\x12\x14\n\x0ctotal_amount\x18\x10 \x01(\x03\x12\x18\n\x10yesterday_volume\x18\x11 \x01(\x01\x12\x11\n\tbuy_price\x18\x12 \x01(\x01\x12\x12\n\nbuy_volume\x18\x13 \x01(\x01\x12\x12\n\nsell_price\x18\x14 \x01(\x01\x12\x13\n\x0bsell_volume\x18\x15 \x01(\x03\x12\x14\n\x0cvolume_ratio\x18\x16 \x01(\x01\"n\n\x13HistoryTickResponse\x12\x11\n\tstock_num\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x36\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32(.trade_agent_protobuf.HistoryTickMessage\"\xa0\x01\n\x12HistoryTickMessage\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\r\n\x05\x63lose\x18\x02 \x01(\x01\x12\x0e\n\x06volume\x18\x03 \x01(\x03\x12\x11\n\tbid_price\x18\x04 \x01(\x01\x12\x12\n\nbid_volume\x18\x05 \x01(\x03\x12\x11\n\task_price\x18\x06 \x01(\x01\x12\x12\n\nask_volume\x18\x07 \x01(\x03\x12\x11\n\ttick_type\x18\x08 \x01(\x03\"x\n\x0cKbarResponse\x12\x11\n\tstock_num\x18\x01 \x01(\t\x12\x12\n\nstart_date\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x03 \x01(\t\x12/\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32!.trade_agent_protobuf.KbarMessage\"a\n\x0bKbarMessage\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\r\n\x05\x43lose\x18\x02 \x01(\x01\x12\x0c\n\x04Open\x18\x03 \x01(\x01\x12\x0c\n\x04High\x18\x04 \x01(\x01\x12\x0b\n\x03Low\x18\x05 \x01(\x01\x12\x0e\n\x06Volume\x18\x06 \x01(\x03\"I\n\x11LastCountResponse\x12\x34\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32&.trade_agent_protobuf.LastCountMessage\"K\n\x10LastCountMessage\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x03\x12\r\n\x05\x63lose\x18\x04 \x01(\x01\"K\n\x12VolumeRankResponse\x12\x35\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\'.trade_agent_protobuf.VolumeRankMessage\"\x89\x04\n\x11VolumeRankMessage\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\n\n\x02ts\x18\x04 \x01(\x03\x12\x0c\n\x04open\x18\x05 \x01(\x01\x12\x0c\n\x04high\x18\x06 \x01(\x01\x12\x0b\n\x03low\x18\x07 \x01(\x01\x12\r\n\x05\x63lose\x18\x08 \x01(\x01\x12\x13\n\x0bprice_range\x18\t \x01(\x01\x12\x11\n\ttick_type\x18\n \x01(\x03\x12\x14\n\x0c\x63hange_price\x18\x0b \x01(\x01\x12\x13\n\x0b\x63hange_type\x18\x0c \x01(\x03\x12\x15\n\raverage_price\x18\r \x01(\x01\x12\x0e\n\x06volume\x18\x0e \x01(\x03\x12\x14\n\x0ctotal_volume\x18\x0f \x01(\x03\x12\x0e\n\x06\x61mount\x18\x10 \x01(\x03\x12\x14\n\x0ctotal_amount\x18\x11 \x01(\x03\x12\x18\n\x10yesterday_volume\x18\x12 \x01(\x03\x12\x14\n\x0cvolume_ratio\x18\x13 \x01(\x01\x12\x11\n\tbuy_price\x18\x14 \x01(\x01\x12\x12\n\nbuy_volume\x18\x15 \x01(\x03\x12\x12\n\nsell_price\x18\x16 \x01(\x01\x12\x13\n\x0bsell_volume\x18\x17 \x01(\x03\x12\x12\n\nbid_orders\x18\x18 \x01(\x03\x12\x13\n\x0b\x62id_volumes\x18\x19 \x01(\x03\x12\x12\n\nask_orders\x18\x1a \x01(\x03\x12\x13\n\x0b\x61sk_volumes\x18\x1b \x01(\x03\"[\n\x1aOrderStatusHistoryResponse\x12=\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32/.trade_agent_protobuf.OrderStatusHistoryMessage\"\x90\x01\n\x19OrderStatusHistoryMessage\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\x01\x12\x10\n\x08quantity\x18\x05 \x01(\x03\x12\x10\n\x08order_id\x18\x06 \x01(\t\x12\x12\n\norder_time\x18\x07 \x01(\t\"a\n\x14RealTimeTickResponse\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12\x37\n\x04tick\x18\x02 \x01(\x0b\x32).trade_agent_protobuf.RealTimeTickMessage\"\xa9\x03\n\x13RealTimeTickMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x0c\n\x04open\x18\x03 \x01(\x01\x12\x11\n\tavg_price\x18\x04 \x01(\x01\x12\r\n\x05\x63lose\x18\x05 \x01(\x01\x12\x0c\n\x04high\x18\x06 \x01(\x01\x12\x0b\n\x03low\x18\x07 \x01(\x01\x12\x0e\n\x06\x61mount\x18\x08 \x01(\x01\x12\x14\n\x0ctotal_amount\x18\t \x01(\x01\x12\x0e\n\x06volume\x18\n \x01(\x03\x12\x14\n\x0ctotal_volume\x18\x0b \x01(\x03\x12\x11\n\ttick_type\x18\x0c \x01(\x03\x12\x10\n\x08\x63hg_type\x18\r \x01(\x03\x12\x11\n\tprice_chg\x18\x0e \x01(\x01\x12\x0f\n\x07pct_chg\x18\x0f \x01(\x01\x12\x1a\n\x12\x62id_side_total_vol\x18\x10 \x01(\x03\x12\x1a\n\x12\x61sk_side_total_vol\x18\x11 \x01(\x03\x12\x1a\n\x12\x62id_side_total_cnt\x18\x12 \x01(\x03\x12\x1a\n\x12\x61sk_side_total_cnt\x18\x13 \x01(\x03\x12\x0f\n\x07suspend\x18\x14 \x01(\x03\x12\x10\n\x08simtrade\x18\x15 \x01(\x03\"h\n\x16RealTimeBidAskResponse\x12\x10\n\x08\x65xchange\x18\x01 \x01(\t\x12<\n\x07\x62id_ask\x18\x02 \x01(\x0b\x32+.trade_agent_protobuf.RealTimeBidAskMessage\"\xd5\x01\n\x15RealTimeBidAskMessage\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x11\n\tbid_price\x18\x03 \x03(\x01\x12\x12\n\nbid_volume\x18\x04 \x03(\x03\x12\x14\n\x0c\x64iff_bid_vol\x18\x05 \x03(\x03\x12\x11\n\task_price\x18\x06 \x03(\x01\x12\x12\n\nask_volume\x18\x07 \x03(\x03\x12\x14\n\x0c\x64iff_ask_vol\x18\x08 \x03(\x03\x12\x0f\n\x07suspend\x18\t \x01(\x03\x12\x10\n\x08simtrade\x18\n \x01(\x03\"S\n\rEventResponse\x12\x11\n\tresp_code\x18\x01 \x01(\x03\x12\x12\n\nevent_code\x18\x02 \x01(\x03\x12\x0c\n\x04info\x18\x03 \x01(\t\x12\r\n\x05\x65vent\x18\x04 \x01(\t\"M\n\x13TradeRecordResponse\x12\x36\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32(.trade_agent_protobuf.TradeRecordMessage\"\x83\x01\n\x12TradeRecordMessage\x12\x10\n\x08quantity\x18\x01 \x01(\x03\x12\r\n\x05price\x18\x02 \x01(\x01\x12\x0e\n\x06\x61\x63tion\x18\x03 \x01(\t\x12\x0c\n\x04\x63ode\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x12\n\norder_time\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\tB\x08Z\x06pkg/pbb\x06proto3')



_STOCKRESPONSE = DESCRIPTOR.message_types_by_name['StockResponse']
_STOCKMESSAGE = DESCRIPTOR.message_types_by_name['StockMessage']
_SNAPSHOTRESPONSE = DESCRIPTOR.message_types_by_name['SnapshotResponse']
_SNAPSHOTMESSAGE = DESCRIPTOR.message_types_by_name['SnapshotMessage']
_HISTORYTICKRESPONSE = DESCRIPTOR.message_types_by_name['HistoryTickResponse']
_HISTORYTICKMESSAGE = DESCRIPTOR.message_types_by_name['HistoryTickMessage']
_KBARRESPONSE = DESCRIPTOR.message_types_by_name['KbarResponse']
_KBARMESSAGE = DESCRIPTOR.message_types_by_name['KbarMessage']
_LASTCOUNTRESPONSE = DESCRIPTOR.message_types_by_name['LastCountResponse']
_LASTCOUNTMESSAGE = DESCRIPTOR.message_types_by_name['LastCountMessage']
_VOLUMERANKRESPONSE = DESCRIPTOR.message_types_by_name['VolumeRankResponse']
_VOLUMERANKMESSAGE = DESCRIPTOR.message_types_by_name['VolumeRankMessage']
_ORDERSTATUSHISTORYRESPONSE = DESCRIPTOR.message_types_by_name['OrderStatusHistoryResponse']
_ORDERSTATUSHISTORYMESSAGE = DESCRIPTOR.message_types_by_name['OrderStatusHistoryMessage']
_REALTIMETICKRESPONSE = DESCRIPTOR.message_types_by_name['RealTimeTickResponse']
_REALTIMETICKMESSAGE = DESCRIPTOR.message_types_by_name['RealTimeTickMessage']
_REALTIMEBIDASKRESPONSE = DESCRIPTOR.message_types_by_name['RealTimeBidAskResponse']
_REALTIMEBIDASKMESSAGE = DESCRIPTOR.message_types_by_name['RealTimeBidAskMessage']
_EVENTRESPONSE = DESCRIPTOR.message_types_by_name['EventResponse']
_TRADERECORDRESPONSE = DESCRIPTOR.message_types_by_name['TradeRecordResponse']
_TRADERECORDMESSAGE = DESCRIPTOR.message_types_by_name['TradeRecordMessage']
StockResponse = _reflection.GeneratedProtocolMessageType('StockResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOCKRESPONSE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.StockResponse)
  })
_sym_db.RegisterMessage(StockResponse)

StockMessage = _reflection.GeneratedProtocolMessageType('StockMessage', (_message.Message,), {
  'DESCRIPTOR' : _STOCKMESSAGE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.StockMessage)
  })
_sym_db.RegisterMessage(StockMessage)

SnapshotResponse = _reflection.GeneratedProtocolMessageType('SnapshotResponse', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTRESPONSE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.SnapshotResponse)
  })
_sym_db.RegisterMessage(SnapshotResponse)

SnapshotMessage = _reflection.GeneratedProtocolMessageType('SnapshotMessage', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTMESSAGE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.SnapshotMessage)
  })
_sym_db.RegisterMessage(SnapshotMessage)

HistoryTickResponse = _reflection.GeneratedProtocolMessageType('HistoryTickResponse', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYTICKRESPONSE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.HistoryTickResponse)
  })
_sym_db.RegisterMessage(HistoryTickResponse)

HistoryTickMessage = _reflection.GeneratedProtocolMessageType('HistoryTickMessage', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYTICKMESSAGE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.HistoryTickMessage)
  })
_sym_db.RegisterMessage(HistoryTickMessage)

KbarResponse = _reflection.GeneratedProtocolMessageType('KbarResponse', (_message.Message,), {
  'DESCRIPTOR' : _KBARRESPONSE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.KbarResponse)
  })
_sym_db.RegisterMessage(KbarResponse)

KbarMessage = _reflection.GeneratedProtocolMessageType('KbarMessage', (_message.Message,), {
  'DESCRIPTOR' : _KBARMESSAGE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.KbarMessage)
  })
_sym_db.RegisterMessage(KbarMessage)

LastCountResponse = _reflection.GeneratedProtocolMessageType('LastCountResponse', (_message.Message,), {
  'DESCRIPTOR' : _LASTCOUNTRESPONSE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.LastCountResponse)
  })
_sym_db.RegisterMessage(LastCountResponse)

LastCountMessage = _reflection.GeneratedProtocolMessageType('LastCountMessage', (_message.Message,), {
  'DESCRIPTOR' : _LASTCOUNTMESSAGE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.LastCountMessage)
  })
_sym_db.RegisterMessage(LastCountMessage)

VolumeRankResponse = _reflection.GeneratedProtocolMessageType('VolumeRankResponse', (_message.Message,), {
  'DESCRIPTOR' : _VOLUMERANKRESPONSE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.VolumeRankResponse)
  })
_sym_db.RegisterMessage(VolumeRankResponse)

VolumeRankMessage = _reflection.GeneratedProtocolMessageType('VolumeRankMessage', (_message.Message,), {
  'DESCRIPTOR' : _VOLUMERANKMESSAGE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.VolumeRankMessage)
  })
_sym_db.RegisterMessage(VolumeRankMessage)

OrderStatusHistoryResponse = _reflection.GeneratedProtocolMessageType('OrderStatusHistoryResponse', (_message.Message,), {
  'DESCRIPTOR' : _ORDERSTATUSHISTORYRESPONSE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.OrderStatusHistoryResponse)
  })
_sym_db.RegisterMessage(OrderStatusHistoryResponse)

OrderStatusHistoryMessage = _reflection.GeneratedProtocolMessageType('OrderStatusHistoryMessage', (_message.Message,), {
  'DESCRIPTOR' : _ORDERSTATUSHISTORYMESSAGE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.OrderStatusHistoryMessage)
  })
_sym_db.RegisterMessage(OrderStatusHistoryMessage)

RealTimeTickResponse = _reflection.GeneratedProtocolMessageType('RealTimeTickResponse', (_message.Message,), {
  'DESCRIPTOR' : _REALTIMETICKRESPONSE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.RealTimeTickResponse)
  })
_sym_db.RegisterMessage(RealTimeTickResponse)

RealTimeTickMessage = _reflection.GeneratedProtocolMessageType('RealTimeTickMessage', (_message.Message,), {
  'DESCRIPTOR' : _REALTIMETICKMESSAGE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.RealTimeTickMessage)
  })
_sym_db.RegisterMessage(RealTimeTickMessage)

RealTimeBidAskResponse = _reflection.GeneratedProtocolMessageType('RealTimeBidAskResponse', (_message.Message,), {
  'DESCRIPTOR' : _REALTIMEBIDASKRESPONSE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.RealTimeBidAskResponse)
  })
_sym_db.RegisterMessage(RealTimeBidAskResponse)

RealTimeBidAskMessage = _reflection.GeneratedProtocolMessageType('RealTimeBidAskMessage', (_message.Message,), {
  'DESCRIPTOR' : _REALTIMEBIDASKMESSAGE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.RealTimeBidAskMessage)
  })
_sym_db.RegisterMessage(RealTimeBidAskMessage)

EventResponse = _reflection.GeneratedProtocolMessageType('EventResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVENTRESPONSE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.EventResponse)
  })
_sym_db.RegisterMessage(EventResponse)

TradeRecordResponse = _reflection.GeneratedProtocolMessageType('TradeRecordResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRADERECORDRESPONSE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.TradeRecordResponse)
  })
_sym_db.RegisterMessage(TradeRecordResponse)

TradeRecordMessage = _reflection.GeneratedProtocolMessageType('TradeRecordMessage', (_message.Message,), {
  'DESCRIPTOR' : _TRADERECORDMESSAGE,
  '__module__' : 'trade_agent_protobuf.src.trade_agent_pb2'
  # @@protoc_insertion_point(class_scope:trade_agent_protobuf.TradeRecordMessage)
  })
_sym_db.RegisterMessage(TradeRecordMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\006pkg/pb'
  _STOCKRESPONSE._serialized_start=68
  _STOCKRESPONSE._serialized_end=134
  _STOCKMESSAGE._serialized_start=137
  _STOCKMESSAGE._serialized_end=274
  _SNAPSHOTRESPONSE._serialized_start=276
  _SNAPSHOTRESPONSE._serialized_end=347
  _SNAPSHOTMESSAGE._serialized_start=350
  _SNAPSHOTMESSAGE._serialized_end=777
  _HISTORYTICKRESPONSE._serialized_start=779
  _HISTORYTICKRESPONSE._serialized_end=889
  _HISTORYTICKMESSAGE._serialized_start=892
  _HISTORYTICKMESSAGE._serialized_end=1052
  _KBARRESPONSE._serialized_start=1054
  _KBARRESPONSE._serialized_end=1174
  _KBARMESSAGE._serialized_start=1176
  _KBARMESSAGE._serialized_end=1273
  _LASTCOUNTRESPONSE._serialized_start=1275
  _LASTCOUNTRESPONSE._serialized_end=1348
  _LASTCOUNTMESSAGE._serialized_start=1350
  _LASTCOUNTMESSAGE._serialized_end=1425
  _VOLUMERANKRESPONSE._serialized_start=1427
  _VOLUMERANKRESPONSE._serialized_end=1502
  _VOLUMERANKMESSAGE._serialized_start=1505
  _VOLUMERANKMESSAGE._serialized_end=2026
  _ORDERSTATUSHISTORYRESPONSE._serialized_start=2028
  _ORDERSTATUSHISTORYRESPONSE._serialized_end=2119
  _ORDERSTATUSHISTORYMESSAGE._serialized_start=2122
  _ORDERSTATUSHISTORYMESSAGE._serialized_end=2266
  _REALTIMETICKRESPONSE._serialized_start=2268
  _REALTIMETICKRESPONSE._serialized_end=2365
  _REALTIMETICKMESSAGE._serialized_start=2368
  _REALTIMETICKMESSAGE._serialized_end=2793
  _REALTIMEBIDASKRESPONSE._serialized_start=2795
  _REALTIMEBIDASKRESPONSE._serialized_end=2899
  _REALTIMEBIDASKMESSAGE._serialized_start=2902
  _REALTIMEBIDASKMESSAGE._serialized_end=3115
  _EVENTRESPONSE._serialized_start=3117
  _EVENTRESPONSE._serialized_end=3200
  _TRADERECORDRESPONSE._serialized_start=3202
  _TRADERECORDRESPONSE._serialized_end=3279
  _TRADERECORDMESSAGE._serialized_start=3282
  _TRADERECORDMESSAGE._serialized_end=3413
# @@protoc_insertion_point(module_scope)
