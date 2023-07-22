class Util:
    """
    A class to help other classes.

    ...

    Methods
    -------
    empty(text):
        Retrieves all words in the text, ignoring any symbols.
    """

    def format_error(message, location, data, exception):
        """
        Formats errors messages for consistency.

        Parameters
        ----------
            message : str
                Message describing the current problem
            location : str
                Where the error took place. i.e. src.lib.util.format_error
            data : any
                Data given to the failed function
            exception : Optional<Exception>
                Previous exception thrown

        Returns
        -------
        str
        """
        
        dtype = type(data)
        try:
            length = len(data)
        except:
            length = None 

        try:
            is_ascii = message.isascii()
        except:
            is_ascii = False

        if is_ascii:
            return f'ERROR: {message}, LOCATION: {location}, DTYPE: {dtype}, LENGTH: {length}'
        else:
            dtype = type(message)
            try:
                length = len(message)
            except:
                length = None 
            raise Exception(f'ERROR: could not format error message as input was not str ascii, LOCATION: src.lib.util, DTYPE: {dtype}, LENGTH: {length}\nEXCEPTION:\n{str(exception)}')

    def is_list_of_str(str_of_list):
        """
        Validates input is a list of str

        Returns
        -------
        bool
        """

        return type(str_of_list) == list and all(isinstance(s, str) and s.isascii() for s in str_of_list)