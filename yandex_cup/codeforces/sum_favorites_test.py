from unittest.mock import Mock, patch
import unittest


import sum_favorites

from my_decorators import stopwatch

class TestMainModule(unittest.TestCase):
    def setUp(self) -> None:
        pass

    # def test_1_case_sum(self, input):
    #     ans = sum_favorites.get_sum_favirites(5, [1, 4, 6])
    #     self.assertEqual(ans, 5)

    def test_2_case_sum(self):
        ans = sum_favorites.get_sum_fast(5, [1, 4, 6])
        self.assertEqual(ans, 5)
    def test_3_case_sum(self):
        ans = sum_favorites.get_sum_fast(3, [2, 3, 4])
        self.assertEqual(ans, -4)

    def test_4_case_sum(self):
        ans = sum_favorites.get_sum_favirites_lambda(100000, [1, 2, 3])
        self.assertEqual(ans, 5000049988)

    def test_5_case_sum(self):
        ans = sum_favorites.get_sum_fast(1, [2, 3, 4])
        self.assertEqual(ans, 1)
    def test_6_case_sum(self):
        ans = sum_favorites.get_sum_fast(1, [1, 3, 4])
        self.assertEqual(ans, -1)
    def test_7_case_sum(self):
        ans = sum_favorites.get_sum_fast(4, [1, 3, 4])
        self.assertEqual(ans, -6)
    # @patch('sum_favorites.get_input_values', return_value=[
    #     (3, 5, [1, 4, 6]),
    #     (3,  3, [2, 3, 4]),
    #     (3, 10000, [1, 2, 3])
    # ])
    # def test_1_case_main(self, input):
    #     ans = sum_favorites.main()
    #     self.assertEqual(ans, '5\n-4\n50004988\n')

if __name__ == '__main__':
    unittest.main()
