import re

from src.lib.util import Util

class TextParser:
    """
    A class to parse text data.

    ...

    Methods
    -------
    extract_words(text):
        Retrieves all words in the text, ignoring any symbols.
    is_ascii(text):
        Identifies if an input is ASCII text characters.
    """

    def extract_words(text):
        """
        Retrieves all words in the text, ignoring any symbols.

        Parameters
        ----------
            text : str
                Text to extract words from

        Returns
        -------
        List<str>
        """

        if not TextParser.is_ascii(text):
            raise Exception(Util.format_error('text is not an ascii encoded str', 'src.lib.text_parser.extract_words', text, None))
        
        words = re.findall(r'[a-zA-Z]+', text)

        return words
    
    def any_words_contain_substring(words, search_term):
        """
        Identifies if an input is ASCII text characters.

        Parameters
        ----------
            words : List<str>
                List of words to inspect for a substring specified as search_term
            search_term : str
                substring to search for in words

        Returns
        -------
        bool
        """

        if not Util.is_list_of_str(words):
            raise Exception(Util.format_error('words is not a list of str', 'src.lib.text_parser.any_words_contain_substring', words, None))
        
        if not TextParser.is_ascii(search_term):
            raise Exception(Util.format_error('text is not an ascii encoded str', 'src.lib.text_parser.any_words_contain_substring', search_term, None))
        
        for word in words:
            if search_term in word:
                return True
        
        return False

    def is_ascii(text):
        """
        Identifies if an input is ASCII text characters.

        Parameters
        ----------
            text : str
                Text validate if encoding is ASCII

        Returns
        -------
        bool
        """

        try:
            return text.isascii()
        except:
            return False