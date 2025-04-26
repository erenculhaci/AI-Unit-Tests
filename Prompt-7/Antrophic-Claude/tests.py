import unittest
from code import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):
    
    def test_example_case(self):
        # Test the example provided in the function docstring
        grades = [4.0, 3, 1.7, 2, 3.5]
        expected = ['A+', 'B', 'C-', 'C', 'A-']
        self.assertEqual(numerical_letter_grade(grades), expected)
    
    def test_all_grade_levels(self):
        # Test all possible grade boundaries
        grades = [4.0, 3.8, 3.5, 3.1, 2.8, 2.5, 2.1, 1.8, 1.5, 1.1, 0.8, 0.5, 0.0]
        expected = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
        self.assertEqual(numerical_letter_grade(grades), expected)
    
    def test_edge_cases(self):
        # Test edge cases including empty list
        grades = []
        expected = []
        self.assertEqual(numerical_letter_grade(grades), expected)
    
    def test_same_grades(self):
        # Test when all students have the same grade
        grades = [3.0, 3.0, 3.0]
        expected = ['B', 'B', 'B']
        self.assertEqual(numerical_letter_grade(grades), expected)
    
    def test_extreme_grades(self):
        # Test with very high and very low grades
        grades = [4.0, 0.0, 4.0, 0.0]
        expected = ['A+', 'E', 'A+', 'E']
        self.assertEqual(numerical_letter_grade(grades), expected)

if __name__ == '__main__':
    unittest.main()