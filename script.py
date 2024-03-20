import os

# Get the current directory
current_dir = os.getcwd()

# Get a list of all files in the current directory
files = os.listdir(current_dir)

# Filter the list to include only .py files
py_files = [file for file in files if file.endswith(".py")]

# Initialize an empty string to store the concatenated text
concatenated_text = ""

# Iterate over each .py file
for file in py_files:
    # Open the file and read its content
    with open(file, "r") as f:
        file_content = f.read()
        
    # Append the file content to the concatenated text
    concatenated_text += file_content + "\n\n"

# Create a new text file to store the concatenated text
output_file = "concatenated_files.txt"
with open(output_file, "w") as f:
    f.write(concatenated_text)

print(f"Concatenated text saved to {output_file}")
