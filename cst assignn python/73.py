##73.	Develop a Python script that automates file organization based on file types.

import os
import shutil

def organize_files(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            ext = file.split('.')[-1]
            folder = os.path.join(directory, ext.upper())
            os.makedirs(folder, exist_ok=True)
            shutil.move(file_path, os.path.join(folder, file))

# Example usage
organize_files("your_directory_path")