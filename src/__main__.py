import sys

from src.app import App

if __name__ == "__main__":
    args = sys.argv
    num_of_args = len(args) - 1

    if (num_of_args == 1):
        file_path = args[1]

        if type(file_path) == str:
            previous_words = None
            with App(file_path) as file:
                for words in file:
                    if not words:
                        continue
                    if previous_words and words:
                        print(App.format_words(previous_words))
                    previous_words = words
        else:
            print(f'ERROR: Input is not a string: {file_path}')
    else:
        print(f'ERROR: Invalid number of arguments: {num_of_args}')