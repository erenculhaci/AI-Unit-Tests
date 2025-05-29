# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import Strongest_Extension

class TestStrongestExtension(unittest.TestCase):

    def test_all_lowercase_extensions(self):
        self.assertEqual(
            Strongest_Extension('MinOut', ['aaa', 'bb', 'ccc']),
            'MinOut.bb'
        )

    def test_negative_strength(self):
        self.assertEqual(
            Strongest_Extension('Neg', ['aB', 'Ab', 'ab']),
            'Neg.aB'
        )

    def test_all_uppercase_extensions(self):
        self.assertEqual(
            Strongest_Extension('MaxOut', ['ABC', 'DEF', 'GHI']),
            'MaxOut.ABC'
        )

    def test_mixed_case(self):
        self.assertEqual(
            Strongest_Extension('Mix', ['aA', 'Bb', 'CC']),
            'Mix.CC'
        )

    def test_single_extension(self):
        self.assertEqual(
            Strongest_Extension('One', ['OnlyOne']),
            'One.OnlyOne'
        )

    def test_empty_string_extension(self):
        self.assertEqual(
            Strongest_Extension('Empty', ['']),
            'Empty.'
        )

    def test_special_characters(self):
        self.assertEqual(
            Strongest_Extension('Special', ['a_b', 'A-B', '#C@']),
            'Special.A-B'
        )

    def test_numbers_in_extension(self):
        self.assertEqual(
            Strongest_Extension('Nums', ['abc1', 'ABC2', '123']),
            'Nums.ABC2'
        )

    def test_same_strength_prefers_first(self):
        self.assertEqual(
            Strongest_Extension('Tie', ['XY', 'YZ', 'ZX']),
            'Tie.XY'
        )

    def test_non_string_class_name(self):
        with self.assertRaises(AttributeError):
            Strongest_Extension(123, ['ext'])

    def test_non_list_extensions(self):
        with self.assertRaises(TypeError):
            Strongest_Extension('Invalid', 'notalist')

    def test_none_class_name(self):
        with self.assertRaises(AttributeError):
            Strongest_Extension(None, ['ext'])

    def test_none_extensions(self):
        with self.assertRaises(TypeError):
            Strongest_Extension('Class', None)

    def test_empty_extension_list(self):
        with self.assertRaises(ValueError):
            Strongest_Extension('EmptyList', [])

if __name__ == '__main__':
    unittest.main()
