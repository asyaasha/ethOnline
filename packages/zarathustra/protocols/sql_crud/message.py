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

"""This module contains sql_crud's message definition."""

# pylint: disable=too-many-statements,too-many-locals,no-member,too-few-public-methods,too-many-branches,not-an-iterable,unidiomatic-typecheck,unsubscriptable-object
import logging
from typing import Any, Optional, Set, Tuple, Union, cast

from aea.configurations.base import PublicId
from aea.exceptions import AEAEnforceError, enforce
from aea.protocols.base import Message

from packages.zarathustra.protocols.sql_crud.custom_types import (
    ErrorCode as CustomErrorCode,
)
from packages.zarathustra.protocols.sql_crud.custom_types import (
    LabeledRecords as CustomLabeledRecords,
)
from packages.zarathustra.protocols.sql_crud.custom_types import (
    UpdateValues as CustomUpdateValues,
)


_default_logger = logging.getLogger("aea.packages.zarathustra.protocols.sql_crud.message")

DEFAULT_BODY_SIZE = 4


class SqlCrudMessage(Message):
    """A protocol for SQL CRUD functionality."""

    protocol_id = PublicId.from_str("zarathustra/sql_crud:0.1.0")
    protocol_specification_id = PublicId.from_str("zarathustra/sql_crud:0.1.0")

    ErrorCode = CustomErrorCode

    LabeledRecords = CustomLabeledRecords

    UpdateValues = CustomUpdateValues

    class Performative(Message.Performative):
        """Performatives for the sql_crud protocol."""

        DELETE = "delete"
        ERROR = "error"
        INJECT = "inject"
        INSERT = "insert"
        RESULT = "result"
        SELECT = "select"
        UPDATE = "update"

        def __str__(self) -> str:
            """Get the string representation."""
            return str(self.value)

    _performatives = {"delete", "error", "inject", "insert", "result", "select", "update"}
    __slots__: Tuple[str, ...] = tuple()

    class _SlotsCls:
        __slots__ = (
            "columns",
            "condition",
            "dialogue_reference",
            "error_code",
            "error_msg",
            "labeled_records",
            "message_id",
            "performative",
            "result",
            "statement",
            "table_name",
            "target",
            "update_values",
        )

    def __init__(
        self,
        performative: Performative,
        dialogue_reference: Tuple[str, str] = ("", ""),
        message_id: int = 1,
        target: int = 0,
        **kwargs: Any,
    ):
        """
        Initialise an instance of SqlCrudMessage.

        :param message_id: the message id.
        :param dialogue_reference: the dialogue reference.
        :param target: the message target.
        :param performative: the message performative.
        :param **kwargs: extra options.
        """
        super().__init__(
            dialogue_reference=dialogue_reference,
            message_id=message_id,
            target=target,
            performative=SqlCrudMessage.Performative(performative),
            **kwargs,
        )

    @property
    def valid_performatives(self) -> Set[str]:
        """Get valid performatives."""
        return self._performatives

    @property
    def dialogue_reference(self) -> Tuple[str, str]:
        """Get the dialogue_reference of the message."""
        enforce(self.is_set("dialogue_reference"), "dialogue_reference is not set.")
        return cast(Tuple[str, str], self.get("dialogue_reference"))

    @property
    def message_id(self) -> int:
        """Get the message_id of the message."""
        enforce(self.is_set("message_id"), "message_id is not set.")
        return cast(int, self.get("message_id"))

    @property
    def performative(self) -> Performative:  # type: ignore # noqa: F821
        """Get the performative of the message."""
        enforce(self.is_set("performative"), "performative is not set.")
        return cast(SqlCrudMessage.Performative, self.get("performative"))

    @property
    def target(self) -> int:
        """Get the target of the message."""
        enforce(self.is_set("target"), "target is not set.")
        return cast(int, self.get("target"))

    @property
    def columns(self) -> Tuple[str, ...]:
        """Get the 'columns' content from the message."""
        enforce(self.is_set("columns"), "'columns' content is not set.")
        return cast(Tuple[str, ...], self.get("columns"))

    @property
    def condition(self) -> Optional[str]:
        """Get the 'condition' content from the message."""
        return cast(Optional[str], self.get("condition"))

    @property
    def error_code(self) -> CustomErrorCode:
        """Get the 'error_code' content from the message."""
        enforce(self.is_set("error_code"), "'error_code' content is not set.")
        return cast(CustomErrorCode, self.get("error_code"))

    @property
    def error_msg(self) -> str:
        """Get the 'error_msg' content from the message."""
        enforce(self.is_set("error_msg"), "'error_msg' content is not set.")
        return cast(str, self.get("error_msg"))

    @property
    def labeled_records(self) -> CustomLabeledRecords:
        """Get the 'labeled_records' content from the message."""
        enforce(self.is_set("labeled_records"), "'labeled_records' content is not set.")
        return cast(CustomLabeledRecords, self.get("labeled_records"))

    @property
    def result(self) -> Union[int, CustomLabeledRecords]:
        """Get the 'result' content from the message."""
        enforce(self.is_set("result"), "'result' content is not set.")
        return cast(Union[int, CustomLabeledRecords], self.get("result"))

    @property
    def statement(self) -> str:
        """Get the 'statement' content from the message."""
        enforce(self.is_set("statement"), "'statement' content is not set.")
        return cast(str, self.get("statement"))

    @property
    def table_name(self) -> str:
        """Get the 'table_name' content from the message."""
        enforce(self.is_set("table_name"), "'table_name' content is not set.")
        return cast(str, self.get("table_name"))

    @property
    def update_values(self) -> CustomUpdateValues:
        """Get the 'update_values' content from the message."""
        enforce(self.is_set("update_values"), "'update_values' content is not set.")
        return cast(CustomUpdateValues, self.get("update_values"))

    def _is_consistent(self) -> bool:
        """Check that the message follows the sql_crud protocol."""
        try:
            enforce(
                isinstance(self.dialogue_reference, tuple),
                "Invalid type for 'dialogue_reference'. Expected 'tuple'. Found '{}'.".format(
                    type(self.dialogue_reference)
                ),
            )
            enforce(
                isinstance(self.dialogue_reference[0], str),
                "Invalid type for 'dialogue_reference[0]'. Expected 'str'. Found '{}'.".format(
                    type(self.dialogue_reference[0])
                ),
            )
            enforce(
                isinstance(self.dialogue_reference[1], str),
                "Invalid type for 'dialogue_reference[1]'. Expected 'str'. Found '{}'.".format(
                    type(self.dialogue_reference[1])
                ),
            )
            enforce(
                type(self.message_id) is int,
                "Invalid type for 'message_id'. Expected 'int'. Found '{}'.".format(type(self.message_id)),
            )
            enforce(
                type(self.target) is int,
                "Invalid type for 'target'. Expected 'int'. Found '{}'.".format(type(self.target)),
            )

            # Light Protocol Rule 2
            # Check correct performative
            enforce(
                isinstance(self.performative, SqlCrudMessage.Performative),
                "Invalid 'performative'. Expected either of '{}'. Found '{}'.".format(
                    self.valid_performatives, self.performative
                ),
            )

            # Check correct contents
            actual_nb_of_contents = len(self._body) - DEFAULT_BODY_SIZE
            expected_nb_of_contents = 0
            if self.performative == SqlCrudMessage.Performative.INSERT:
                expected_nb_of_contents = 2
                enforce(
                    isinstance(self.table_name, str),
                    "Invalid type for content 'table_name'. Expected 'str'. Found '{}'.".format(type(self.table_name)),
                )
                enforce(
                    isinstance(self.labeled_records, CustomLabeledRecords),
                    "Invalid type for content 'labeled_records'. Expected 'LabeledRecords'. Found '{}'.".format(
                        type(self.labeled_records)
                    ),
                )
            elif self.performative == SqlCrudMessage.Performative.SELECT:
                expected_nb_of_contents = 2
                enforce(
                    isinstance(self.table_name, str),
                    "Invalid type for content 'table_name'. Expected 'str'. Found '{}'.".format(type(self.table_name)),
                )
                enforce(
                    isinstance(self.columns, tuple),
                    "Invalid type for content 'columns'. Expected 'tuple'. Found '{}'.".format(type(self.columns)),
                )
                enforce(
                    all(isinstance(element, str) for element in self.columns),
                    "Invalid type for tuple elements in content 'columns'. Expected 'str'.",
                )
                if self.is_set("condition"):
                    expected_nb_of_contents += 1
                    condition = cast(str, self.condition)
                    enforce(
                        isinstance(condition, str),
                        "Invalid type for content 'condition'. Expected 'str'. Found '{}'.".format(type(condition)),
                    )
            elif self.performative == SqlCrudMessage.Performative.UPDATE:
                expected_nb_of_contents = 2
                enforce(
                    isinstance(self.table_name, str),
                    "Invalid type for content 'table_name'. Expected 'str'. Found '{}'.".format(type(self.table_name)),
                )
                enforce(
                    isinstance(self.update_values, CustomUpdateValues),
                    "Invalid type for content 'update_values'. Expected 'UpdateValues'. Found '{}'.".format(
                        type(self.update_values)
                    ),
                )
                if self.is_set("condition"):
                    expected_nb_of_contents += 1
                    condition = cast(str, self.condition)
                    enforce(
                        isinstance(condition, str),
                        "Invalid type for content 'condition'. Expected 'str'. Found '{}'.".format(type(condition)),
                    )
            elif self.performative == SqlCrudMessage.Performative.DELETE:
                expected_nb_of_contents = 1
                enforce(
                    isinstance(self.table_name, str),
                    "Invalid type for content 'table_name'. Expected 'str'. Found '{}'.".format(type(self.table_name)),
                )
                if self.is_set("condition"):
                    expected_nb_of_contents += 1
                    condition = cast(str, self.condition)
                    enforce(
                        isinstance(condition, str),
                        "Invalid type for content 'condition'. Expected 'str'. Found '{}'.".format(type(condition)),
                    )
            elif self.performative == SqlCrudMessage.Performative.INJECT:
                expected_nb_of_contents = 1
                enforce(
                    isinstance(self.statement, str),
                    "Invalid type for content 'statement'. Expected 'str'. Found '{}'.".format(type(self.statement)),
                )
            elif self.performative == SqlCrudMessage.Performative.RESULT:
                expected_nb_of_contents = 1
                enforce(
                    isinstance(self.result, CustomLabeledRecords) or type(self.result) is int,
                    "Invalid type for content 'result'. Expected either of '['LabeledRecords', 'int']'. Found '{}'.".format(
                        type(self.result)
                    ),
                )
            elif self.performative == SqlCrudMessage.Performative.ERROR:
                expected_nb_of_contents = 2
                enforce(
                    isinstance(self.error_code, CustomErrorCode),
                    "Invalid type for content 'error_code'. Expected 'ErrorCode'. Found '{}'.".format(
                        type(self.error_code)
                    ),
                )
                enforce(
                    isinstance(self.error_msg, str),
                    "Invalid type for content 'error_msg'. Expected 'str'. Found '{}'.".format(type(self.error_msg)),
                )

            # Check correct content count
            enforce(
                expected_nb_of_contents == actual_nb_of_contents,
                "Incorrect number of contents. Expected {}. Found {}".format(
                    expected_nb_of_contents, actual_nb_of_contents
                ),
            )

            # Light Protocol Rule 3
            if self.message_id == 1:
                enforce(
                    self.target == 0,
                    "Invalid 'target'. Expected 0 (because 'message_id' is 1). Found {}.".format(self.target),
                )
        except (AEAEnforceError, ValueError, KeyError) as e:
            _default_logger.error(str(e))
            return False

        return True
