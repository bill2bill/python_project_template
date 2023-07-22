# Python Template

This repository is an example template of how to layout a Python project using test driven development (TDD).

---
---
---


# SeekerShout

SeekerShout is a program to print formatted lines in a file where words in the line contain a substring.

Example

    ss.sh path/to/file

Expected Output

    [word word]
    [word]

## Constraints

- user must input a path
- user must input one argument
- files must not contain lines with over 1 million characters
- file must not have empty rows
- file must contain the search term at the end of the file
- files must be ASCII text files

## Prerequisites

- Python 3.7 or higher setup with VENV support
- make must be installed
- tail must be installed

## Setup

Once all prerequisites are installed a command can be run to setup the environment.

    make setup

## Testing

To test the code is up to standard

    make setup_dev
    make test

## Future

If I could continue developing and improve the project further

- Linting using pylint
- Code formatter using black
- Convert [THOUGHTS.md](docs/THOUGHTS.md) to proper documentation
- Structure the tests using groups
- Test for more extreme conditions, i.e. a line with 1 million characters

## Past

If I could go back and do the project differently

- Git init at the beggining and commit meaningful milestones in the project. i.e. docs complete, tests complete ...