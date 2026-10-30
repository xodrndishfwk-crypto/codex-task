import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_toolkit


class ValidateToolkitTests(unittest.TestCase):
    def test_current_repository_passes(self):
        self.assertEqual([], validate_toolkit.validate())

    def test_missing_files_are_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            errors = validate_toolkit.validate(Path(directory))
        self.assertTrue(any("missing required file" in error for error in errors))

    def test_secret_pattern_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative in validate_toolkit.REQUIRED:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("---\nname: x\ndescription: x\n---\n" if path.name == "SKILL.md" else "ok\n", encoding="utf-8")
            fake_token = "gh" + "p_" + "12345678901234567890"
            (root / "sample.txt").write_text(f"token={fake_token}", encoding="utf-8")
            errors = validate_toolkit.validate(root)
        self.assertTrue(any("GitHub token" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
