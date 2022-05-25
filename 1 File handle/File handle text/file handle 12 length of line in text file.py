def longlines():
    F = open("story.txt", "r")
    line = F.readlines()            #按行读取

    for i in line:
        if len(i) < 50:
            print(i, end="   ")

    F.close()


longlines()
