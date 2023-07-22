import unittest

from src.lib.file_io import FileIo

class TestFileIo(unittest.TestCase):

    # -------------------
    # file_lines_iter
    # -------------------

    # Positive

    def test_file_lines_iter_arg_string_ascii(self):
        args = 'tests/data/text_data.txt'
        expected = ['line1\n', "line23423line2/'].];'[];line2\n", 'random1\n', 'line3\n', 'random2\n', 'in']
        with FileIo(args) as file:
            actual = [line for line in file]

        self.assertEqual(len(expected), len(actual))
        for idx, form_line_exp in enumerate(expected):
            self.assertEqual(form_line_exp, actual[idx])

    # Negative

    def test_file_lines_iter_arg_int(self):
        args = 12345

        with self.assertRaises(Exception) as context:
            with FileIo(args) as file:
                actual = [line for line in file]
        self.assertIn('input was not str ascii', str(context.exception))

    def test_file_lines_iter_arg_none(self):
        args = None

        with self.assertRaises(Exception) as context:
            with FileIo(args) as file:
                actual = [line for line in file]
        self.assertIn('input was not str ascii', str(context.exception))

    def test_file_lines_iter_arg_not_ascii(self):
        args = 'tests/data/text_data£$£".txt'

        with self.assertRaises(Exception) as context:
            with FileIo(args) as file:
                actual = [line for line in file]
        self.assertIn('input was not str ascii', str(context.exception))

    def test_file_lines_iter_arg_empty(self):
        with self.assertRaises(Exception) as context:
            with FileIo() as file:
                actual = [line for line in file]
        self.assertIn('missing 1 required positional argument', str(context.exception))

    def test_file_lines_iter_arg_missing_file(self):
        args = 'tests/data/missing_data.txt'
        
        with self.assertRaises(Exception) as context:
            with FileIo(args) as file:
                actual = [line for line in file]
        self.assertIn('could not open file', str(context.exception))

    def test_file_lines_iter_arg_corrupt_file(self):
        args = 'tests/data/bad_data.txt'
        
        with self.assertRaises(Exception) as context:
            with FileIo(args) as file:
                actual = [line for line in file]
        self.assertIn('corrupt file', str(context.exception))

    # -------------------
    # file_last_line
    # -------------------

    # Positive

    def test_file_last_line_arg_string_ascii(self):
        args = 'tests/data/text_data.txt'
        expected = 'in'
        actual = FileIo.file_last_line(args)

        self.assertEqual(expected, actual)

    def test_file_last_line_arg_missing_file(self):
        args = 'tests/data/missing_data.txt'
        expected = ''
        actual = FileIo.file_last_line(args)

        self.assertEqual(expected, actual)

    # Negative

    def test_file_last_line_arg_int(self):
        args = 12345

        with self.assertRaises(Exception) as context:
            FileIo.file_last_line(args)
        self.assertIn('could not execute command tail -n 1 on chosen file', str(context.exception))

    def test_file_last_line_arg_none(self):
        args = None

        with self.assertRaises(Exception) as context:
            FileIo.file_last_line(args)
        self.assertIn('could not execute command tail -n 1 on chosen file', str(context.exception))

    def test_file_last_line_arg_not_ascii(self):
        args = 'tests/data/text_data£$$.txt'

        with self.assertRaises(Exception) as context:
            FileIo.file_last_line(args)
        self.assertIn('could not execute command tail -n 1 on chosen file', str(context.exception))

    def test_file_last_line_arg_empty(self):
        with self.assertRaises(Exception) as context:
            FileIo.file_last_line()
        self.assertIn(' missing 1 required positional argument', str(context.exception))

    def test_file_last_line_arg_corrupt_file(self):
        args = 'tests/data/bad_data.txt'

        with self.assertRaises(Exception) as context:
            FileIo.file_last_line(args)
        self.assertIn('could not execute command tail -n 1 on chosen file', str(context.exception))