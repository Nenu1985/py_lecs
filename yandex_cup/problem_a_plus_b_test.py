import argparse
import logging
from unittest.mock import Mock, patch
import os
import unittest
import sys
from problem_a_plus_b import get_input_values
import problem_a_plus_b

from contextlib import redirect_stdout


class TestMainModule(unittest.TestCase):
    def setUp(self) -> None:
        pass


    @patch('problem_a_plus_b.get_input_values', return_value=[
        '2*2=4',
        '25*25=625',
        '10+10=20',
    ])
    def test_1_case_main(self, input):
        ans = problem_a_plus_b.main()
        self.assertEqual(ans, 10)

    @patch('problem_a_plus_b.get_input_values', return_value=[
        '2*2=5',
    ])
    def test_2_case_main(self, input):
        ans = problem_a_plus_b.main()
        self.assertEqual(ans, 0)

    @patch('problem_a_plus_b.get_input_values', return_value=[
        '2*2=4',
    ])
    def test_3_case_main(self, input):
        ans = problem_a_plus_b.main()
        self.assertEqual(ans, -1)

    @patch('problem_a_plus_b.get_input_values', return_value=[
        'z*z=y1',
    ])
    def test_4_case_main(self, input):
        ans = problem_a_plus_b.main()
        self.assertEqual(ans, 36)

    @patch('problem_a_plus_b.get_input_values', return_value=[
        'f*f=e1',
    ])
    def test_5_case_main(self, input):
        ans = problem_a_plus_b.main()
        self.assertEqual(ans, 16)

    @patch('problem_a_plus_b.get_input_values', return_value=[
        'f*f=e1',
        'z*z=y1',
        '2*2=4',
    ])
    def test_5_case_main(self, input):
        ans = problem_a_plus_b.main()
        self.assertEqual(ans, 0)
    # @patch('problem_a_plus_b.get_input_values', return_value=[

    # ])
    # def test_6_case_main(self, input):
    #     ans = problem_a_plus_b.main()
    #     self.assertEqual(ans, 0)
if __name__ == '__main__':
    unittest.main()
