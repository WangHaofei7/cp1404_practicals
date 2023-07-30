NAME_FILE = "name.txt"
NUMBER_FILE = "number.txt"
NUMBERS = [17, 42, 400]

#name
out_file = open(NAME_FILE, 'w')
name = input("Entry your name(enter to exit): ")
while name is not "":
    out_file.write(f"{name}\n")
    name = input("Entry your name(enter to exit): ")
out_file.close()

in_file = open(NAME_FILE, 'r')
for name in in_file.readlines():
    name = name.strip()
    print(f"Your name is {name}")
in_file.close()

#number
out_file = open(NUMBER_FILE, 'r')
result = 0
first_two_numbers = in_file.readlines()[:2]
result = int(first_two_numbers[0]) + int(first_two_numbers[1])
print(f"result:{result}")
in_file.close()

# print total for all lines in a file
target_file = NUMBERS_FILE
total = 0
in_file = open(target_file, 'r')
for line in in_file.readlines():
    number = int(line)
    total += number
print(f"total:{total}")
in_file.close