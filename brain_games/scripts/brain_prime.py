import random
from brain_games.cli import welcome_user


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(1, 50)
    is_prime_result = is_prime(number)
    correct_answer = 'yes' if is_prime_result else 'no'
    return number, correct_answer


def ask_question(name):
    correct_answers_count = 0
    rounds = 3

    for i in range(rounds):
        number, correct_answer = generate_question()

        print(f"Question: {number}")
        user_answer = input("Your answer: ")

        if user_answer.lower() == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;"
                  f"(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

        if correct_answers_count == rounds:
            print(f"Congratulations, {name}!")


def main():
    name = welcome_user()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    ask_question(name)


if __name__ == "__main__":
    main()
