# practicing with streams
import sys

sys.stdout.write("Enter the name of the file")

#sys.stdout是python中的标准输出流，默认是映射到控制台的，即将信息打印到控制台。
file = sys.stdin.readline()
print(file)
F = open(file.strip(), "r")
print(F.readlines())
while True:
    ch = F.readlines()
    for i in ch:
        print(i, end="")

F.close()
