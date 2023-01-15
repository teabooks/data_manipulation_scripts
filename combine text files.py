import os

# specify the directory where the files are located
directory = 'path/to/files'

# create an empty set to store the lines
lines = set()

# iterate over the files in the directory
for filename in os.listdir(directory):
    # only process text files
    if filename.endswith('.txt'):
        # open the file
        with open(os.path.join(directory, filename)) as f:
            # read the lines from the file
            file_lines = f.readlines()
            # add the lines to the set
            lines.update(file_lines)

# write the deduplicated lines to a new file
with open('deduped_lines.txt', 'w') as out_file:
    for line in lines:
        out_file.write(line)

#This script first specify the directory where the files are located. Then it creates an empty set called lines, which will be used to store the lines from the files. It iterates over the files in the directory and for each file it opens the file, reads the lines from the file, and adds the lines to the set. Since sets are unique it automatically deduplicates the lines. Finally it writes the deduplicated lines to a new file named deduped_lines.txt