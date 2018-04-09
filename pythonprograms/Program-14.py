""" Program-14 : To copy a file """
import sys
if len(sys.argv) < 3:
    print("Wrong parameter")
    print("./copyfile.py file1 file2")
    sys.exit(1)

f1 = open(sys.argv[1])   #open first file
s = f1.read()
f1.close()               # close first file
f2 = open(sys.argv[2], 'w')  # open second file in write mode
f2.write(s)                  # cope the contant of one file to othere
f2.close()