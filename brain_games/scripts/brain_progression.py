import random

from brain_games.cli import welcome_user


def generate_progression():
    progression_length = random.randint(5, 10)
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    hidden_place = random.randint(0, progression_length - 1)

    progression = [start + i * step for i in range(progression_length)]
    hidden_number = progression[hidden_place]
    progression[hidden_place] = '..'

    return progression, hidden_number


def ask_question(name):
    correct_answers_count = 0
    rounds = 3

    for i in range(rounds):
        progression, hidden_value = generate_progression()
        progression_str = ' '.join(map(str, progression))

        print(f"Question: {progression_str}")
        user_answer = int(input("Your answer: "))

        if user_answer == hidden_value:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer "
                  f";(. Correct answer was '{hidden_value}'.")
            print(f"Let's try again, {name}!")
            break

        if correct_answers_count == rounds:
            print(f"Congratulations, {name}!")


def main():
    name = welcome_user()

    print("What number is missing in the progression?")

    ask_question(name)


if __name__ == "__main__":
    main()
