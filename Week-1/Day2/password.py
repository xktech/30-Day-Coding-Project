# Password Generator

import random
import string

def ask(prompt, options):
    while True:
        choice = input(f"{prompt} ({'/'.join(options)}): ").lower()
        if choice in options:
            return options[choice]
        print(f"Please enter one of: {','.join(options)}")

def configure_password():
    while True:
        print("Configure Password? (y/n): ")

        choice = input("> ").lower()

        if choice == "y":
            config = {
                "numbers": ask("Include numbers?", {"y": True, "n": False}),
                "case": ask("Letter case?", {"u": "upper", "l": "lower", "m": "mixed"}),
                "length": int(input("Enter the length of your password: ")),
            }
            generate_pass(config)
            break
        elif choice == "n":
            generate_pass()
            break


CASE_CHARSETS = {
    "upper": string.ascii_uppercase,
    "lower": string.ascii_lowercase,
    "mixed": string.ascii_letters,
}


def generate_pass(config=None):
    if config is None:
        config = {"numbers": True, "case": "mixed", "length": int(input("Enter the length of your password: "))}
    chaserset = CASE_CHARSETS[config["case"]]
    if config["numbers"]:
        chaserset+=string.digits

    pswd = ''.join(random.choices(chaserset, k=config["length"]))

    print(f"Your password is: {pswd}")
while True:
    print("1. GENERATE PASSWORD")
    print("2. EXIT")

    choice = input("> ")

    if choice == "1":
        configure_password()
    elif choice == "2":
        break

