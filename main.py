import os
str1 = "dd if=/dev/zero of=./"
str2 = " bs=1M count=100 status=progress"
count = int(input("来几个? : "))
for i in range(count):
    str3 = str1 + str(i) + str2
    os.system(str3)
