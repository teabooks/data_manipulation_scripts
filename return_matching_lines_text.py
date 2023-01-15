import re

def find_phrase(phrases, filepath):
    matches = []
    with open(filepath, 'r') as f:
        for line in f:
            for phrase in phrases:
                if re.search(phrase, line):
                    matches.append(line.strip())
                    break
    return matches

phrases = ["phrase1", "phrase2", "phrase3"]
filepath = "path/to/text/file.txt"
matches = find_phrase(phrases, filepath)

if matches:
    for match in matches:
        print(match)
else:
    print("None of the patterns were found in the text file.")


#In this code, a list of patterns are passed to the function find_patterns() instead of a single pattern. The for loop iterates over each line in the file, and a nested for loop iterates over each pattern in the list. The re.search() function is used to check if the pattern is found in the line. If a match is found, the line is appended to the matches list using append() function and the inner loop is broken. The strip() function removes any leading or trailing whitespace from the line. After all lines have been processed, the matches list is returned. Finally, the matches are printed if any are found, otherwise it prints that none of the patterns were found in the text file.