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

"""Test messages module for sql_crud protocol."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,redefined-builtin
from typing import List

from aea.test_tools.test_protocol import BaseProtocolMessagesTestCase

from packages.zarathustra.protocols.sql_crud.custom_types import ErrorCode, LabeledRecords, UpdateValues
from packages.zarathustra.protocols.sql_crud.message import SqlCrudMessage


UPDATE_VALUES = UpdateValues(
    {
        "int_column": 1,
        "float_column": 1.1,
        "bool_column": True,
        "str_column": "apple",
        "bytes_column": b"byte",
    }
)

LABELED_RECORDS = LabeledRecords(
    {
        "int_column": [1, 2, 3],
        "float_column": [1.1, 2.2, 3.3],
        "bool_column": [True, False, True],
        "str_column": ["apple", "banana", "cherry"],
        "bytes_column": [b"byte1", b"byte2", b"byte3"],
    }
)


class TestMessageSqlCrud(BaseProtocolMessagesTestCase):
    """Test for the 'sql_crud' protocol message."""

    MESSAGE_CLASS = SqlCrudMessage

    def build_messages(self) -> List[SqlCrudMessage]:  # type: ignore[override]
        """Build the messages to be used for testing."""
        return [
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.INSERT,
                table_name="some str",
                labeled_records=LABELED_RECORDS,
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.SELECT,
                table_name="some str",
                columns=("some str",),
                condition="some str",
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.UPDATE,
                table_name="some str",
                update_values=UPDATE_VALUES, 
                condition="some str",
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.DELETE,
                table_name="some str",
                condition="some str",
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.INJECT,
                statement="some str",
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.RESULT,
                result=12,
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.RESULT,
                result=LABELED_RECORDS,
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.ERROR,
                error_code=ErrorCode(0),
                error_msg="some str",
            ),
        ]

    def build_inconsistent(self) -> List[SqlCrudMessage]:  # type: ignore[override]
        """Build inconsistent messages to be used for testing."""
        return [
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.INSERT,
                # skip content: table_name
                labeled_records=LABELED_RECORDS,
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.SELECT,
                # skip content: table_name
                columns=("some str",),
                condition="some str",
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.UPDATE,
                # skip content: table_name
                update_values=UPDATE_VALUES,
                condition="some str",
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.DELETE,
                # skip content: table_name
                condition="some str",
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.INJECT,
                # skip content: statement
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.RESULT,
                # skip content: result
            ),
            SqlCrudMessage(
                performative=SqlCrudMessage.Performative.ERROR,
                # skip content: error_code
                error_msg="some str",
            ),
        ]
