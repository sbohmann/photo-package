import unittest

from name_and_suffix import NameAndSuffix


class NameAndSuffixTest(unittest.TestCase):
    def test_simple_cases(self):
        self._check('a', '.b', 'a.b')
        self._check('a', '.', 'a.')
        self._check('a', '', 'a')

    def _check(self, name, suffix, source):
        result = NameAndSuffix(source)
        self.assertEqual(name, result.name)
        self.assertEqual(suffix, result.suffix)
