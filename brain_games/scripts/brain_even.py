#!/usr/bin/env python3
import random
import prompt


def welcome_user():
    global username
    username = prompt.string("May I have your name? ")
    print(f"Hello, {username}!")


def wrong_answer(ans, num, username):
    answer = f"""'{ans}' is wrong answer ;(. Correct answer was '{num}'.
Let's try again, {username}!"""
    return answer


def iseven(num):
    even = 'no'
    if num % 2 == 0:
        even = 'yes'
    return (num, even)


def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        num = random.randrange(1, 100)
        num = iseven(num)
        print(f'Question: {num[0]}')
        ans = input('Your answer: ')
        if ans == num[1]:
            print('Correct!')
        else:
            print(wrong_answer(ans, num[1], username))
            break
    else:
        print(f'Congratulations, {username}!')


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    even_game()


if __name__ == "__main__":
    main()
