# Display all odd numbers between 1 and 20
for i in range(1, 21 ,2):
    print(i, end='')
print()

# Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end='')
    print()

# Count from 20 to 1
for i in range(20, 0, -1):
    print(i, end='')
print()

# Print n stars
n = int(input("Number of stars: "))
for i in range(n):
    print('*', end='')
print()

# Print n lines of increasing stars
for i in range(1, n+1):
    print ('*' * i)