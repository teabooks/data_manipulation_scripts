import os

def merge_and_dedupe(file_paths, output_file):
    # Create an empty set to store unique lines
    unique_lines = set()

    # Iterate through each file path
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            # Read the lines of the file
            lines = f.readlines()
            # Add each line to the set, which will automatically dedupe identical lines
            unique_lines.update(lines)

    # Write the unique lines to the output file
    with open(output_file, 'w') as f:
        for line in unique_lines:
            f.write(line)

# Example usage:
file_paths = ['./file1.txt', './file2.txt', './file3.txt']
output_file = './merged_deduped.txt'
merge_and_dedupe(file_paths, output_file)


#This script defines a function merge_and_dedupe that takes in a list of file paths and an output file path. It creates an empty set unique_lines to store the unique lines from all the files. It then iterates through each file path, opens the file, reads the lines, and adds each line to the set unique_lines. Since sets automatically dedupe identical lines, this will remove any duplicate lines from the files. Finally, the script writes the unique lines to the output file.

#You can use this script by calling merge_and_dedupe passing the list of files you want to merge and the output file path.