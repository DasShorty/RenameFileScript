import os

path = input("Path to dir: ")
print("Path: " + path)
prefix = input("Prefix to remove: ")
print("Prefix: " + prefix)

arr = os.listdir(path)

print("Files: " + str(arr))
input("Continue? ")


def rename(old, new):
    os.rename(path + old, path + new)


for file in arr:
    if prefix not in file.title():
        print("skipping " + file.title())
        continue

    newFileName = file.title().replace(prefix, "").strip()
    print(newFileName)
    rename(file.title(), newFileName)
