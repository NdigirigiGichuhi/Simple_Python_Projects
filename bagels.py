#!/usr/bin/python3

import random

attempts = 0


def intro():
    print("Bagels, a deductive logic game.\n"
            "By Ndigirigi Gichuhi ndigirigigichuhi@gmail.com")

    print("I am thinking of a 3-digit number."
            " Try to Guess what it is.\n"
            "Here are some clues:\n"
            "When I say:     That means:\n"
            "   Pico         One digit is correct but in the"
            " wrong position.\n"
            "   Fermi        One digit is correct and in the "
            "right position.\n"
            "   Bagels       No digit is correct.\n")

def generate_number():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(my_list)  #shuffle my_list
    num = my_list[:3] #slice the list to first 3 numbers
    #make the slice string
    my_string = ""
    for number in num:
        my_string += str(number)
    return my_string


def guess_number():
    while True:
        secret_num = generate_number()
        print(secret_num)

        while True:
            guess_num = str(input("Enter a guess "))
            if len(guess_num) < 3 or len(guess_num) > 3:
                print("Enter three numbers")
            else:
                break

        if guess_num == secret_num:
            print("You won!!")
            break
            
        for i in range(len(secret_num)):
            if guess_num[i] == secret_num[i]:
                print("Correct number at the right position")
                print(guess_num[i])

        for i in range(len(secret_num)):
            if guess_num[i] in secret_num:
                print("Correct number in the wrong position")
                print(guess_num[i])


def main():
    guess_number()

if __name__ == "__main__":
    main()
