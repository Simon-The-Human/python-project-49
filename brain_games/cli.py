import prompt

def welcome_user():
    name = prompt.string("Present yourself: ")
    print(f"Hello, {name}!")
