# Part A
with open('learning_python.txt', 'r') as file_read:
    print(file_read.read())
print()

# Part B
with open('learning_python.txt', 'r') as file_read:
    for string in file_read:
        print(string, end='')
print("\n")

# Part C
with open('learning_python.txt', 'r') as file_read:
    strings = file_read.readlines()
    for string in strings:
        print(string, end='')
