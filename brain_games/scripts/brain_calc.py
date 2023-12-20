import random

from brain_games.cli import welcome_user


def generate_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    expression = f"{num1} {operator} {num2}"
    correct_answer = str(eval(expression))
    return expression, correct_answer


def ask_question(name):
    correct_answers_count = 0
    rounds = 3

    for i in range(rounds):
        expression, correct_answer = generate_question()

        print(f"Question: {expression}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;"
                  f"(. Correct answer was '{correct_answer}'.")
            print("Let's try again, " + name + "!")
            break

        if correct_answers_count == rounds:
            print("Congratulations, " + name + "!")


def main():
    name = welcome_user()

    print("What is the result of the expression?")

    ask_question(name)


if __name__ == "__main__":
    main()
