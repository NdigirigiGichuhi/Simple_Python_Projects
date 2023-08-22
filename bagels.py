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



def get_number():
    print("I have thought up a number.\n"
            "  You have 10 guesses to get it.")

    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(num_list)
    num_1 = str(num_list[0])
    num_2 = str(num_list[1])
    num_3 = str(num_list[2])
    my_num = num_1 + num_2 + num_3;

    return (my_num);

def get_guess_num():
    guess = input("Enter your guess: ")

    if len(guess) < 3 or len(guess) > 3:
        print("Enter three numbers")

    return guess


def give_clues(my_num, guess):

    if guess == my_num:
        return "You won"

    clues = ["Fermi", "Pico", "Bagels", "You won"]

    for i in range(len(my_num)):
        if my_num[i] == guess[i]:
            return clues[0]

        elif guess[i] in my_num:
            return clues[1]
        if not guess[i] in my_num:
            return clues[2]

    return clues


def main():

    i = 1;
    intro()

    my_num = get_number()
    #print(my_num)
    while i <= 10:
        print("\nAttempt #{}".format(i))
        guess = get_guess_num()
        clues = give_clues(my_num, guess)
        print(clues)
        i += 1
        if clues == "You won":
            break
    print("Thank you for playing")


main()
