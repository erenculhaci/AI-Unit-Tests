import unittest
from code import Strongest_Extension

class TestStrongestExtension(unittest.TestCase):

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

if __name__ == "__main__":
    unittest.main()
