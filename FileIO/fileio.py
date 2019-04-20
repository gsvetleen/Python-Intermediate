# path of file along with type of what to do after opening
fileknife = open("/home/svetleen/Documents/PythonLearning/sample.txt", 'r')

# example 1
for line in fileknife:
    # condition check if line contains word
    if "jabberwock" in line.lower():
        print(line, end='')  # file already has a new line character
fileknife.close()

# example 2 -> with closes the file for you.
with open("/home/svetleen/Documents/PythonLearning/sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')

# example 3 with assignment
with open("/home/svetleen/Documents/PythonLearning/sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

# example 4 puts each line into a list along with the newline character, NOTE readlineS
with open("/home/svetleen/Documents/PythonLearning/sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

# output list
for line in lines:
    print(line, end='')

# readlines returns a list and readline returns a string of each line in the filef


# read file in reverse
with open("/home/svetleen/Documents/PythonLearning/sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line,end='')