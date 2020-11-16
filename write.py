# read the file and store all the line in the list
# reverse the list
# write the list back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    r_content = reversed(content)
    with open('test.txt', 'w') as writer:
        for line in r_content:
            writer.write(line)
