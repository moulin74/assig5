import fileinput
import time
file = open('app.py', 'r')
lines = file.readlines()
s = time.time()
count = 0
for index,lines in enumerate(lines):
    print("Line {}: {}".format(index, lines.strip()))
    count = count + 1
e = time.time()
print("Execution time in seconds: ",(e - s))
print("No. of lines printed: ",count)
file.close()