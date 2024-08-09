"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Karel Černý
email: karel.cerny@t-mobile.cz
discord: charliebalck
"""
import random


def input_number() -> str:
    str_number = input("Enter a number: ")
    print(f'{"-" * 47}\n>>> {str_number}')
    return str_number


def welcome() -> str:
    print(
        f'Hi there!\n{"-" * 47}'
        f'\nI\'ve generated a random 4 digit number for you.'
        f'\nLet\'s play a bulls and cows game.\n{"-" * 47}'
    )
    return input_number()


def check_number(str_number: str) -> str:
    while True:
        if not str_number.isnumeric():
            print("The input is not numeric.")
            str_number = input_number()
        elif len(str_number) != 4:
            print("The input does not have only 4 characters.")
            str_number = input_number()
        elif len(set(str_number)) != 4:
            print("The input has duplicate characters.")
            str_number = input_number()
        elif str_number.startswith("0"):
            print("The input starts with 0.")
            str_number = input_number()
        else:
            break
    return str_number


def set_secretnumber() -> str:
    str_secretnumber = "1111"
    while True:
        if len(set(str_secretnumber)) != 4:
            str_secretnumber = str(random.randint(1000, 9999))
        else:
            break
    return str_secretnumber


def game(str_number: str, str_secretnumber: str) -> str:
    int_bulls = 0
    int_cows = 0
    str_bull = "bull"
    str_cow = "cow"
    lst_bulls = []
    if str_number == str_secretnumber:
        str_result = "Correct, you've guessed the right number"
    else:
        for x in range(0, 4):
            if str_number[x:x + 1] == str_secretnumber[x:x + 1]:
                int_bulls = int_bulls + 1
                lst_bulls.append(str_number[x:x + 1])
        for x in str_number:
            if x in str_secretnumber and x not in lst_bulls:
                int_cows = int_cows + 1
        if int_bulls > 1:
            str_bull = str_bull + "s"
        if int_cows > 1:
            str_cow = str_cow + "s"
        str_result = f'{int_bulls} {str_bull}, {int_cows} {str_cow}\n{"-" * 47}'
    return str_result


def main():
    str_secretnumber = set_secretnumber()
    # print(str_secretnumber)
    str_number = welcome()
    str_number = check_number(str_number)
    str_result = game(str_number, str_secretnumber)
    int_counter = 0
    str_guess = "guess"
    while True:
        int_counter = int_counter + 1
        if str_result.startswith("Correct"):
            break
        else:
            print(str_result)
            str_result = game(check_number(input_number()), str_secretnumber)
    if int_counter > 1:
        str_guess = str_guess + "es"
    print(f'{str_result}\nin {int_counter} {str_guess}!\n{"-" * 47}')


if __name__ == "__main__":
    main()
