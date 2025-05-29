def move_one_ball(arr):
    """
    Write a Python function that determines whether a list of unique integers can be sorted into non-decreasing order by performing any number of right shift operations (i.e., circular rotations to the right).

    Requirements:
    - Input must be only a list of unique integers.
    - Return True if the array can be sorted with right shifts only; else, return False.
    - Raise an error if the input is not a list or contains any non-integer or boolean.
    - An empty list or a list with one element should be considered sortable.
    - The logic must correctly handle sorted, rotated, and unsortable cases.

    Parameters:
    arr (list): A list of unique integers.

    Returns:
    bool: True if the list can be sorted using only right shifts; False otherwise.

    Raises:
    ValueError: If the input is not a list or contains non-integer or boolean elements.
    """


def pluck(arr):
    """
    You are given an array which is a branch of a tree, where each node is a non-negative integer.

    You will implement a function called `pluck(arr)` that finds and returns the node with the smallest even value, with its index alongside. The return value must be a list of the form `[smallest_even_value, index]`.

    Requirements:
    - If multiple nodes have the same smallest even value, return the one having the smallest index.
    - If there are no even values or the input list is empty, return empty list: `[]`.
    - The function must:
    * Only accept inputs that are lists of non-negative integers (also exclude boolean values).
    * Raise a `TypeError` if the input is not a list.
    * Raise a `TypeError` if any element in the list is not a valid non-negative integer (e.g., float, bool, string, etc.).
    * Raise a `ValueError` if any integer in the list is negative.

    Your implementation must be robust and include necessary input validation for type and value correctness.

    Input Validation:
    - Raise a TypeError if the input is not a list.
    - Raise a TypeError if any element in the list is not a valid non-negative integer 
      (e.g., float, bool, string, etc.).
    - Raise a ValueError if any integer in the list is negative.

    Parameters:
    arr (list): A list of non-negative integers representing nodes.

    Returns:
    list: A list containing the smallest even value and its index [value, index], or [] if no even values exist.

    Raises:
    TypeError: If the input is not a list or contains invalid types.
    ValueError: If the list contains negative integers.

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """


def minPath(grid, k):
    """
    Find the minimum lexicographical path of length k in the given N x N grid.

    A path is defined as a sequence of adjacent cells (up, down, left, right)
    with no cell visited more than once (i.e., a simple path). The path length
    is the number of cells included.

    The minimum path is the one whose sequence of cell values is lexicographically smallest
    between all simple paths of length k in the grid.

    Args:
    - grid (List[List[int]]): A square 2D list of integers of size N x N, with unique
    integers from 1 to N x N.
    - k (int): A positive integer which represents the desired length of the path.

    Returns:
    - List[int]: The values on the cells that the minimum lexicographical path goes through.
    Returns an empty list if there is no path of length k exists.

    Raises:
    - TypeError: If the inputs are not one of the expected types:
    - grid must be a list of lists of integers only,
    - all rows must have the same length equal to grid size (square),
    - k must be a positive integer.

    Notes:
    - Paths must not revisit any cell.
    - Adjacent cells share an edge (up, down, left, or right).
    - If k <= 0, or grid is empty, return an empty list.
            
    Examples:

        Input: grid = [ [1,2,3], [4,5,6], [7,8,9]], k = 3
        Output: [1, 2, 1]

        Input: grid = [ [5,9,3], [4,1,6], [7,8,2]], k = 1
        Output: [1]
    """


def maximum(arr, k):
    """
    Given an array arr and a non-negative integer k, return a sorted list
    in ascending order containing the k largest elements in arr.

    If k is 0, return an empty list. If k is larger than the length of arr, 
    return the k largest elements that exist (i.e., up to the full array). The function must validate
    inputs and give suitable exceptions in case of invalid input types or values.

    Args:
    - arr (List[Union[int, float]]): A list or tuple of comparable numeric values.
    - k (int): A non-negative integer specifying how many of the largest values to return.

    Returns:
    - List[Union[int, float]]: A list of the k largest elements from arr, sorted in ascending order.

    Raises:
    - TypeError: If arr is not a list or tuple, or if k is not an integer.
    - TypeError: If the elements in arr are not all comparable (e.g., mixing strings and numbers).
    - ValueError: If k is negative.

    Examples:
    - maximum([-3, -4, 5], 3) => [-4, -3, 5]
    - maximum([4, -4, 4], 2) => [4, 4]
    - maximum([-3, 2, 1, 2, -1, -2, 1], 1) => [2]
    - maximum([1.5, 2, 3.7, 3], 2) => [3, 3.7]
    - maximum([1, 2, 3], 0) => []

    Notes:
    - The result list is always sorted in ascending order, regardless of the original order.
    - Duplicates are kept.
    - The function is functional with float and integer comparisons.
    """


def even_odd_palindrome(n):
    """
    Given a non-negative integer `n`, return a tuple `(even_count, odd_count)` representing the number of
    even and odd palindromic integers within the inclusive range from `1` to `n`.

    A palindromic integer is a number that reads the same forwards and backwards (e.g., 1, 121, 22).

    Args:
    - n (int): A non-negative integer specifying the upper bound of the range to check for integer palindromes (inclusive).

    Returns:
    - Tuple[int, int]: A tuple `(even_count, odd_count)` where:
      - even_count is the number of even palindromic integers in the range [1, n]
      - odd_count is the number of odd palindromic integers in the range [1, n]

    Raises:
    - TypeError: If n is not an integer, or if it is a boolean value.
    - ValueError: If n is negative.

    Examples:
    - even_odd_palindrome(3) => (1, 2)  # palindromes: 1, 2, 3
    - even_odd_palindrome(12) => (4, 6)  # palindromes: 1--9, 11
    - even_odd_palindrome(50) => (6, 7)  # evens: 2,4,6,8,22,44; odds: 1,3,5,7,9,11,33
    - even_odd_palindrome(99) => (8, 10) # palindromes up to 99
    - even_odd_palindrome(0) => (0, 0)   # empty range

    Notes:
    - Input n must be a non-negative integer. Floats, strings, booleans, and other types are not allowed.
    - Boolean values like True and False are explicitly rejected, even though they are subclasses of int in Python.
    - The function counts all numeric palindromes between 1 and n, inclusive.
    - This function handles input values up to at least 10^3 efficiently.
    """


def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list (in ascending order) of all the odd numbers
    encountered in the full Collatz sequence starting from n until it reaches 1.

    The Collatz sequence can be defined like below:
    - Start with any positive integer n.
    - For each item:
      - If the current term is even, the next term is the previous term divided by 2.
      - If the current term is odd (and not 1), the next term is 3 * previous + 1.
    - The sequence ends once it reaches 1.

    Details and requirements:
    - The returned list must include all odd numbers encountered in the sequence, including the starting number and 1.
    - The returned list must be sorted in ascending order and contain unique values (no same values).
    - The function must validate input:
      - n must be an integer.
      - n must be positive (greater than zero).
      - If input is invalid, the function must raise appropriate exceptions (e.g., TypeError or ValueError).

    Args:
    - n (int): A positive integer starting value for the Collatz sequence.

    Returns:
    - List[int]: Sorted list of all unique odd numbers encountered in the Collatz sequence starting at n, including 1.

    Raises:
    - TypeError: If n is not an integer.
    - ValueError: If n is less than or equal to zero.

    Examples:
    - get_odd_collatz(1) => [1]
      (Sequence: [1])
    - get_odd_collatz(5) => [1, 5]
      (Sequence: [5, 16, 8, 4, 2, 1], odd numbers: 5 and 1)
    - get_odd_collatz(7) => [1, 5, 7, 11, 13, 17]
      (Sequence: [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])
    - get_odd_collatz(10) => [1, 5]
      (Sequence: [10, 5, 16, 8, 4, 2, 1])

    Notes:
    - The function must not allow floats (even if they represent whole numbers), strings, or other types — only integers are accepted n.
    - The returned list must be sorted and must not include no same values.
    - The sequence always ends at 1, per the Collatz conjecture assumption.
    """


def numerical_letter_grade(grades):
    """
    Given a list of floating point GPA values, write a function that converts each GPA to a related letter grade
    according to a custom grading table provided by the instructor.

    GPA to Letter Grade Conversion Table:
    - `4.0` => `"A+"`
    - `(3.7, 4.0)` => `"A"`
    - `(3.3, 3.7]` => `"A-"`
    - `(3.0, 3.3]` => `"B+"`
    - `(2.7, 3.0]` => `"B"`
    - `(2.3, 2.7]` => `"B-"`
    - `(2.0, 2.3]` => `"C+"`
    - `(1.7, 2.0]` => `"C"`
    - `(1.3, 1.7]` => `"C-"`
    - `(1.0, 1.3]` => `"D+"`
    - `(0.7, 1.0]` => `"D"`
    - `(0.0, 0.7]` => `"D-"`
    - `0.0` => `"E"`

    Details and requirements:
    - The function must accept a list of numeric GPA values and only accepts this (floats or ints).
    - The function must return a list of letter grades as strings corresponding to their GPA in the table.
    - The function must perform input validation:
      - Each element in the input list must be an `int` or `float`.
      - Each GPA must be in the range `[0.0, 4.0]`.
      - If a GPA is outside this range, the function must raise a `ValueError`.
      - If any element is not a numeric type, the function must raise a `TypeError`.
    - Floating-point precision should be handled gracefully (e.g., `3.699999999` should be treated correctly as under `3.7`).

    Args:
    - `grades (List[float])`: A list of GPA values between `0.0` and `4.0` inclusive.

    Returns:
    - `List[str]`: A list of letter grades corresponding to each GPA.

    Raises:
    - `TypeError`: If any element in the input list is not a numeric value.
    - `ValueError`: If any GPA is outside the threshold of `[0.0, 4.0]`.

    Examples:
    - `grade_equation([4.0, 3, 1.7, 2, 3.5])` => `["A+", "B", "C-", "C", "A-"]`
    - `grade_equation([0.0, 4.0])` => `["E", "A+"]`
    - `grade_equation([3.7, 3.3, 3.0, 2.7])` => `["A-", "B+", "B", "B-"]`
    - `grade_equation(["A", 2.0])` => `TypeError`
    - `grade_equation([-1.0])` => `ValueError`

    Notes:
    - You must use precise comparison logic to handle floating-point edge cases (e.g., values near thresholds).
    - The output list must keep the order of the input GPAs.
    """


def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already ate a certain number of carrots today. However, you need to eat more carrots to meet your daily requirement. You are also given the number of carrots currently available.

    Your task is to determine:
    - The total number of carrots you will have eaten after attempting to meet your need.
    - The number of carrots left after your attempt.

    If there are enough carrots remaining, you eat exactly as many as you need.  
    If not, you eat all remaining carrots, but your need is only partially fulfilled.

    Details and requirements:
    - Return a list of two integers:
    - Total number of carrots eaten after this meal.
    - Number of carrots left after the meal.
    - Inputs must be non-negative integers only.
    - The function must raise correct exceptions if any input is invalid.

    Args:
    - number (int): The number of carrots already eaten.
    - need (int): The number of carrots you need to eat now.
    - remaining (int): The number of carrots available currently.

    Returns:
    - List[int]: A list with two elements:
    1. Total number of carrots eaten after this meal.
    2. Number of carrots left after this meal.

    Raises:
    - TypeError: If any input is not an integer.
    - ValueError: If any input is negative.

    Examples:
    - eat(5, 6, 10) => [11, 4]    (5 already eaten, eats 6 more from 10, 4 remain)
    - eat(4, 8, 9) => [12, 1]     (4 + 8 = 12, 1 left)
    - eat(1, 10, 10) => [11, 0]   (1 + 10 = 11, nothing left)
    - eat(2, 11, 5) => [7, 0]     (2 + 5 = 7, not enough to meet need)
    - eat(10, 5, 0) => [10, 0]    (No carrots left to eat)
    - eat(0, 0, 0) => [0, 0]      (No eating needed or possible)

    Notes:
    - Inputs must be integers and floats, strings, or other types are not accepted.
    - All input values must be greater than or equal to zero.
    - The returned list will always contain two non-negative integers.

    Constrains:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000
    """


def poly(xs: list, x: float):
    """
    Your task is to implement a polynomial evaluating function taking a list of coefficients and a value at which the polynomial is to be evaluated. The function calculates the value of the polynomial at that point.

    Details and requirements:
    - The polynomial is expressed as:
        xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    - The input xs must be a list or tuple of numeric coefficients.
    - Coefficients can be integers, floats, or complex numbers.
    - The input x must be an integer, float, or complex number.
    - The function must raise appropriate exceptions for invalid inputs.
    - The function must return the result of the polynomial evaluation as a numeric value.

    Args:
    - xs (List[Union[int, float, complex]]): A list or tuple of polynomial coefficients, where xs[i] is the coefficient for the term with degree i.
    - x (Union[int, float, complex]): The value at which to evaluate the polynomial.

    Returns:
    - Union[int, float, complex]: The result of evaluating the polynomial at the given value of x.

    Raises:
    - TypeError: If xs is not a list or tuple.
    - TypeError: If any element of xs is not an int, float, or complex.
    - TypeError: If x is not an int, float, or complex.

    Examples:
    - poly([5], 10) => 5
    - poly([2, 3], 4) => 14
    - poly([1, 0, 2], 2) => 9
    - poly([-1, -2, -3], 2) => -17
    - poly([5, 4, 3, 2, 1], 2) => 57
    - poly([1 + 2j, 3], 1) => (4+2j)

    Notes:
    - Do not use libraries like numpy or sympy; use only base Python types and arithmetic.
    - The function should handle polynomials of arbitrary degree.
    - The function should reject invalid inputs like strings, dictionaries, booleans, None, and generators.
    - Empty coefficient list should return 0.
    - There should be support for complex numbers.
    """


def find_zero(coeffs: list):
    """
    Your task is to implement a function find_zero that receives a list of coefficients which is actually representing a polynomial and returns a single real root (zero) of that polynomial.

    Details and requirements:
    - The polynomial is expressed as
        coeffs[0] + coeffs[1] * x + coeffs[2] * x^2 + ... + coeffs[n] * x^n
      where coeffs[i] is the coefficient for the term x^i.
    - The input coeffs must be a list of numeric coefficients.
    - Only coefficients of type int or float are allowed; bool values must be rejected.
    - The list coeffs must contain an even number of coefficients, i.e., its length must be divisible by 2.
    - The polynomial must have at least two coefficients (degree ≥ 1).
    - Leading zeros in the coefficient list (coefficients of the lowest degree terms) are allowed and should be trimmed internally.
    - Trailing zeros (coefficients for the highest degree terms) are not allowed; they make the polynomial invalid.
    - The polynomial must not be empty or zeros all.
    - The function should find and return one real root of the polynomial if any exists.
    - If no real roots exist, raise a ValueError.

    Args:
    - coeffs (List[float]): A list of numeric coefficients with even length, where coeffs[i] corresponds to x^i.

    Returns:
    - float: One real root of the polynomial.

    Raises:
    - AttributeError: If coeffs is not a list.
    - ValueError: If the length of coeffs is not even.
    - ValueError: If the polynomial is empty, all coefficients are zero, or trailing zeros are present.
    - ValueError: If the polynomial degree is less than 1 (after trimming leading zeros).
    - TypeError: If any coefficient is not a number (int or float), or is NaN or infinite.
    - ValueError: If any coefficient is a boolean.
    - ValueError: If no real root is found.

    Examples:
    - find_zero([1, 2]) => approximately -0.5  (for 1 + 2x=0)
    - find_zero([-6, 11, -6, 1]) => one of 1.0, 2.0, 3.0  (roots of (x-1)(x-2)(x-3))
    - find_zero([-1, 0, 1]) => even argument check fails ValueError

    Notes:
    - The function must not allow bool coefficients, and give ValueError.
    - The function must raise TypeError if any coefficient is NaN or infinite.
    - The function should trim leading zeros before processing but give ValueError if trailing zeros are existing.
    - Use numerical methods (e.g., numpy.roots) to find roots and return only one real root.
    - If multiple real roots exist, returning any one real root is acceptable.
    - Do not return complex roots even if they exist.
    - The function should be able to handle large and small magnitude coefficients correctly.
    - The function should raise correct exceptions when invalid input is given.
    """


def sorted_list_sum(lst):
    """
    You are given a list of elements. You will implement a function called `sorted_list_sum(lst)` that returns a sorted list of only the strings with even lengths.

    The function must:
    - Accept a list as input.
    - Raise a TypeError if the input is not a list.
    - Raise a TypeError if any element of the list is not a string.

    The returned list should:
    - Include only the strings whose lengths are even (e.g., 2, 4, 6, ...).
    - Be sorted first by length in ascending order, and then alphabetically for strings of the same length.

    Examples:
    sorted_list_sum(["ab", "a", "abc", "abcd"]) => ["ab", "abcd"]
    sorted_list_sum(["cd", "ab", "ef", "xy"])   => ["ab", "cd", "ef", "xy"]
    sorted_list_sum(["a", "abc", "abcde"])     => []

    Ensure strict input type validation for both the list and its elements.
    """


def strongest_extension(class_name, extensions):
    """
    You are given a class name and a list of extension names. You must implement a function called `Strongest_Extension(class_name, extensions)` that returns a string in the following format:

    <class_name>.<strongest_extension>

    The strongest extension is determined by the "strength" of each extension, where:
    - Each uppercase letter contributes +1,
    - Each lowercase letter contributes -1,
    - Digits, symbols, or non-alphabetic characters contribute 0.

    The extension with the highest total strength is selected. If there is a tie (same strength), return the extension that appears first in the list.

    Constraints:
    - `class_name` must be a string. If not, raise an AttributeError.
    - `extensions` must be a list of strings. If not, raise a TypeError.
    - If the list `extensions` is empty, raise a ValueError.

    Example:
    Strongest_Extension("my_class", ["AA", "Be", "CC"])
    # Returns: "my_class.AA"

    Explanation:
    - "AA" has strength +2
    - "Be" has strength 0
    - "CC" also has strength +2
    - Since "AA" and "CC" are tied, "AA" is chosen as it appears first.
    """


def solve(n: int) -> str:
    """
    Write a function `solve(n)` that takes a single integer input `n` and returns a string representing the binary form of the sum of its digits.

    Function Signature:
    def solve(n: int) -> str

    Input:
    - A single integer `n` where:
        - 0 <= n <= 10000

    Output:
    - Return the binary representation (as a string) of the sum of the digits of `n`.

    Constraints:
    - If the input is not an integer, raise a TypeError with the message "Input must be an integer."
    - If the input is less than 0 or greater than 10000, raise a ValueError with the message "Input must be between 0 and 10000 inclusive."

    Examples:
    - solve(123)   => "110"     # 1+2+3 = 6 → binary: 110
    - solve(9999)  => "100100"  # 9+9+9+9 = 36 → binary: 100100
    - solve(0)     => "0"       # sum = 0 → binary: 0
    - solve(1000)  => "1"       # 1+0+0+0 = 1 → binary: 1
    """


def valid_date(date_str):
    """
    You must implement a function called `valid_date(date_str)` that returns True if the input string is a valid date in the format
    MM-DD-YYYY, and False otherwise.

    Rules:
    - The string must be in the exact format MM-DD-YYYY,
    - MM must be between 01 and 12,
    - DD must be a valid day for the given month, accounting for leap years,
    - YYYY must be between 0001 and 9999,
    - Separators must be hyphens only; other formats like slashes or dots are invalid,
    - The input must not contain letters, whitespace, or extra symbols.

    Exceptions:
    - If the input is not a string, the function must raise an AttributeError.
    """


def is_palindrome(s):
    """
    You must implement a function:
    def is_palindrome(s):

    Rules:
    - The function returns True if the input string is a palindrome.
    - The comparison must be case-sensitive.
    - All characters must be preserved and considered as-is (e.g., punctuation, whitespace, symbols).
    - Raise TypeError for any input that is not a string.
    """


def reverse_delete(s, c):
    """
    You will implement a function named `reverse_delete(s, c)` that:
    - Removes all characters from string s that are present in string c,
    - Returns a tuple (new_string, is_palindrome),
    - Where is_palindrome is True if the remaining string is a palindrome.

    Note: Both deletion and palindrome checks are case-sensitive.
    """


def get_closest_vowel(word):
    """
    You will implement a function called `get_closest_vowel(word)` that returns the rightmost vowel in a word that is surrounded
    by consonants on both sides (i.e., the characters directly before and after the vowel must not be vowels).

    The function must:
    - Return the rightmost surrounded vowel (case preserved),
    - Return "" if no such vowel exists,
    - Raise TypeError if the input is not a string.

    Vowels are defined as: a, e, i, o, u (both uppercase and lowercase).
    """


def decimal_to_binary(n):
    """
    You are to implement a function named `decimal_to_binary(n)` that takes a non-negative integer and returns its binary
    representation wrapped in the string format "db<binary>db".

    Requirements:
    - Input must be a non-negative integer.
    - Raise a TypeError for non-integer inputs.
    - Raise a ValueError for negative integers.
    - The binary output should include only 0s and 1s and must be wrapped with "db" at both ends.

    Args:
    - n (int): A non-negative integer to convert.

    Returns:
    - str: A string of the form "db<binary_digits>db" representing the binary form of the input.

    Examples:
    - decimal_to_binary(0) => "db0db"
    - decimal_to_binary(5) => "db101db"
    - decimal_to_binary(255) => "db11111111db"

    Raises:
    - TypeError: If the input is not an integer.
    - ValueError: If the input is negative.

    Notes:
    - The binary conversion must preserve all binary digits exactly.
    - The output must include "db" at both the beginning and the end.
    - Invalid types such as float, string, list, etc., should raise an error.
    """


def intersection(interval1, interval2):
    """
    You are to implement a function called `intersection(interval1, interval2)` that determines whether two intervals intersect,
    and if they do, whether the length of the overlapping part is a prime number.

    Each interval is represented as a tuple of two integers (start, end). The function must work regardless of the input order
    (e.g., (5, 1) is the same as (1, 5)).

    Return:
    - "YES" if the intervals overlap and the overlap length is a prime number.
    - "NO" otherwise.

    Input Validation:
    - Raise TypeError if the input is not a tuple.
    - Raise ValueError if the tuple does not have exactly 2 elements.
    - Raise TypeError if any element of the tuple is not an integer.

    Args:
    - interval1 (Tuple[int, int]): First interval (start, end).
    - interval2 (Tuple[int, int]): Second interval (start, end).

    Returns:
    - str: "YES" or "NO" based on the intersection and prime overlap length.

    Examples:
    - intersection((1, 5), (3, 7)) => "YES"  (overlap is [3, 4, 5], length 3 which is prime)
    - intersection((0, 2), (3, 5)) => "NO"   (no overlap)
    - intersection((2, 2), (2, 2)) => "NO"   (overlap length 1, not prime)
    - intersection((5, 1), (0, 3)) => "NO"   (normalized to (1,5) and (0,3); overlap [1,2], length 2 → prime → "YES")

    Notes:
    - Input order does not matter. Normalize intervals internally.
    - Use standard methods to check for primality of overlap length.
    - Intervals include both start and end values (closed intervals).
    """


def words_in_sentence(sentence):
    """
    You are given a sentence containing words separated by spaces. You will implement a function called `words_in_sentence(sentence)` that returns a string containing only the words that have a prime number of characters.

    The output words must:
    - Be preserved in their original order from the input sentence,
    - Contain only alphabetic characters (skip any with digits or punctuation),
    - Be selected only if their length is a prime number,
    - Ignore any leading, trailing, or extra whitespace between words.

    Input validation:
    - Accept only string input,
    - Raise a TypeError for any non-string input.

    Returns:
    - A space-separated string of valid words meeting the criteria above.

    Examples:
    - words_in_sentence("this is an example!") => "this is"
    - words_in_sentence("  prime   digits123   okay ") => "prime okay"
    - words_in_sentence(12345) => raises TypeError
    - words_in_sentence("1two three4") => ""

    Notes:
    - The function should not modify words that pass validation,
    - Use built-in `str.isalpha()` for alphabetic filtering,
    - Consider 2, 3, 5, 7, 11, etc. as prime lengths.
    """
