# Factorial of n = product of n and all positive integers less than n
import string


def factorial(n):
    # The Unintentional Case
    if n < 0 or not isinstance(n, int):
        raise ValueError("Input must be a non-negative integer")

    # Base Condition: Exit Condition
    if n in [0, 1]:
        return 1

    # Recursive Case
    return n * factorial(n - 1)


print(factorial(17))


# -------------------------------------------------------------------------------------------------

# Fibonacci numbers. find the nth fibonacci
# To make it fast and avoid re-calculating numbers already done, we going to use a list to store them

def fibonacci(n, previous_list={}):
    # unintentional case
    if n < 0 or not isinstance(n, int):
        raise ValueError("Input must be a positive integer")

    # base conditions
    if n in previous_list:
        return previous_list[n]
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1

    # recursive conditions
    previous_list[n] = fibonacci(n - 1, previous_list) + fibonacci(n - 2, previous_list)
    return previous_list[n]


for i in range(10):
    print(f"{i} -> {fibonacci(i)}")


# --------------------------------------------------------------------------------------------------------

# Sum the digits of a positive integer using recursion

def sum_of_digits(number):
    # the unintentional case
    if number < 0 or not isinstance(number, int):
        raise ValueError("Input must be a positive integer")

    # the base condition
    if number < 10:
        return number

    # the recursive condition
    last_digit = number - ((number // 10) * 10)
    rest_of_digits = (number // 10)
    return last_digit + sum_of_digits(rest_of_digits)


print(sum_of_digits(101010))


# -------------------------------------------------------------------------------------------------------

# power of a number using recursion

def power_of_x(x, y):
    # unintentional case
    if type(x) not in [int, float] or not isinstance(y, int) or y < 0:
        raise ValueError("X must be an integer and Y must be a positive integer")

    # base conditions
    if y == 0:
        return 1
    if y == 1:
        return x

    # recursive condition
    return x * power_of_x(x, y - 1)


print(power_of_x(3, 4))


# ----------------------------------------------------------------------------------------------------

# greatest common factor or divisor

def gcf(x, y):
    # unintentional case
    if isinstance(x, int) and isinstance(y, int):
        if x < 0:
            x = x * -1
        if y < 0:
            y = y * -1
    else:
        raise ValueError("Input has to be integers")

    # base condition
    if y == 0:
        return x

    # recursive case
    # Using Euclidean Algorithm
    return gcf(y, x % y)


print(gcf(985602920, -1448))


# ------------------------------------------------------------

# convert decimal to binary

def dec_to_bin(d):
    # Exceptions case
    if d < 0 or not isinstance(d, int):
        raise ValueError("Please input positive integers only")

    # base case
    if d == 0:
        return "0"
    if d == 1:
        return "1"

    # recursive case
    reminder = d % 2
    quotient = d // 2
    return dec_to_bin(quotient) + str(reminder)


print(dec_to_bin(1000))


# ------------------------------------------------------------

# convert binary to decimal

def bin_to_dec(b, i=0):
    # Exceptions case
    if not isinstance(b, str):
        raise ValueError("Please input string of 0s an 1s only")

    # base case
    if len(b) == 0:
        return 0

    # recursive case
    return bin_to_dec(b[:-1], i + 1) + int(b[-1]) * pow(2, i)


print(bin_to_dec("101010101"))


# -----------------------------------------------------------
# Write a recursive function called nestedEvenSum. Return the sum of all even numbers in an
# object which may contain nested objects.

def nested_even_sum(obj):
    # base condition
    if not obj:
        return 0

    # recursive condition
    sum = 0

    k, v = obj.popitem()
    if isinstance(v, int):
        if v % 2 == 0:
            sum += v
    elif isinstance(v, dict):
        sum += nested_even_sum(v)

    return sum + nested_even_sum(obj)

"""
    -----------------------------------------------
    another solution

    # base condition
    if not obj:
        return sum

    # recursive condition
    k,v = obj.popitem()
    if isinstance(v, int):
        if v % 2 ==0:
            sum += v
    elif isinstance(v, dict):
        sum += nestedEvenSum(v)

    return nestedEvenSum(obj, sum)

-------------------------------------------------------
    # another solution is much simpler
    sum = 0
    for k, v in obj.items():
        if isinstance(v, int):
            if v % 2 == 0:
                sum += v
        elif isinstance(v, dict):
            sum += nestedEvenSum(v)

    return sum
"""


obj1 = {
    "outer": 2,
    "obj": {
        "inner": 2,
        "otherObj": {
            "superInner": 2,
            "notANumber": True,
            "alsoNotANumber": "yup"
        }
    }
}

obj2 = {
    "a": 2,
    "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
    "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": 'car'}
}

print(nested_even_sum(obj1))  # 6
print(nested_even_sum(obj2))  # 10

#-------------------------------------------------------------------

from pprint import pprint

"""
stringifyNumbers
Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and converts them to strings. Recursion would be a great way to solve this!

Examples

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}
 
stringifyNumbers(obj)
 
{'num': '1', 
 'test': [], 
 'data': {'val': '4', 
          'info': {'isRight': True, 'random': '66'}
          }
}
"""

def stringifyNumbers(obj):
    # recursive condition
    for k in obj:
        if isinstance(obj[k], int):
            obj[k] = str(obj[k])
        elif isinstance(obj[k], dict):
            obj[k] = stringifyNumbers(obj[k])

    return obj

def stringifyNumbers2(obj):

    # recursive condition
    for k in obj:
        if type(obj[k]) is int:
            obj[k] = str(obj[k])
        elif type(obj[k]) is dict:
            obj[k] = stringifyNumbers(obj[k])

    return obj



obj = {
     "num": 1,
     "test": [],
     "data": {
          "val": 4,
          "info": {
               "isRight": True,
               "random": 66
          }
     }
}
print(obj)
print(stringifyNumbers(obj))
print(stringifyNumbers2(obj))