import random

def get_guess():
    return list(input("What is your Guess"))
def generate_code():
    digits = [str(num) for num in  range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues(code, user_guess):
    if user_guess == code:
        return "code Cracked"
    clues = []

    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("close")
    if clues == []:
        clues.append("Nope")
    else:
        return clues


print("welocome to code breaker!")

secret_code = generate_code()
print(secret_code)
clue_report = []

while clue_report != "code Cracked":
    guess = get_guess()
    clue_report = generate_clues(guess, secret_code)
    print("here is the result of your guess: ")

    print(clue_report)
