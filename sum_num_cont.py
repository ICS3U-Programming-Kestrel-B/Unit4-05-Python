#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Nov. 10, 2022
# This program asks how many numbers
# you want to add together, gets that
# numbers of integers from the user,
# and displays the sum

import random
import math


def main():
    # introductory paragraph
    print("This program asks how many numbers")
    print("you want to add together, gets that")
    print("numbers of integers from the user,")
    print("and displays the sum")
    print("")

    # input
    # initializing sum
    sum = 0

    # initializing work_string2
    work_string2 = ""

    # initializing counter
    counter = 1

    # getting num_count_string
    num_count_string = input("Enter the amount of integers: ")

    # checking that num_count_string is an int
    try:
        # checking that num_count_int is an integer
        num_count_int = int(num_count_string)

        # if counter <= num_count_int:
        # starting loop
        while counter <= num_count_int:
            # checking that num_count_int isn't negative
            if num_count_int < 0:
                print("Please enter a positive number.")
                print("Thanks for playing!")
                # continue
            if num_count_int > 0:
                # getting user_num_string
                user_num_string = input(("Enter a number: ").format(num_count_int))
                # getting user_num_int
                user_num_int = int(user_num_string)

                # continue statement???
                # if user_num_int < 0:
                #    continue

                # updating counter
                counter = counter + 1
                # updating sum
                sum = sum + user_num_int
                # updating work_string
                work_string = ("{} + ").format(user_num_int)
                # updating work_string2
                work_string2 = work_string2 + work_string
            if counter > num_count_int:
                print(work_string2)
                print(("= {}").format(sum))
        # except ValueError:
        # print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid integer.")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()

# code graveyard

# if user_num_int >= 0:
#    continue
# print(user_num_int)

# num_count_int = num_count_int - 1
# print(("{} 2").format(num_count_int))

# if counter == 0:
# print(("= {}").format(sum))
# elif user_num_int < 0:
# print("Please enter a positive number.")
# else:
# print("No comment")
# except ValueError:
# print("Please enter a valid integer.")

# print(user_num_int)
# while counter <= num_count_int:

# work_string = user_num_int + " + "
