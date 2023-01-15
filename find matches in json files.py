import os
import json
import re

# specify the directory where the JSON files are located
directory = 'path/to/json_files'

# specify the key phrase to search for
key_phrase = 'example'

# create a list to store the matches
matches = []

# iterate over the files in the directory
for filename in os.listdir(directory):
    # only process JSON files
    if filename.endswith('.json'):
        # open the file
        with open(os.path.join(directory, filename)) as f:
            # load the JSON data from the file
            data = json.load(f)
            # search for the key phrase in the JSON data
            for key, value in data.items():
                if isinstance(value, dict):
                    for k,v in value.items():
                        if key_phrase in v:
                            matches.append(v)
                elif key_phrase in value:
                    matches.append(value)

# extract the sentences that contain the key phrase
sentences = []
for match in matches:
    for sentence in match.split('\n'):
        if key_phrase in sentence:
            sentences.append(sentence)

# print the sentences
print(sentences)


#This script first specifies the directory where the JSON files are located and the key phrase to search for. Then it creates an empty list called matches, which will be used to store the matches. It iterates over the files in the directory and for each file it opens the file, loads the JSON data from the file and search for the key phrase in the JSON data using for loop. If it finds the key phrase in any value, it appends it to the matches list. After that, it loops over the matches and for each match, it splits the match by \n (newline) and then loops over the sentences, if it finds the key phrase in the sentence, it appends it to the sentences list. Finally, it prints the sentences.