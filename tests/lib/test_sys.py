import unittest

from src.lib.sys import Sys

class TestSys(unittest.TestCase):

    # -------------------
    # run
    # -------------------

    # Positive

    def test_run_arg_string_ascii_tail(self):
        args = ['tail', '-n', '1', 'tests/data/text_data_sml.txt']
        expected = 'kermit'
        actual = Sys.run(args)

        self.assertEqual(expected, actual)

    # Negative

    def test_run_arg_int(self):
        args = 13434
        
        with self.assertRaises(Exception) as context:
            actual = Sys.run(args)
        self.assertIn('input was not a list of strings', str(context.exception))

    def test_run_arg_none(self):
        args = None
        
        with self.assertRaises(Exception) as context:
            actual = Sys.run(args)
        self.assertIn('input was not a list of strings', str(context.exception))

    def test_run_arg_not_ascii(self):
        args = ['ll£$&*"()']
        
        with self.assertRaises(Exception) as context:
            actual = Sys.run(args)
        self.assertIn('input was not a list of strings', str(context.exception))

    def test_run_arg_str_ascii(self):
        args = 'll'
        
        with self.assertRaises(Exception) as context:
            actual = Sys.run(args)
        self.assertIn('input was not a list of strings', str(context.exception))

    def test_run_arg_str_utf_8(self):
        args = 'll£"()$*"'
        
        with self.assertRaises(Exception) as context:
            actual = Sys.run(args)
        self.assertIn('input was not a list of strings', str(context.exception))

    def test_run_arg_empty(self):
        with self.assertRaises(Exception) as context:
            actual = Sys.run()
        self.assertIn('missing 1 required positional argument', str(context.exception))