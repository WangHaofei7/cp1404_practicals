def get_valid_denominator(prompt):
    denominator = int(input("Enter the denominator"))
    while denominator == 0:
        print("denominator can be zero!")
        denominator = int(input("Enter the denominator"))

    return denominator


try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")