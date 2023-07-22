from src.lib.sys import Sys
from src.lib.util import Util
from src.lib.text_parser import TextParser

class FileIo:
    """
    A class to represent an interface to files on the system.

    ...

    Attributes
    ----------
    full_file_path : str
        Files full path

    Methods
    -------
    file_lines_iter():
        Created an iterator for lines in a file.
    file_last_line():
        Captures the last line in a file.
    """

    def __init__(self, full_file_path):
        """
        Constructs all the necessary attributes for the file_io object.

        Parameters
        ----------
            full_file_path : str
                Files full path
        """

        if TextParser.is_ascii(full_file_path):
            self.full_file_path = full_file_path
        else:
            raise Exception(Util.format_error('input was not str ascii', 'src.lib.file_io.__init__', full_file_path, None))
        
    def __enter__(self):
        try:
            self.iter = open(self.full_file_path, 'r', encoding='ascii')
            return self
        except Exception as e:
            raise Exception(Util.format_error('could not open file', 'src.lib.file_io.__enter__', self.full_file_path, e))
        
    def __exit__(self, exc_type, exc_value, tb):
        self.iter.close()

    def __iter__(self):
        """
        Iterates over a files lines, using ASCII encoding.
        
        """

        return self
        
    def __next__(self):
        try:
            return next(self.iter)
        except UnicodeDecodeError as e:
            raise Exception(Util.format_error('corrupt file', 'src.lib.file_io.__next__', self.full_file_path, e))

    def file_last_line(full_file_path):
        """
        Retrieves the last line in a file.

        Returns
        -------
        str
        """

        try:
            return Sys.run(['tail', '-n', '1', full_file_path])
        except Exception as e:
            raise Exception(Util.format_error('could not execute command tail -n 1 on chosen file', 'src.lib.file_io.file_last_line', full_file_path, e))