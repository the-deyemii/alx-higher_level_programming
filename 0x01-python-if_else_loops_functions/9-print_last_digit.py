#!/usr/bin/python3
def print_last_digit(number):
    num = int
    if number < 0:
        num = number % -10
        num *= -1
    else:
        num = number % 10
    print(f'{num:d}', end="")
    return (num)
