from .. import cli
import random
import prompt


def welcome_user():
    global username
    username = prompt.string("Present yourself: ")
    print(f"Hello, {username}!")


def calc(num1, num2, act):
    if act == "+":
        return num1 + num2
    if act == "-":
        return num1 - num2
    if act == "*":
        return num1 * num2


def calc_game():
    print('What is the result of the expression?')
    for _ in range(3):
        num1 = random.randrange(1, 100)
        num2 = random.randrange(1, 100)
        acts = ['+', '-', '*']
        act = random.choice(acts)
        num = calc(num1, num2, act)
        print(f'Question: {num1} {act} {num2}')
        ans = int(input(f'Your answer: '))
        if ans == num:
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{num}'.\nLet's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    calc_game()


if __name__ == "__main__":
    main()
