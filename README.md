# Console note app

![logo](https://raw.githubusercontent.com/pogudo-e/note_console/evgeny/img/logo.png)

## Project Information
___
It is necessary to write a project containing the functionality of working with notes.
The program must be able to create a note, save it, read the list
notes, edit note, delete note.

## Task conditions
___
Implement a note console application, with saving, reading,
adding, editing and deleting notes. The note should
contain an ID, title, body of the note, and creation date/time
or last modified note. Saving notes needed to be done
in json or csv format (field separation is recommended to be done through
semicolon). User interface implementation student can
do as it is more convenient for him, you can do it as program launch parameters
(command, data), can be done as a command request from the console and
subsequent data entry, somehow else, at the discretion of the student.

## Solving the problem
___
A program was written at startup that takes arguments for adding, deleting, reading and updating data in a file.
The program can accept both one command and several different ones in one run. When saving or updating a note, its date is added/updated in the format: *day/mouth/year-hour:minutes*. library [pretty table](https://pypi.org/project/prettytable/) was used for data output

## How to run program

You need to install and run the virtual environment:

    python3 -m venv {project_name}

and:

    source {project_name}/bin/activate

install dependencies:

    pip install -r requirements.txt

> Run the main.py with the required arguments.

## Commads

| Command       | Description |
| ------------- | ----------- |
| `--add -a`    | take note title consisting of one word and its text of any length. |
| `--read -r`   | to read all notes from a file. If there are arguments, it searches and displays all matches. |
| `--edit -e`   | for editing. Next, in the context menu, you must specify the name of the note and, if available, make changes to the text. |
| `--delete -d` | for removing. It accepts arguments in the form of a record identifier or name as input. |
