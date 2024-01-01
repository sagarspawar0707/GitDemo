''''''
#file = open('test.txt')
#read all contests of file
#read n numbers of characters by passing parameters
#print(file.read(5))
#read one single line at aline
#print(file.readline())
#print(file.readline())



#print line by line using readline methods

with open('test.txt', 'r') as file:
    lines = file.readlines()

# Now 'lines' is a list containing all lines from the file
for line in lines:
    print(line)

print(file.mode)
print(file.name)

file.close()

with open('sample.txt' ,'r') as file1:
      lines1=file1.readlines()

for line in lines1:
     print(line.strip())


file1.close()