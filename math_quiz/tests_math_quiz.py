import unittest
from math_quiz import Rand_Int, Rand_Operator, Calculation


class TestMathGame(unittest.TestCase):

    def test_Rand_Int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Rand_Int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Rand_Operator(self):
        # Test if the random operators are valid

        valid_operators = ['+', '-', '*']
        rand_op = Rand_Operator()
        self.assertTrue(rand_op, valid_operators)

    def test_Calculation(self):
        # Checking if our calculations are correct
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (2, 4, '*', '2 * 4', 8),
            (9, 3, '-', '9 - 3', 6),
            (-1, -3, '+', '-1 + -3', -4)

        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            result = Calculation(num1, num2, operator)
            self.assertEqual(result, (expected_problem, expected_answer), f"Failed for {num1}{operator}{num2}")
            # assertEqual is used to compare the result to the expected answer


if __name__ == "__main__":
    unittest.main()
