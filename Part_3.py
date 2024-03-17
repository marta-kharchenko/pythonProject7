lines = 0
words = 0
characters = 0
file = 'learning_python.txt'

with open(file, 'r') as file_read:
    for line in file_read:
        lines += 1
        words += len(line.split())
        characters += len(line)

print('Number of lines: ', lines)
print('Number of words: ', words)
print('Number of characters: ', characters)

