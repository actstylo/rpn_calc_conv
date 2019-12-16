import unittest
from infix_to_rpn import process_input, shunting


class TestInfixPpn(unittest.TestCase):

    def test_process_input(self):
        input_value = '3 * 4 + ( 6 - 9 ) ^ 2'
        expected_output = [('NUMBER', '3'), ('*', (3, 'L')), ('NUMBER', '4'), ('+', (2, 'L')), ('(', (9, 'L')), 
                           ('NUMBER', '6'), ('-', (2, 'L')), ('NUMBER', '9'), (')', (0, 'L')), ('^', (4, 'R')), ('NUMBER', '2')]
        self.assertEqual(process_input(input_value), expected_output)

    def test_shunting(self):
        input_value = [('NUMBER', '3'), ('*', (3, 'L')), ('NUMBER', '4'), ('+', (2, 'L')), ('(', (9, 'L')),
                           ('NUMBER', '6'), ('-', (2, 'L')), ('NUMBER', '9'), (')', (0, 'L')), ('^', (4, 'R')), ('NUMBER', '2')]
        expected_output = '3 4 * 6 9 - 2 ^ +'
        self.assertEqual(shunting(input_value), expected_output)


