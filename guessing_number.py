import random


# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f"Enter a number between 1 and {x} =>>> "))

#         if guess < random_number:
#             if random_number-guess < 10:
#                 print("Your guess is close but low, Try again")
#             else:
#                 print("Your guess is too low!!")

#         elif guess > random_number:
#             if guess-random_number < 10:
#                 print("Your guess is close but high, Please, Try again.")
#             else:
#                 print("Your guess is too high")
#     print(
#         f"Congrats, You have guessed the currect number {random_number} correctly.")


# guess(20)


def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":

        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)??").lower()

        if feedback == "h":
            high = guess-1
        elif feedback == "l":
            low = guess-1
    print("Congrats, computer guessed the correct number {guess}.")


computer_guess(10)
