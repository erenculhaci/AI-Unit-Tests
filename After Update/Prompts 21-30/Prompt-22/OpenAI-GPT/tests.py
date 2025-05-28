# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

import unittest
from code import Strongest_Extension

class TestStrongestExtension(unittest.TestCase):

    # --- Original Functional Tests ---
    def test_example1(self):
        self.assertEqual(
            Strongest_Extension("Slices", ['SErviNGSliCes', 'Cheese', 'StuFfed']),
            'Slices.SErviNGSliCes'
        )

    def test_example2(self):
        self.assertEqual(
            Strongest_Extension("my_class", ['AA', 'Be', 'CC']),
            'my_class.AA'
        )

    def test_tied_strengths(self):
        self.assertEqual(
            Strongest_Extension("Test", ['aA', 'Aa']),
            'Test.aA'
        )

    def test_all_negative_strengths(self):
        self.assertEqual(
            Strongest_Extension("Core", ['aaa', 'bbb', 'cCc']),
            'Core.cCc'
        )

    def test_empty_extension(self):
        self.assertEqual(
            Strongest_Extension("Void", ["", "a", "B"]),
            'Void.B'
        )

    # --- Additional Tests ---
    def test_all_uppercase_extensions(self):
        self.assertEqual(
            Strongest_Extension("MaxOut", ['AAA', 'BB', 'CCCC']),
            'MaxOut.CCCC'
        )

    def test_all_lowercase_extensions(self):
        self.assertEqual(
            Strongest_Extension("MinOut", ['aaa', 'bb', 'cccc']),
            'MinOut.aaa'
        )

    def test_mixed_case_balanced(self):
        self.assertEqual(
            Strongest_Extension("Mid", ['Ab', 'aB', 'Xx']),
            'Mid.Ab'
        )

    def test_non_alpha_characters(self):
        self.assertEqual(
            Strongest_Extension("Edge", ['A1a', '@@', 'Zz']),
            'Edge.A1a'
        )

    def test_one_extension(self):
        self.assertEqual(
            Strongest_Extension("Solo", ['OnlyOne']),
            'Solo.OnlyOne'
        )

    def test_all_empty_extensions(self):
        self.assertEqual(
            Strongest_Extension("Empty", ['', '', '']),
            'Empty.'
        )

    def test_first_strongest_by_order(self):
        self.assertEqual(
            Strongest_Extension("Tie", ['AxX', 'aXX', 'AXx']),
            'Tie.AxX'
        )

    # --- Optional Robustness (type validation) ---
    def test_non_string_extension(self):
        with self.assertRaises(TypeError):
            Strongest_Extension("Invalid", [123, 'abc'])

    def test_non_list_extensions(self):
        with self.assertRaises(TypeError):
            Strongest_Extension("Fail", "NotAList")

if __name__ == "__main__":
    unittest.main()
