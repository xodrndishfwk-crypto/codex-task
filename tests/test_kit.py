import contextlib
import io
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import kit


class KitTests(unittest.TestCase):
    def test_help(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = kit.main(["kit.py"])
        self.assertEqual(0, result)
        self.assertIn("python kit.py check", output.getvalue())

    def test_scan_finds_data(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("task", encoding="utf-8")
            (root / "data.csv").write_text("a,b\n1,2\n", encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = kit.scan(root)
        self.assertEqual(0, result)
        self.assertIn("data.csv", output.getvalue())

    def test_csv_profile(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "data.csv"
            path.write_text("value,name\n1,A\n2,B\n2,B\n,\n", encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = kit.inspect_data(path)
        self.assertEqual(0, result)
        text = output.getvalue()
        self.assertIn("ROWS: 4", text)
        self.assertIn("DUPLICATE ROWS: 1", text)
        self.assertIn("value: blank=1", text)

    def test_list_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "manual.pdf").write_bytes(b"pdf")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = kit.list_files(root)
        self.assertEqual(0, result)
        self.assertIn("manual.pdf\t.pdf\t3", output.getvalue())

    def test_decision_check_finds_blank_source(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "decisions.csv"
            path.write_text("subject,decision,reason,source\nA,pass,meets rule,\n", encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = kit.check_decisions(path)
        self.assertEqual(1, result)
        self.assertIn("blank source", output.getvalue())


if __name__ == "__main__":
    unittest.main()
