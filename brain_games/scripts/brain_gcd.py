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


def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def gcd_game():
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        num1 = random.randrange(1, 100)
        num2 = random.randrange(1, 100)
        gcd_num = gcd(num1, num2)
        print(f'Question: {num1} {num2}')
        ans = int(input('Your answer: '))
        if ans == gcd_num:
            print('Correct!')
        else:
            print(wrong_answer(ans, gcd_num, username))
            break
    else:
        print(f'Congratulations, {username}!')


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    gcd_game()


if __name__ == "__main__":
    main()
