#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        c = None
    finally:
        print("Indeed Results: {}".format(c))
        return(c)
