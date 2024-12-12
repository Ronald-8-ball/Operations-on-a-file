file = open('File1.txt','r')
print(file.read())
file.close()

file = open('File1.txt','r')
print(file.read(5))
file.close()

file = open('File1.txt','a')
file.write("\n I am de best programmer")
file.close()
