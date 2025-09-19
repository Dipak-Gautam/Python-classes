# file = open("example.txt", "w")

# file.write("Hello i am dipak Gautam \n")
# file.write(" this is second line")

# file.close()

# recommended way

# with open("example.txt", "w") as file:
#     file.write("This is first line \n")
#     file.write("This is second line")

# # Appending On File
# with open("example.txt", "a") as file:
#     file.write("\n This line is appended")

# # --- reading from file
# with open("example.txt", "r") as file:
#     content = file.read()

# print("content = ", content)


# ---Deleting a file
# import os

# if os.path.exists("example.txt"):
#     os.remove("example.txt")
#     print("file deleted successfully")
# else:
#     print("no such file exist")
