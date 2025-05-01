import unittest
from code import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]), ['A+', 'B', 'C-', 'C', 'A-'])

    def test_all_perfect(self):
        self.assertEqual(numerical_letter_grade([4.0, 4.0, 4.0]), ['A+', 'A+', 'A+'])

    def test_edge_cases(self):
        self.assertEqual(numerical_letter_grade([3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]), 
                         ['A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E'])

    def test_lowest_scores(self):
        self.assertEqual(numerical_letter_grade([0.2, 0.5, 0.6]), ['D-', 'D-', 'D-'])

    def test_random_gpas(self):
        self.assertEqual(numerical_letter_grade([2.5, 3.8, 1.9, 0.8]), ['B-', 'A', 'C', 'D'])

if __name__ == "__main__":
    unittest.main()
