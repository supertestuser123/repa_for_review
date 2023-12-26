import random
from math import gcd
from brain_games.cli import welcome_user

def generate_random_numbers():
    """Функция создания рандомных чисел"""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    return num1, num2

def ask_question(name):
    correct_answers = 0
    for _ in range(3):
        num1, num2 = generate_random_numbers()
        print(f'Question: {num1} {num2}')
        user_answer = int(input("Your answer: "))

        if user_answer == gcd(num1, num2):
            print("Correct!")
            correct_answers += 1
            if correct_answers == 3:
                print(f"Congratulations, {name}!")
                break
        else:
            correct_gcd = gcd(num1, num2)
            print(f"'{user_answer}' is the wrong answer "
                  f";(. Correct answer was '{correct_gcd}'.")
            print(f"Let's try again, {name}!")
            break


def main():
    name = welcome_user()

    print("Find the greatest common divisor of given numbers.")

    ask_question(name)


if __name__ == "__main__":
    main()
