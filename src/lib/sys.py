import subprocess

from src.lib.util import Util

class Sys:
    """
    A class interact with the system.

    ...

    Methods
    -------
    run(cmd):
        Executes system commands and captures their output.
    """

    def run(cmd):
        """
        Executes system commands and captures their output.

        Parameters
        ----------
            cmd : List<str>
                Command split by spaces into a list of str. i.e. ['ls', '-l']

        Returns
        -------
        str
        """

        if Util.is_list_of_str(cmd):
            try:
                return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=3).stdout.decode('ascii')
            except Exception as e:
                raise Exception(Util.format_error('failed to run the command on subprocess', 'src.lib.sys.run', cmd, e))

        raise Exception(Util.format_error('input was not a list of strings', 'src.lib.sys.run', cmd, None))