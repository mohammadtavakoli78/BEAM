"""Test the real converters without model imports or dataset downloads."""

import ast
import json
import os
import pickle
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_converter(relative_path):
    # download_dataset.py runs downloads on import. Compile only the actual
    # converter definition so these tests need no external service or package.
    path = ROOT / relative_path
    tree = ast.parse(path.read_text(encoding="utf-8"))
    function = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "convert_chats_pickle_to_json"
    )
    namespace = {"json": json, "os": os, "pickle": pickle}
    module = ast.Module(body=[function], type_ignores=[])
    exec(compile(module, str(path), "exec"), namespace)  # noqa: S102 -- trusted repository source
    return namespace[function.name]


class ChatConversionTests(unittest.TestCase):
    def check_conversion(self, batches, expected_anchors, expected_turns):
        for path in ("src/beam/download_dataset.py", "src/beam/utils.py"):
            with self.subTest(converter=path):
                converter = load_converter(path)
                if path.endswith("download_dataset.py"):
                    result = converter(batches)
                else:
                    with tempfile.TemporaryDirectory() as directory:
                        source = Path(directory) / "chat.pickle"
                        destination = Path(directory) / "chat.json"
                        with source.open("wb") as stream:
                            pickle.dump(batches, stream)
                        converter(str(source), str(destination))
                        result = json.loads(destination.read_text())
                self.assertEqual(
                    [batch["time_anchor"] for batch in result], expected_anchors
                )
                self.assertEqual([batch["turns"] for batch in result], expected_turns)
                self.assertEqual(
                    [batch["batch_number"] for batch in result],
                    list(range(1, len(batches) + 1)),
                )

    def test_first_turn_anchor_survives_followups_without_anchor_fields(self):
        first = {
            "id": 0,
            "role": "user",
            "question_type": "main_question",
            "time_anchor": "July-01-2024",
            "content": "Start",
        }
        reply = {"id": 1, "role": "assistant", "content": "Reply"}
        followup = {
            "id": 2,
            "role": "user",
            "question_type": "main_question",
            "content": "Follow-up",
        }
        self.check_conversion(
            [[first, reply, followup]],
            ["July-01-2024"],
            [[[first, reply], [followup]]],
        )

    def test_null_followup_anchors_do_not_erase_the_batch_date(self):
        first = {
            "id": 0,
            "role": "user",
            "question_type": "main_question",
            "time_anchor": "July-01-2024",
            "content": "Start",
        }
        reply = {"id": 1, "role": "assistant", "time_anchor": None, "content": "Reply"}
        followup = {
            "id": 2,
            "role": "user",
            "question_type": "main_question",
            "time_anchor": None,
            "content": "Follow-up",
        }
        self.check_conversion(
            [[first, reply, followup]],
            ["July-01-2024"],
            [[[first, reply], [followup]]],
        )

    def test_unknown_batch_date_stays_unknown(self):
        first = {
            "id": 0,
            "role": "user",
            "question_type": "main_question",
            "time_anchor": None,
            "content": "Undated",
        }
        reply = {"id": 1, "role": "assistant", "content": "Reply"}
        self.check_conversion([[first, reply]], [None], [[[first, reply]]])

    def test_date_does_not_leak_into_the_next_batch(self):
        dated = {
            "id": 0,
            "role": "user",
            "question_type": "main_question",
            "time_anchor": "July-01-2024",
            "content": "Dated",
        }
        undated = {
            "id": 1,
            "role": "user",
            "question_type": "main_question",
            "content": "Undated",
        }
        self.check_conversion(
            [[dated], [undated]],
            ["July-01-2024", None],
            [[[dated]], [[undated]]],
        )


if __name__ == "__main__":
    unittest.main()
