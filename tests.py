import unittest
from task1 import fib1, fib_recursive
from task2 import counter
from task3 import sum_with_factorial
from task4 import skipped_num
from task5 import is_or_not
from task6 import sudoku, printt
from task7 import without_one

class tests(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib1(3), 2)
        self.assertEqual(fib1(0), 0)
        self.assertEqual(fib1(1), 1)
        self.assertEqual(fib1(2), 1)
        self.assertEqual(fib1(6), 8)

        self.assertEqual(fib_recursive(3), 2)
        self.assertEqual(fib_recursive(0), 0)
        self.assertEqual(fib_recursive(1), 1)
        self.assertEqual(fib_recursive(2), 1)
        self.assertEqual(fib_recursive(6), 8)

    def test_counter(self):
        vec = [63, 55, 11, 10, 10, 9, 1]
        self.assertEqual(counter(vec), 6)
        vec1 = [63, 55, 11, 10, 9, 1]
        self.assertEqual(counter(vec1), 6)

    def test_is_or_not(self):
        matrix = [[0, 2, 3, 10, 15], [2, 4, 11, 16, 17], [3, 7, 12, 17, 30], [6, 7, 30, 60, 85], [7, 13, 31, 75, 90]]
        self.assertEqual(is_or_not(matrix, 0), 'YES')
        self.assertEqual(is_or_not(matrix, 90), 'YES')
        self.assertEqual(is_or_not(matrix, 10), 'YES')
        self.assertEqual(is_or_not(matrix, 7), 'YES')
        self.assertEqual(is_or_not(matrix, 12), 'YES')
        self.assertEqual(is_or_not(matrix, 4), 'YES')
        self.assertEqual(is_or_not(matrix, 35), None)

    def test_sum_with_factorial(self):
        self.assertEqual(sum_with_factorial(1), 1)
        self.assertEqual(sum_with_factorial(2), 1.5)
        self.assertEqual(sum_with_factorial(3), 1.67)
        self.assertEqual(sum_with_factorial(4), 1.71)

    def test_skipped_num(self):
        vec = [0, 1, 4, 6, 3, 2]
        self.assertEqual(skipped_num(vec), 5)
        vec1 = [1, 2, 3]
        self.assertEqual(skipped_num(vec1), 0)

    def test_sudoku(self):
        matrix = [[2, 3, 8, 9, 6, 5, 7, 1, 4], [7, 5, 9, 4, 1, 3, 6, 8, 2], [4, 1, 6, 2, 7, 8, 9, 5, 3],
                  [9, 4, 5, 1, 3, 6, 2, 7, 8], [6, 8, 7, 5, 2, 4, 1, 3, 9], [3, 2, 1, 8, 9, 7, 4, 6, 5],
                  [1, 6, 2, 3, 5, 9, 8, 4, 7], [5, 7, 4, 6, 8, 2, 3, 9, 1], [8, 9, 3, 7, 4, 1, 5, 2, 6]]
        printt(matrix)
        print()
        self.assertEqual(sudoku(matrix, 3), 1)
        matrix1 =[[3, 7, 4, 9, 6, 3, 1, 5, 8], [3, 5, 1, 4, 8, 2, 6, 7, 9], [8, 9, 6, 5, 7 , 1, 2, 4, 3],
                  [9, 4, 2, 1, 5, 8, 3, 6, 7], [6, 1, 7, 3, 2, 9, 5, 8, 4], [5, 3, 8, 6, 4, 7, 9, 2, 1],
                  [7, 6, 9, 2, 1, 4, 8, 3, 5], [1, 8, 5, 7, 3, 6, 4, 9, 2], [4, 2, 3, 8, 9, 5, 7, 1, 6]]
        printt(matrix1)
        self.assertEqual(sudoku(matrix1, 3), 'error!!!')

    def test_without_one(self):
        vec = [2, 3, 4, 5, 10]
        self.assertEqual(without_one(vec), [600, 400, 300, 240, 120])