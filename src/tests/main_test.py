import unittest
from main import main

class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def test_main(self):
        self.assertEqual("Hello world", main())

    def tearDown(self):
        pass