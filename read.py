file = open('test.txt')
# Read all the content of the file
# print(file.read())
# Read n number of character by passing parameter
# print(file.read(5))
# Read line by line
# print(file.readline())
# print(file.readline())

# line = file.readline()
# while line != "":
#    print(line)
#    line = file.readline()

for line in file.readlines():
    print(line)

file.close()