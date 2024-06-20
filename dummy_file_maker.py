import os
import zipfile

# Directory and file names
directory = "example_directory"
files = ["example1.tcl", "example2.tcl", "txt_example1.txt"]

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Create dummy files
for file in files:
    with open(os.path.join(directory, file), "w") as f:
        f.write(f"This is a dummy file named {file}\n")

# # Create a zip file
# zip_filename = 'example_files.zip'
# with zipfile.ZipFile(zip_filename, 'w') as zipf:
#     for file in files:
#         zipf.write(os.path.join(directory, file), os.path.join(directory, file))

# print(f"Dummy files created and zipped into {zip_filename}")
