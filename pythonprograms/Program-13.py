""" Program-13 : To read and write from a file """
file1 =open("MyFile.txt")   # opening file
print(file1)
print(file1.read())  # How to read a  file
file1.close()     #closing file

# How to write in file
file2 = open("MyFile.txt",'w')
file2.write('powerpork\n')
file2.write('indrag\n')
file2.write('mishti\n')
file2.write('sankarshan')
file2.close()

file2= open("MyFile.txt")
print(file2.read())
file2.close()