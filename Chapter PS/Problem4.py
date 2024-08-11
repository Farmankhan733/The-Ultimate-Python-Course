import os

# Sepcify the directory you want to list.
directory_path = '/The-Ultimate -Python-Course'

# List all files and directories in the specified path 
contents = os.listdir(directory_path)

# Print each file and directory name 
for item in contents:
    print(item)