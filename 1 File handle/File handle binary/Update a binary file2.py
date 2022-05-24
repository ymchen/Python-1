# updating records in a bnary file

import pickle


def update():
    F = open("studrec.dat", "rb+")
    value = pickle.load(F)
    found = 0
    roll = int(input("Enter the roll number of the record"))
    for i in value:
        if roll == i[0]:
            print("current name", i[1])
            print("current marks", i[2])
            i[1] = input("Enter the new name")
            i[2] = int(input("Enter the new marks"))
            found = 1

    if found == 0:
        print("Record not found")

    else:
        F.seek(0)
        pickle.dump(value, F)
    F.close()

update()
F = open("studrec.dat", "rb")
val = pickle.load(F)
print(val)
F.close()
