#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 18, 2021
# Adds a series of numbers together


def main():

    # First input
    user_input = (input("Enter the amount of numbers to be added: "))

    try:
        number_of_numbers = int(user_input)
        loop_counter = 0
        total_sum = 0

        for loop_counter in range(number_of_numbers):
            loop_counter = loop_counter + 1
            user_input2 = (input("Enter a number to be added: "))
            try:
                user_number = int(user_input2)
                if (user_number <= 0):
                    continue
                total_sum = total_sum + user_number
            except Exception:
                print("{} is not an integer".format(user_input2))
    except Exception:
        print("{} is not a positive integer".format(user_input))
    print("The sum of the positive numbers is = {}".format(total_sum))


if __name__ == "__main__":
    main()
