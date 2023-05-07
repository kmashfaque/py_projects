import random


def rock_paper_scissor():
    user_input = input(f"Rock (R) or paper (P) or scissor(S) ==>> ").lower()

    computer_input = random.choice(["r", "p", "s"])
    draw_value = 0
    initial_value = 0
    user_value = 0
    computer_value = 0
    final_value = 10
    if user_input:
        while initial_value < final_value:
            user_input = input(
                f"Rock (R) or paper (P) or scissor(S) ==>> ").lower()
            if (user_input == "r" and computer_input == "s") or (user_input == "s" and computer_input == "p") or (user_input == "p" and computer_input == "r"):
                user_value = user_value + 1

            elif computer_input == user_input:
                draw_value = draw_value + 1

            else:
                computer_value = computer_value + 1

            initial_value = initial_value+1

        if computer_value > user_value:
            print(
                f"You lost ==> you won {user_value}, you lost {computer_value}, drawn {draw_value}")
        else:
            print(
                f"You lost ==> you won {user_value}, you lost {computer_value}, drawn {draw_value}")


rock_paper_scissor()

# def is_win(user, oponent):
#     user_value = 0
#     final_value = 10
#     while random_value != final_value:
#         if (user == "r" and oponent == "s") or (user == "s" and oponent == "p") or (user == "p" and oponent == "r"):
#             user_value += 1
#             True
#         else:

# print(rock_paper_scissor())
