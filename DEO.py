file = open('File2.txt','r')
print(file.readline())
file.close()

file = open('File2.txt','r')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('File2.txt','r')
print(file.readlines())
file.close()

file = open('File2.txt','r')
for x in file:
    print(x)
file.close()
