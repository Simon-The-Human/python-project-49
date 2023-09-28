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


def prime(num):
    prime = 'yes'
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            prime = 'no'
    return prime


def prime_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        num = random.randrange(1, 100)
        print(f'Question: {num}')
        is_prime = prime(num)
        ans = input('Your answer: ')
        if ans == is_prime:
            print('Correct!')
        else:
            print(wrong_answer(ans, is_prime, username))
            break
    else:
        print(f'Congratulations, {username}!')


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    prime_game()


if __name__ == "__main__":
    main()
