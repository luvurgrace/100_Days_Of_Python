# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close() # have to close file
#
with open("../../../../Desktop/my_file.txt") as file: # reading file
    contents = file.read()
    print(contents) # no need to close it

# with open("/Users/MikitaLutsik/Desktop/my_file.txt", mode="w") as file: # read-only mode "r"
#     file.write("New text.")


# TO MAKE FILE READABLE:
# "w" (removing all file's info instead). If file does not exist, it will be created
# "a" (adding something to file)


