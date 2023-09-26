from .. import cli
import random
import prompt


def welcome_user():
    global username
    username = prompt.string("Present yourself: ")
    print(f"Hello, {username}!")


def calc_game():
    def calc(num1, num2, act):
        if act == "+":
            return num1 + num2
        if act == "-":
            return num1 - num2
        if act == "*":
            return num1 * num2
    print('What is the result of the expression?')
    for _ in range(3):
        num = random.randrange(1, 100)
        num = calc(num)
        print(f'Question: {num[0]}')
        ans = input(f'Your answer: ')
        if ans == num[1]:
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{num[1]}'.\nLet's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')
