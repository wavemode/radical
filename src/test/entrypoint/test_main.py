import unittest
import os

if os.environ.get("RAD_DEBUG"):
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


class MainTest(unittest.TestCase):
    def test_success(self):
        self.assertEqual(2, 1 + 1)
