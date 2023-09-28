from .. import cli
import random
import prompt


def welcome_user():
    global username
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}!")


def progression(num, coef):
    raw = list()
    c = num
    for _ in range(10):
        raw.append(c)
        c += coef
    return raw


def progression_q(raw):
    c = random.randint(0, 9)
    raw_q = {
        "raw": raw,
        "c": c,
        "ans": raw[c]
    }
    raw_q["raw"][c] = '..'
    return raw_q


def calc_game():
    print('What number is missing in the progression?')
    for _ in range(3):
        num = random.randrange(1, 100)
        coef = random.randrange(1, 20)
        raw = progression(num, coef)
        raw_q = progression_q(raw)
        question = " ".join(str(i) for i in raw_q["raw"])
        print(f'Question: {question}')
        ans = int(input(f'Your answer: '))
        if ans == raw_q["ans"]:
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{raw_q['ans']}'.\nLet's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    calc_game()


if __name__ == "__main__":
    main()
