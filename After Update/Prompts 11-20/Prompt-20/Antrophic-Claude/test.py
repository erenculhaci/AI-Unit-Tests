import unittest
from code import is_sorted

class TestIsSorted(unittest.TestCase):

    def test_single_element_list(self):
        self.assertTrue(is_sorted([5]))

    def test_sorted_lists(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6]))
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 6, 7]))

    def test_unsorted_lists(self):
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        self.assertFalse(is_sorted([5, 4, 3, 2, 1]))

    def test_allowed_duplicates(self):
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))
        self.assertTrue(is_sorted([1, 1, 2, 2, 3, 3, 4]))

    def test_too_many_duplicates(self):
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))
        self.assertFalse(is_sorted([1, 1, 1, 2, 3, 4]))

    def test_empty_list(self):
        self.assertTrue(is_sorted([]))

    def test_duplicate_threshold(self):
        self.assertTrue(is_sorted([2, 2]))
        self.assertTrue(is_sorted([1, 1, 2, 2, 3, 3]))
        self.assertFalse(is_sorted([2, 2, 2]))

    def test_identical_elements(self):
        self.assertTrue(is_sorted([7]))
        self.assertTrue(is_sorted([7, 7]))
        self.assertFalse(is_sorted([7, 7, 7]))

    def test_unsorted_with_duplicates(self):
        self.assertFalse(is_sorted([3, 2, 2, 2]))
        self.assertFalse(is_sorted([1, 3, 3, 3, 2]))

    def test_large_numbers(self):
        self.assertTrue(is_sorted([1000, 2000, 3000]))
        self.assertTrue(is_sorted([1000, 1000, 2000]))
        self.assertFalse(is_sorted([1000, 1000, 1000]))

    def test_non_list_input(self):
        with self.assertRaises(ValueError):
            is_sorted("12345")
        with self.assertRaises(ValueError):
            is_sorted(12345)

    def test_non_integer_values(self):
        with self.assertRaises(ValueError):
            is_sorted([1, 2, "3", 4])
        with self.assertRaises(ValueError):
            is_sorted([1, 2.5, 3])

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            is_sorted([-1, 0, 1])
        with self.assertRaises(ValueError):
            is_sorted([1, -2, 3])

if __name__ == "__main__":
    unittest.main()
