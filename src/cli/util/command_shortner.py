import argparse
import os

# Create the argument parser
parser = argparse.ArgumentParser(description='Process a file based on its extension')
parser.add_argument('filename', type=str, help='The name of the file to process')

# Parse the arguments
args = parser.parse_args()

# Get the extension of the file
file_ext = os.path.splitext(args.filename)[1]

# Check the extension and execute the corresponding command
if file_ext == '.py':
    # Execute the command to run a Python script
    print(f"Running the Python script:")
elif file_ext == '.txt':
    # Execute the command to display the contents of a text file
    print(f"Displaying the contents of the text file: {args.filename}")
else:
    # File extension not recognized
    print(f"Error: file extension not recognized for file {args.filename}")
