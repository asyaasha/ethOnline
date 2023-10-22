# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023 zarathustra
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Serialization module for sql_crud protocol."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,redefined-builtin
from typing import Any, Dict, cast

from aea.mail.base_pb2 import DialogueMessage
from aea.mail.base_pb2 import Message as ProtobufMessage
from aea.protocols.base import Message, Serializer

from packages.zarathustra.protocols.sql_crud import sql_crud_pb2
from packages.zarathustra.protocols.sql_crud.custom_types import (
    ErrorCode,
    LabeledRecords,
    UpdateValues,
)
from packages.zarathustra.protocols.sql_crud.message import SqlCrudMessage


class SqlCrudSerializer(Serializer):
    """Serialization for the 'sql_crud' protocol."""

    @staticmethod
    def encode(msg: Message) -> bytes:
        """
        Encode a 'SqlCrud' message into bytes.

        :param msg: the message object.
        :return: the bytes.
        """
        msg = cast(SqlCrudMessage, msg)
        message_pb = ProtobufMessage()
        dialogue_message_pb = DialogueMessage()
        sql_crud_msg = sql_crud_pb2.SqlCrudMessage()

        dialogue_message_pb.message_id = msg.message_id
        dialogue_reference = msg.dialogue_reference
        dialogue_message_pb.dialogue_starter_reference = dialogue_reference[0]
        dialogue_message_pb.dialogue_responder_reference = dialogue_reference[1]
        dialogue_message_pb.target = msg.target

        performative_id = msg.performative
        if performative_id == SqlCrudMessage.Performative.INSERT:
            performative = sql_crud_pb2.SqlCrudMessage.Insert_Performative()  # type: ignore
            table_name = msg.table_name
            performative.table_name = table_name
            labeled_records = msg.labeled_records
            LabeledRecords.encode(performative.labeled_records, labeled_records)
            sql_crud_msg.insert.CopyFrom(performative)
        elif performative_id == SqlCrudMessage.Performative.SELECT:
            performative = sql_crud_pb2.SqlCrudMessage.Select_Performative()  # type: ignore
            table_name = msg.table_name
            performative.table_name = table_name
            columns = msg.columns
            performative.columns.extend(columns)
            if msg.is_set("condition"):
                performative.condition_is_set = True
                condition = msg.condition
                performative.condition = condition
            sql_crud_msg.select.CopyFrom(performative)
        elif performative_id == SqlCrudMessage.Performative.UPDATE:
            performative = sql_crud_pb2.SqlCrudMessage.Update_Performative()  # type: ignore
            table_name = msg.table_name
            performative.table_name = table_name
            update_values = msg.update_values
            UpdateValues.encode(performative.update_values, update_values)
            if msg.is_set("condition"):
                performative.condition_is_set = True
                condition = msg.condition
                performative.condition = condition
            sql_crud_msg.update.CopyFrom(performative)
        elif performative_id == SqlCrudMessage.Performative.DELETE:
            performative = sql_crud_pb2.SqlCrudMessage.Delete_Performative()  # type: ignore
            table_name = msg.table_name
            performative.table_name = table_name
            if msg.is_set("condition"):
                performative.condition_is_set = True
                condition = msg.condition
                performative.condition = condition
            sql_crud_msg.delete.CopyFrom(performative)
        elif performative_id == SqlCrudMessage.Performative.INJECT:
            performative = sql_crud_pb2.SqlCrudMessage.Inject_Performative()  # type: ignore
            statement = msg.statement
            performative.statement = statement
            sql_crud_msg.inject.CopyFrom(performative)
        elif performative_id == SqlCrudMessage.Performative.RESULT:
            performative = sql_crud_pb2.SqlCrudMessage.Result_Performative()  # type: ignore
            if msg.is_set("result"):
                if isinstance(msg.result, int):
                    performative.result_type_int_is_set = True
                    result_type_int = msg.result
                    performative.result_type_int = result_type_int
                elif isinstance(msg.result, LabeledRecords):
                    performative.result_type_LabeledRecords_is_set = True
                    result_type_LabeledRecords = msg.result
                    LabeledRecords.encode(performative.result_type_LabeledRecords, result_type_LabeledRecords)
                elif msg.result is None:
                    pass
                else:
                    raise ValueError(f'Bad value set to `result` {msg.result }')
            sql_crud_msg.result.CopyFrom(performative)
        elif performative_id == SqlCrudMessage.Performative.ERROR:
            performative = sql_crud_pb2.SqlCrudMessage.Error_Performative()  # type: ignore
            error_code = msg.error_code
            ErrorCode.encode(performative.error_code, error_code)
            error_msg = msg.error_msg
            performative.error_msg = error_msg
            sql_crud_msg.error.CopyFrom(performative)
        else:
            raise ValueError("Performative not valid: {}".format(performative_id))

        dialogue_message_pb.content = sql_crud_msg.SerializeToString()

        message_pb.dialogue_message.CopyFrom(dialogue_message_pb)
        message_bytes = message_pb.SerializeToString()
        return message_bytes

    @staticmethod
    def decode(obj: bytes) -> Message:
        """
        Decode bytes into a 'SqlCrud' message.

        :param obj: the bytes object.
        :return: the 'SqlCrud' message.
        """
        message_pb = ProtobufMessage()
        sql_crud_pb = sql_crud_pb2.SqlCrudMessage()
        message_pb.ParseFromString(obj)
        message_id = message_pb.dialogue_message.message_id
        dialogue_reference = (
            message_pb.dialogue_message.dialogue_starter_reference,
            message_pb.dialogue_message.dialogue_responder_reference,
        )
        target = message_pb.dialogue_message.target

        sql_crud_pb.ParseFromString(message_pb.dialogue_message.content)
        performative = sql_crud_pb.WhichOneof("performative")
        performative_id = SqlCrudMessage.Performative(str(performative))
        performative_content = dict()  # type: Dict[str, Any]
        if performative_id == SqlCrudMessage.Performative.INSERT:
            table_name = sql_crud_pb.insert.table_name
            performative_content["table_name"] = table_name
            pb2_labeled_records = sql_crud_pb.insert.labeled_records
            labeled_records = LabeledRecords.decode(pb2_labeled_records)
            performative_content["labeled_records"] = labeled_records
        elif performative_id == SqlCrudMessage.Performative.SELECT:
            table_name = sql_crud_pb.select.table_name
            performative_content["table_name"] = table_name
            columns = sql_crud_pb.select.columns
            columns_tuple = tuple(columns)
            performative_content["columns"] = columns_tuple
            if sql_crud_pb.select.condition_is_set:
                condition = sql_crud_pb.select.condition
                performative_content["condition"] = condition
        elif performative_id == SqlCrudMessage.Performative.UPDATE:
            table_name = sql_crud_pb.update.table_name
            performative_content["table_name"] = table_name
            pb2_update_values = sql_crud_pb.update.update_values
            update_values = UpdateValues.decode(pb2_update_values)
            performative_content["update_values"] = update_values
            if sql_crud_pb.update.condition_is_set:
                condition = sql_crud_pb.update.condition
                performative_content["condition"] = condition
        elif performative_id == SqlCrudMessage.Performative.DELETE:
            table_name = sql_crud_pb.delete.table_name
            performative_content["table_name"] = table_name
            if sql_crud_pb.delete.condition_is_set:
                condition = sql_crud_pb.delete.condition
                performative_content["condition"] = condition
        elif performative_id == SqlCrudMessage.Performative.INJECT:
            statement = sql_crud_pb.inject.statement
            performative_content["statement"] = statement
        elif performative_id == SqlCrudMessage.Performative.RESULT:
            if sql_crud_pb.result.result_type_int_is_set:
                result = sql_crud_pb.result.result_type_int
                performative_content["result"] = result
            if sql_crud_pb.result.result_type_LabeledRecords_is_set:
                pb2_result_type_LabeledRecords = sql_crud_pb.result.result_type_LabeledRecords
                result = LabeledRecords.decode(pb2_result_type_LabeledRecords)
                performative_content["result"] = result
        elif performative_id == SqlCrudMessage.Performative.ERROR:
            pb2_error_code = sql_crud_pb.error.error_code
            error_code = ErrorCode.decode(pb2_error_code)
            performative_content["error_code"] = error_code
            error_msg = sql_crud_pb.error.error_msg
            performative_content["error_msg"] = error_msg
        else:
            raise ValueError("Performative not valid: {}.".format(performative_id))

        return SqlCrudMessage(
            message_id=message_id,
            dialogue_reference=dialogue_reference,
            target=target,
            performative=performative,
            **performative_content,
        )
