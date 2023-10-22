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

"""Test dialogues module for sql_crud protocol."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,redefined-builtin
from aea.test_tools.test_protocol import BaseProtocolDialoguesTestCase

from packages.zarathustra.protocols.sql_crud.custom_types import LabeledRecords
from packages.zarathustra.protocols.sql_crud.dialogues import SqlCrudDialogue, SqlCrudDialogues
from packages.zarathustra.protocols.sql_crud.message import SqlCrudMessage

DUMMY_LABELED_RECORDS = LabeledRecords(
    {
        "int_column": [1, 2, 3],
        "float_column": [1.1, 2.2, 3.3],
        "bool_column": [True, False, True],
        "str_column": ["apple", "banana", "cherry"],
        "bytes_column": [b"byte1", b"byte2", b"byte3"],
    }
)


class TestDialoguesSqlCrud(BaseProtocolDialoguesTestCase):
    """Test for the 'sql_crud' protocol dialogues."""

    MESSAGE_CLASS = SqlCrudMessage

    DIALOGUE_CLASS = SqlCrudDialogue

    DIALOGUES_CLASS = SqlCrudDialogues

    ROLE_FOR_THE_FIRST_MESSAGE = SqlCrudDialogue.Role.CLIENT

    def make_message_content(self) -> dict:
        """Make a dict with message contruction content for dialogues.create."""
        return dict(
            performative=SqlCrudMessage.Performative.INSERT,
            table_name="some str",
            labeled_records=DUMMY_LABELED_RECORDS,
        )
