import unittest
from code import Strongest_Extension

class TestStrongestExtension(unittest.TestCase):
    
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
    
    def test_mixed_case(self):
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
    
    def test_empty_extensions(self):
        self.assertEqual(
            Strongest_Extension('Empty', ['']),
            'Empty.'
        )

if __name__ == '__main__':
    unittest.main()