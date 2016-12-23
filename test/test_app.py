import unittest
from app import __version__


class TestApp(unittest.TestCase):
    def test_example(self):
        self.assertEqual(len(__version__.split('.')), 3)
