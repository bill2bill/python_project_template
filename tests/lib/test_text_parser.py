import unittest

from src.lib.text_parser import TextParser

class TestTextParser(unittest.TestCase):

    # -------------------
    # extract_words
    # -------------------

    # Positive

    def test_extract_words_arg_string_ascii_empty(self):
        args = '                 3'
        expected = []
        actual = [word for word in TextParser.extract_words(args)]

        self.assertEqual(len(expected), len(actual))
        for idx, form_line_exp in enumerate(expected):
            self.assertEqual(form_line_exp, actual[idx])

    def test_extract_words_arg_string_ascii_small(self):
        args = '                    _get9_'
        expected = ['get']
        actual = [word for word in TextParser.extract_words(args)]

        self.assertEqual(len(expected), len(actual))
        for idx, form_line_exp in enumerate(expected):
            self.assertEqual(form_line_exp, actual[idx])

    def test_extract_words_arg_string_ascii_medium(self):
        args = '1111tired1111of1111sitting1111'
        expected = ['tired', 'of', 'sitting']
        actual = [word for word in TextParser.extract_words(args)]

        self.assertEqual(len(expected), len(actual))
        for idx, form_line_exp in enumerate(expected):
            self.assertEqual(form_line_exp, actual[idx])

    def test_extract_words_arg_string_ascii_large(self):
        args = '908^)-234 923this-++-23is./<.";][}"another-=&^533-43test/\'\]/.\]3oh34/\/    /\/joy'
        expected = ['this', 'is', 'another', 'test', 'oh', 'joy']
        actual = [word for word in TextParser.extract_words(args)]

        self.assertEqual(len(expected), len(actual))
        for idx, form_line_exp in enumerate(expected):
            self.assertEqual(form_line_exp, actual[idx])

    # Negative

    def test_extract_words_arg_int(self):
        args = 12345

        with self.assertRaises(Exception) as context:
            TextParser.extract_words(args)
        self.assertIn('text is not an ascii encoded str', str(context.exception))

    def test_extract_words_arg_none(self):
        args = None

        with self.assertRaises(Exception) as context:
            TextParser.extract_words(args)
        self.assertIn('text is not an ascii encoded str', str(context.exception))

    def test_extract_words_arg_not_ascii(self):
        args = '1111tired1111óf1111sitting1111'

        with self.assertRaises(Exception) as context:
            TextParser.extract_words(args)
        self.assertIn('text is not an ascii encoded str', str(context.exception))

    def test_extract_words_arg_empty(self):
        with self.assertRaises(Exception) as context:
            TextParser.extract_words()
        self.assertIn('missing 1 required positional argument', str(context.exception))

    # -------------------
    # any_words_contain_substring
    # -------------------

    # Positive

    def test_any_words_contain_substring_arg_string_ascii_true(self):
        args = [['word', 'word', 'random'], 'ord']
        actual = TextParser.any_words_contain_substring(*args)

        self.assertTrue(actual)

    def test_any_words_contain_substring_arg_string_ascii_false(self):
        args = [['word', 'word', 'random'], 'bob']
        actual = TextParser.any_words_contain_substring(*args)

        self.assertFalse(actual)

    # Negative

    def test_any_words_contain_substring_arg_list_int(self):
        args = [12345, 'bob']

        with self.assertRaises(Exception) as context:
            TextParser.any_words_contain_substring(*args)
        self.assertIn('words is not a list of str', str(context.exception))

    def test_any_words_contain_substring_arg_term_int(self):
        args = [['word', 'word', 'random'], 12345]

        with self.assertRaises(Exception) as context:
            TextParser.any_words_contain_substring(*args)
        self.assertIn('text is not an ascii encoded str', str(context.exception))

    def test_any_words_contain_substring_arg_list_none(self):
        args = [None, 'bob']

        with self.assertRaises(Exception) as context:
            TextParser.any_words_contain_substring(*args)
        self.assertIn('words is not a list of str', str(context.exception))

    def test_any_words_contain_substring_arg_term_none(self):
        args = [['word', 'word', 'random'], None]

        with self.assertRaises(Exception) as context:
            TextParser.any_words_contain_substring(*args)
        self.assertIn('text is not an ascii encoded str', str(context.exception))

    def test_any_words_contain_substring_arg_list_not_ascii(self):
        args = [['word£"$)*"£&%', 'word', 'random£"%£"'], 'bob']

        with self.assertRaises(Exception) as context:
            TextParser.any_words_contain_substring(*args)
        self.assertIn('words is not a list of str', str(context.exception))

    def test_any_words_contain_substring_arg_term_not_ascii(self):
        args = [['word', 'word', 'random'], 'bob£$$']

        with self.assertRaises(Exception) as context:
            TextParser.any_words_contain_substring(*args)
        self.assertIn('text is not an ascii encoded str', str(context.exception))

    def test_any_words_contain_substring_arg_empty(self):
        with self.assertRaises(Exception) as context:
            TextParser.extract_words()
        self.assertIn('missing 1 required positional argument', str(context.exception))

    # -------------------
    # is_ascii
    # -------------------

    # Positive

    def test_is_ascii_arg_string_ascii(self):
        args = 'some random text?'
        actual = TextParser.is_ascii(args)

        self.assertTrue(actual)

    def test_is_ascii_arg_string_utf_8(self):
        args = 'some random text?£)($*")'
        actual = TextParser.is_ascii(args)

        self.assertFalse(actual)

    def test_is_ascii_arg_string_int(self):
        args = 324532532
        actual = TextParser.is_ascii(args)

        self.assertFalse(actual)

    def test_is_ascii_arg_string_none(self):
        args = None
        actual = TextParser.is_ascii(args)

        self.assertFalse(actual)

    # Negative

    def test_is_ascii_arg_empty(self):
        with self.assertRaises(Exception) as context:
            TextParser.is_ascii()
        self.assertIn('missing 1 required positional argument', str(context.exception))