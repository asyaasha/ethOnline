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

"""This module contains class representations corresponding to every custom type in the protocol specification."""

from enum import Enum
from typing import Any, Dict, List, Union

PRIMITIVES = bool, int, float, str, bytes


def _value_decode(entry_proto) -> Union[PRIMITIVES]:
    """Decode value."""

    if entry_proto.HasField("bool_value"):
        return entry_proto.bool_value
    if entry_proto.HasField("int_value"):
        return entry_proto.int_value
    if entry_proto.HasField("float_value"):
        return float(entry_proto.float_value)
    if entry_proto.HasField("str_value"):
        return entry_proto.str_value
    if entry_proto.HasField("bytes_value"):
        return entry_proto.bytes_value
    else:
        raise ValueError(f"Invalid Value entry: {entry_proto}")


def _value_encode(entry_proto, value: Union[PRIMITIVES]) -> None:
    """Encode value."""

    if isinstance(value, bool):
        entry_proto.bool_value = value
    elif isinstance(value, int):
        entry_proto.int_value = value
    elif isinstance(value, float):
        entry_proto.float_value = str(value)
    elif isinstance(value, str):
        entry_proto.str_value = value
    elif isinstance(value, bytes):
        entry_proto.bytes_value = value
    else:
        raise ValueError(f"Unsupported value type: {value}")


class ErrorCode(Enum):
    """This class represents an instance of ErrorCode."""

    INVALID_SQL_STATEMENT = 0
    INVALID_PERFORMATIVE = 1
    UNEXPECTED_EXCEPTION = 2

    @staticmethod
    def encode(error_code_protobuf_object: Any, error_code_object: "ErrorCode") -> None:
        """
        Encode an instance of this class into the protocol buffer object.
        The protocol buffer object in the error_code_protobuf_object argument is matched with the instance of this class in the 'error_code_object' argument.
        :param error_code_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :param error_code_object: an instance of this class to be encoded in the protocol buffer object.
        """
        error_code_protobuf_object.error_code = error_code_object.value

    @classmethod
    def decode(cls, error_code_protobuf_object: Any) -> "ErrorCode":
        """
        Decode a protocol buffer object that corresponds with this class into an instance of this class.
        A new instance of this class is created that matches the protocol buffer object in the 'error_code_protobuf_object' argument.
        :param error_code_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :return: A new instance of this class that matches the protocol buffer object in the 'error_code_protobuf_object' argument.
        """
        enum_value_from_pb2 = error_code_protobuf_object.error_code
        return ErrorCode(enum_value_from_pb2)


class BaseContainer:
    """BaseContainer"""

    def __eq__(self, other):
        if not isinstance(self, type(other)):
            return NotImplemented
        return self.data == other.data

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.data})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.data})"


class LabeledRecords(BaseContainer):
    """This class represents an instance of LabeledRecords."""

    def __init__(self, data: Dict[str, List[Union[PRIMITIVES]]]):
        """Initialise an instance of LabeledRecords."""

        self.data = data

    @staticmethod
    def encode(labeled_records_protobuf_object, labeled_records_object: "LabeledRecords") -> None:
        """
        Encode an instance of this class into the protocol buffer object.

        The protocol buffer object in the labeled_records_protobuf_object argument is matched with the instance of this class in the 'labeled_records_object' argument.

        :param labeled_records_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :param labeled_records_object: an instance of this class to be encoded in the protocol buffer object.
        """

        for column_name, column_values in labeled_records_object.data.items():
            column_proto = labeled_records_protobuf_object.columns.add()
            column_proto.name = column_name
            for value in column_values:
                value_proto = column_proto.values.add()
                _value_encode(value_proto, value)

    @classmethod
    def decode(cls, labeled_records_protobuf_object) -> "LabeledRecords":
        """
        Decode a protocol buffer object that corresponds with this class into an instance of this class.

        A new instance of this class is created that matches the protocol buffer object in the 'labeled_records_protobuf_object' argument.

        :param labeled_records_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :return: A new instance of this class that matches the protocol buffer object in the 'labeled_records_protobuf_object' argument.
        """

        data = {}
        for column_proto in labeled_records_protobuf_object.columns:
            column_name = column_proto.name
            column_values = []
            for value_proto in column_proto.values:
                value = _value_decode(value_proto)
                column_values.append(value)
            data[column_name] = column_values

        return cls(data)

    @property
    def rows(self) -> List[Dict[str, Union[PRIMITIVES]]]:
        """Rows."""

        return [dict(zip(self.data, values)) for values in zip(*self.data.values())]


class UpdateValues(BaseContainer):
    """This class represents an instance of UpdateValues."""

    def __init__(self, data: Dict[str, Union[PRIMITIVES]]):
        """Initialise an instance of UpdateValues."""
        self.data = data

    @staticmethod
    def encode(update_values_protobuf_object, update_values_object: "UpdateValues") -> None:
        """
        Encode an instance of this class into the protocol buffer object.

        The protocol buffer object in the update_values_protobuf_object argument is matched with the instance of this class in the 'update_values_object' argument.

        :param update_values_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :param update_values_object: an instance of this class to be encoded in the protocol buffer object.
        """

        for key, value in update_values_object.data.items():
            key_value_proto = update_values_protobuf_object.key_value_pairs.add()
            key_value_proto.key = key
            _value_encode(key_value_proto, value)

    @classmethod
    def decode(cls, update_values_protobuf_object) -> "UpdateValues":
        """
        Decode a protocol buffer object that corresponds with this class into an instance of this class.

        A new instance of this class is created that matches the protocol buffer object in the 'update_values_protobuf_object' argument.

        :param update_values_protobuf_object: the protocol buffer object whose type corresponds with this class.
        :return: A new instance of this class that matches the protocol buffer object in the 'update_values_protobuf_object' argument.
        """

        data = {}
        for key_value_proto in update_values_protobuf_object.key_value_pairs:
            key = key_value_proto.key
            value = _value_decode(key_value_proto)
            data[key] = value

        return cls(data)
