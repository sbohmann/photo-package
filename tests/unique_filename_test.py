import unittest

from unique_filename import Creator


class UniqueFilenameTest(unittest.TestCase):
    def test_simple_cases(self):
        creator = Creator()
        self.assertEqual('abc', creator.create('abc'))
        self.assertEqual('abc.jpg', creator.create('abc.jpg'))
        self.assertEqual('abc_2', creator.create('abc'))
        self.assertEqual('abc_2.jpg', creator.create('abc.jpg'))
        self.assertEqual('abc_3', creator.create('abc'))
        self.assertEqual('abc_3.jpg', creator.create('abc.jpg'))
