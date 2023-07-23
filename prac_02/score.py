import random

def main():
    score = float(input("Enter score: "))
    result = convert_to_result(score)
    print(f"Score:{score}, Result:{result}")

    random_score = random.randint(0, 101)
    result = convert_to_result(random_score)
    print(f"Random score : {random_score}, Result:{result}")

def convert_to_result(score):
    result = ""
    if score < 0 or score > 100:
        result = "Invalid score"
    else:
        if score > 50:
            result = "Passable"
        if score > 90:
            result = "Excellent"
    if score < 50:
        result = "Bad"

    return result