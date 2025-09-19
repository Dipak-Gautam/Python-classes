# import csv
# data = ["Dipak", 20, "Engineer"]

# with open("data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(data)


# # appending in csv file
# import csv

# data = [
#     ["ram", 10, "Engineer"],
#     ["sam", 11, "Engineer"]
# ]

# with open("data.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)


# # writing with header
# import csv

# import csv

# header = ["Name", "Age", "Occupation"]
# data = [
#     ["Dipak", 24, "Developer"],
#     ["Sita", 22, "Designer"]
# ]

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(header)
#     writer.writerows(data)


# # reading from csv file

# import csv

# with open("data.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# reading in list
import csv
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)
    print(data)
