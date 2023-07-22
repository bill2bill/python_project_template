from src.lib.util import Util
from src.lib.file_io import FileIo
from src.lib.text_parser import TextParser

class App(FileIo):
    """
    SeekerShout application.

    Print formatted lines in a file where words in the line contain a substring.

    ...

    Methods
    -------
    run(text):
        Run the application.
    """

    def __init__(self, full_file_path):
        """
        Constructs all the necessary attributes for the app object.

        Parameters
        ----------
            full_file_path : str
                Files full path
        """
        super().__init__(full_file_path)
        
        try:
            self.search_term = FileIo.file_last_line(full_file_path)
        except Exception as e:
            raise Exception(Util.format_error('could not extract words from the line', 'src.app.__init__', full_file_path, e))
        
    def __iter__(self):
        super().__iter__()
        return self

    def __next__(self):
        line = super().__next__()
        try:
            words = TextParser.extract_words(line)
            if TextParser.any_words_contain_substring(words, self.search_term):
                return words
            return None
        except Exception as e:
            raise Exception(Util.format_error('could not extract words from the line', 'src.app.__next__', line, e))
    
    def format_words(words):
        """
        Formats a list of words.

        Joins the list of words with a single space, surrounded by square brackets.

        Example: [word word word]

        Returns
        -------
        str
        """

        if Util.is_list_of_str(words):
            return f'[{" ".join(words)}]'
        
        raise Exception(Util.format_error('input was not a list of str', 'src.app.format_words', words, None))
    
