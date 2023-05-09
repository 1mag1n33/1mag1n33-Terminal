import os

# get the path of the file to be checked
file_path = os.getcwd()

# get the extension of the file
file_ext = os.path.splitext(file_path)[1]
class command_short():
    # check if the file has .py extension
    if file_ext == '.py':
        # execute the command here
        print("Running the Python file")
    else:
        # do something else
        print("File extension is not .py")
