"""Exercise the validator CLI and Git's commit-msg hook."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("check_commit_message.py")


class CommitMessageTests(unittest.TestCase):
    def check_message(self, message):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--message", message],
            capture_output=True,
            text=True,
        )

    def test_accepts_allowed_types_and_message_bodies(self):
        for prefix in ("feat", "fix", "refactor", "docs", "test", "perf", "build", "ci", "chore"):
            with self.subTest(prefix=prefix):
                result = self.check_message(prefix + ": validate commit titles\n\nCommit body.")
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_invalid_titles(self):
        for message in ("Apply changes", "feature: add skill", "fix:", "fix: ",
                        "fix:    ", "fix:add skill", " fix: add skill", "", "\nfix: add skill"):
            with self.subTest(message=message):
                result = self.check_message(message)
                self.assertEqual(result.returncode, 1)
                self.assertIn("Invalid commit title", result.stderr)

    def test_message_file_input_and_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            message_file = Path(directory) / "message.txt"
            message_file.write_text("docs: describe commit validation\n", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(message_file)])
            self.assertEqual(result.returncode, 0)
            message_file.unlink()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(message_file)], capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 2)

    def test_git_hook_rejects_invalid_commit_and_accepts_valid_commit(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)

            def git(*args):
                return subprocess.run(
                    ["git", "-C", str(repo), *args], capture_output=True, text=True,
                )

            result = git("init", "--quiet")
            self.assertEqual(result.returncode, 0, result.stderr)
            hooks = repo / ".git" / "hooks"
            result = git("config", "core.hooksPath", str(hooks))
            self.assertEqual(result.returncode, 0, result.stderr)
            hook = hooks / "commit-msg"
            shutil.copyfile(SCRIPT, hook)
            hook.chmod(0o755)

            def commit(message):
                return git("-c", "user.name=Test", "-c", "user.email=test@example.com",
                           "-c", "commit.gpgsign=false", "commit", "--allow-empty", "-m", message)

            result = commit("Apply changes")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Invalid commit title", result.stderr)
            self.assertNotEqual(git("rev-parse", "--verify", "HEAD").returncode, 0)
            result = commit("fix: validate checkpoint commit messages")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(git("log", "-1", "--format=%s").stdout.strip(),
                             "fix: validate checkpoint commit messages")


if __name__ == "__main__":
    unittest.main()
