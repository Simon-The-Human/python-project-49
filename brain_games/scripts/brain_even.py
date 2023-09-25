#!/usr/bin/env python3
from .. import cli
import random
import prompt


def welcome_user():
    global username
    username = prompt.string("Present yourself: ")
    print(f"Hello, {username}!")


def even_game():
    def iseven(num):
        even = 'no'
        if num % 2 == 0:
            even = 'yes'
        return (num, even)
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        num = random.randrange(1, 100)
        num = iseven(num)
        print(f'Question: {num[0]}')
        ans = input(f'Your answer: ')
        if ans == num[1]:
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{num[1]}'.\nLet's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    even_game()


if __name__ == "__main__":
    main()