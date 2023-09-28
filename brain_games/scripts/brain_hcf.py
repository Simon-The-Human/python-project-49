from .. import cli
import random
import prompt


def welcome_user():
    global username
    username = prompt.string("Present yourself: ")
    print(f"Hello, {username}!")


def hcf(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def hcf_game():
    print('What is the result of the expression?')
    for _ in range(3):
        num1 = random.randrange(1, 100)
        num2 = random.randrange(1, 100)
        hcf_num = hcf(num1, num2)
        print(f'Question: {num1} {num2}')
        ans = int(input(f'Your answer: '))
        if ans == hcf_num:
            print('Correct!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{hcf_num}'.\nLet's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    hcf_game()


if __name__ == "__main__":
    main()
