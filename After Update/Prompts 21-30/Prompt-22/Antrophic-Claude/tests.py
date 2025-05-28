# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import Strongest_Extension

class TestStrongestExtension(unittest.TestCase):

    # --- Valid Functional Tests ---
    def test_example_1(self):
        self.assertEqual(
            Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']),
            'Slices.SErviNGSliCes'
        )

    def test_example_2(self):
        self.assertEqual(
            Strongest_Extension('my_class', ['AA', 'Be', 'CC']),
            'my_class.AA'
        )

    def test_all_uppercase(self):
        self.assertEqual(
            Strongest_Extension('Class', ['AAA', 'BBB', 'CCC']),
            'Class.AAA'
        )

    def test_all_lowercase(self):
        self.assertEqual(
            Strongest_Extension('Test', ['aaa', 'bbb', 'ccc']),
            'Test.aaa'
        )

    def test_mixed_case_variants(self):
        self.assertEqual(
            Strongest_Extension('Mixed', ['AbC', 'aBc', 'ABC']),
            'Mixed.ABC'
        )

    def test_same_strength_first_wins(self):
        self.assertEqual(
            Strongest_Extension('Same', ['AB', 'CD', 'EF']),
            'Same.AB'
        )

    def test_negative_strength(self):
        self.assertEqual(
            Strongest_Extension('Neg', ['aB', 'Ab', 'ab']),
            'Neg.Ab'
        )

    def test_single_extension(self):
        self.assertEqual(
            Strongest_Extension('Single', ['OnlyOne']),
            'Single.OnlyOne'
        )

    def test_zero_strength(self):
        self.assertEqual(
            Strongest_Extension('Zero', ['Aa', 'Bb', 'Cc']),
            'Zero.Aa'
        )

    def test_large_strength_difference(self):
        self.assertEqual(
            Strongest_Extension('Large', ['ABCDEF', 'abcdef', 'AbCdEf']),
            'Large.ABCDEF'
        )

    def test_complex_mixed_case(self):
        self.assertEqual(
            Strongest_Extension('Complex', ['PyThOn', 'JAVA', 'javascript']),
            'Complex.JAVA'
        )

    # --- Edge Cases ---
    def test_empty_extension(self):
        self.assertEqual(
            Strongest_Extension('Empty', ['']),
            'Empty.'
        )

    def test_extensions_with_numbers(self):
        self.assertEqual(
            Strongest_Extension('Nums', ['Ext1', 'EXT2', 'ext3']),
            'Nums.EXT2'
        )

    def test_extensions_with_special_chars(self):
        self.assertEqual(
            Strongest_Extension('Special', ['Ext_1', 'EXT-2', 'ext@3']),
            'Special.EXT-2'
        )

    def test_very_long_extensions(self):
        self.assertEqual(
            Strongest_Extension('Long', ['VeryLongExtensionName', 'SHORT']),
            'Long.SHORT'
        )

    def test_identical_extensions(self):
        self.assertEqual(
            Strongest_Extension('Identical', ['Same', 'Same', 'Same']),
            'Identical.Same'
        )

    # --- Boundary Cases ---
    def test_only_uppercase_letters(self):
        self.assertEqual(
            Strongest_Extension('Upper', ['A', 'BB', 'CCC']),
            'Upper.A'
        )

    def test_only_lowercase_letters(self):
        self.assertEqual(
            Strongest_Extension('Lower', ['a', 'bb', 'ccc']),
            'Lower.a'
        )

    def test_alternating_case_pattern(self):
        self.assertEqual(
            Strongest_Extension('Alt', ['AbAbAb', 'aBaBaB']),
            'Alt.AbAbAb'
        )

    def test_multiple_same_max_strength(self):
        self.assertEqual(
            Strongest_Extension('Multi', ['ABC', 'DEF', 'GHI']),
            'Multi.ABC'
        )

    # --- Invalid Input Tests ---
    def test_non_string_class_name(self):
        with self.assertRaises(AttributeError):
            Strongest_Extension(123, ['ext'])

    def test_non_list_extensions(self):
        with self.assertRaises(TypeError):
            Strongest_Extension('Class', 'not_a_list')

    def test_none_class_name(self):
        with self.assertRaises(AttributeError):
            Strongest_Extension(None, ['ext'])

    def test_none_extensions(self):
        with self.assertRaises(TypeError):
            Strongest_Extension('Class', None)

    def test_empty_extensions_list(self):
        with self.assertRaises(ValueError):
            Strongest_Extension('Class', [])

if __name__ == '__main__':
    unittest.main()