import argparse
import asyncio
import logging
import os
from pathlib import Path
from shutil import copy2

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Sort files in a source folder into subfolders in an output folder based on file extensions.')
parser.add_argument('source_folder', type=str, help='The source folder path')
parser.add_argument('output_folder', type=str, help='The output folder path')

# Parse command line arguments
args = parser.parse_args()

# Initialize asynchronous paths for the source and output folders
source_path = Path(args.source_folder)
output_path = Path(args.output_folder)

# Asynchronous function to read all files in the source folder and its subfolders
async def read_folder(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            await copy_file(Path(root) / file)

# Asynchronous function to copy each file to the corresponding subfolder in the output folder based on its extension
async def copy_file(file_path):
    extension = file_path.suffix[1:]  # Get the file extension without the dot
    target_folder = output_path / extension
    target_folder.mkdir(exist_ok=True)  # Create the subfolder if it doesn't exist
    target_path = target_folder / file_path.name
    copy2(file_path, target_path)  # Copy the file to the target path
    print(f'Copied {file_path} to {target_path}')

# Main block to run the asynchronous read_folder function
if __name__ == '__main__':
    # Set up error logging
    logging.basicConfig(level=logging.ERROR)

    # Run the read_folder function asynchronously
    asyncio.run(read_folder(source_path))
