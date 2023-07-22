import unittest

from src.app import App

class TestApp(unittest.TestCase):

    # -------------------
    # App
    # -------------------

    # Positive

    def test_run_arg_string_ascii(self):
        args = 'tests/data/text_data.txt'
        expected = [['line'], ['line', 'line', 'line'], None, ['line'], None, ['in']]
        with App(args) as file:
            actual = [form_line for form_line in file]

        self.assertEqual(len(expected), len(actual))
        for idx, form_line_exp in enumerate(expected):
            self.assertEqual(form_line_exp, actual[idx])

    # Negative

    def test_run_arg_int(self):
        args = 12345

        with self.assertRaises(Exception) as context:
            with App(args) as file:
                actual = [form_line for form_line in file]
        self.assertIn('input was not str ascii', str(context.exception))

    def test_run_arg_none(self):
        args = None
        
        with self.assertRaises(Exception) as context:
            with App(args) as file:
                actual = [form_line for form_line in file]
        self.assertIn('input was not str ascii', str(context.exception))

    def test_run_arg_not_ascii(self):
        args = 'fewfó'
        
        with self.assertRaises(Exception) as context:
            with App(args) as file:
                actual = [form_line for form_line in file]
        self.assertIn('input was not str ascii', str(context.exception))

    def test_run_arg_empty(self):
        with self.assertRaises(Exception) as context:
            with App() as file:
                actual = [form_line for form_line in file]
        self.assertIn(' missing 1 required positional argument', str(context.exception))

    # -------------------
    # format_words
    # -------------------

    # Positive

    def test_format_words_arg_string_ascii_2(self):
        word = 'word'
        args = [word] * 2
        expected = '[word word]'
        actual = App.format_words(args)

        self.assertEqual(expected, actual)

    def test_format_words_arg_string_ascii_10(self):
        word = 'word'
        args = [word] * 10
        expected = '[word word word word word word word word word word]'
        actual = App.format_words(args)

        self.assertEqual(expected, actual)

    def test_format_words_arg_string_ascii_20(self):
        word = 'word'
        args = [word] * 20
        expected = '[word word word word word word word word word word word word word word word word word word word word]'
        actual = App.format_words(args)

        self.assertEqual(expected, actual)

    # Negative

    def test_format_words_arg_int(self):
        args = 13434
        
        with self.assertRaises(Exception) as context:
            actual = App.format_words(args)
        self.assertIn('input was not a list of str', str(context.exception))

    def test_format_words_arg_none(self):
        args = None
        
        with self.assertRaises(Exception) as context:
            actual = App.format_words(args)
        self.assertIn('input was not a list of str', str(context.exception))

    def test_format_words_arg_utf_8_list(self):
        word = 'wórd'
        args = [word] * 2
        
        with self.assertRaises(Exception) as context:
            actual = App.format_words(args)
        self.assertIn('input was not a list of str', str(context.exception))

    def test_format_words_arg_str_ascii(self):
        args = 'word'
        
        with self.assertRaises(Exception) as context:
            actual = App.format_words(args)
        self.assertIn('input was not a list of str', str(context.exception))

    def test_format_words_arg_str_utf_8(self):
        args = 'wórd£$£%£$'
        
        with self.assertRaises(Exception) as context:
            actual = App.format_words(args)
        self.assertIn('input was not a list of str', str(context.exception))

    def test_format_words_arg_empty(self):
        with self.assertRaises(Exception) as context:
            actual = App.format_words()
        self.assertIn('missing 1 required positional argument', str(context.exception))