# Fibonacci
import datetime
import math


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


"""for i in range(0, 100):
    print(f"{i}: {fibonacci(i)}")"""


# Recursion is slower than or equal to Iterative
# This is because there are duplicate calls in Recursive algorithms


# Fibonacci
# iterative approach 1
# This does not start from scratch. it continues. Very Fast

def fibonacci(n):
    a, b = 0, 0
    for i in range(0, n + 1):
        if i == 1:
            a = 0
            b = 1

        print(f"{i}: {b}")
        temp = a + b
        a = b
        b = temp


"""
print(datetime.datetime.now())
fibonacci(100)
print(datetime.datetime.now())
"""


# This approach calculates each nth element form scratch

def fibonacci_iterative(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            c = a + b
            a, b = b, c
        return b


"""
print(datetime.datetime.now())
for i in range(101):
    print(f"{i}: {fibonacci_iterative(i)}")
print(datetime.datetime.now())
"""


# The number factor problem
# x, select the combination of numbers from options that add up to x
# come back to this later

def find_factor_combinations(number, factors):
    """
    This function takes a positive integer 'number' and a list of smaller integers 'factors' as input,
    and returns all possible combinations of smaller numbers in the list that can add up to make that
    number using divide and conquer approach.
    """
    if number == 0:
        return [()]
    if number < 0:
        return []

    factor_combinations = []
    for i in range(len(factors)):
        sub_factor_combinations = find_factor_combinations(number - factors[i], factors[i:])
        for sub_factor_combination in sub_factor_combinations:
            factor_combinations.append((factors[i],) + sub_factor_combination)
    return factor_combinations


print(find_factor_combinations(4, [1, 3, 4]))


# House Robber Problem  in Python
# Return max value without visiting  adjacent items

def house_robber(houses, current_index):
    if current_index >= len(houses):
        return 0
    else:
        steal_first_house = houses[current_index] + house_robber(houses, current_index + 2)
        skip_first_house = house_robber(houses, current_index + 1)
        return max(steal_first_house, skip_first_house)


houses_list = [6, 7, 1, 30, 8, 2, 4]
print(house_robber(houses_list, 0))


# find min number of operations needed to modify one string to another
# Convert One String to Another with minimum operation in Python
# This problem uses The Levenshtein distance algorithm

def find_min_operation(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return find_min_operation(s1, s2, index1 + 1, index2 + 1)
    else:
        delete_op = 1 + find_min_operation(s1, s2, index1, index2 + 1)
        insert_op = 1 + find_min_operation(s1, s2, index1 + 1, index2)
        replace_op = 1 + find_min_operation(s1, s2, index1 + 1, index2 + 1)
        return min(delete_op, insert_op, replace_op)


print(find_min_operation("table", "tbrltt", 0, 0))


## ZERO ONE KNAPSACK PROBLEM
## Given the weights and profits of n items,
## Find max profits within c capacity

class Item:
    def __init__(self, name, weight, profit):
        self.name = name
        self.weight = weight
        self.profit = profit
        self.ratio = self.profit / self.weight


# This solution of greedy algorithm is valid only if you can taken fractions of an item, else, it doesnt give max profit
def get_max_profit(list_of_items: list, max_capacity: int):
    list_of_items = sorted(list_of_items, key=lambda x: x.ratio)

    item = list_of_items.pop()
    reminder = max_capacity
    final_list = []

    while list_of_items:
        if reminder >= item.weight:
            final_list.append(item)

        reminder -= item.weight
        if reminder <= 0:
            break

        item = list_of_items.pop()

    return final_list


list_of_items = \
    [Item("Mango", 3, 31), Item("Apple", 1, 26), Item("Orange", 2, 17), Item("Banana", 5, 72), Item("Lime", 2, 1500)]
answer = get_max_profit(list_of_items, 7)
print([item.name for item in answer])
print(sum([item.profit for item in answer]))


# recursive approach - with greedy algorithm

def get_max_profit2(items, remainder):
    # base conditions
    if len(items) == 0 or remainder <= 0:
        return []

    item = items.pop()
    # recursive case
    if remainder >= item.weight:
        remainder -= item.weight
        return [item] + get_max_profit2(items, remainder)
    else:
        return get_max_profit2(items, remainder)


list_of_items = \
    [Item("Mango", 3, 31), Item("Apple", 1, 26), Item("Orange", 2, 17), Item("Banana", 5, 72), Item("Lime", 2, 1500)]
list_of_items.sort(key=lambda x: x.ratio)
answer = get_max_profit2(list_of_items, 7)
print([item.name for item in answer])
print(sum([item.profit for item in answer]))


# recursive approach -- no greedy algorithm
# This approach uses recursion to include and exclude each item in the list

def get_max_profit3(items, remainder, current_index):
    if remainder <= 0 or current_index >= len(items) or current_index < 0:
        return 0
    elif items[current_index].weight <= remainder:
        profit1 = items[current_index].profit + get_max_profit3(items, remainder - items[current_index].weight,
                                                                current_index + 1)
        profit2 = get_max_profit3(items, remainder, current_index + 1)
        return max(profit1, profit2)
    else:
        return 0


list_of_items = \
    [Item("Mango", 3, 31), Item("Apple", 1, 26), Item("Orange", 2, 17), Item("Banana", 5, 72), Item("Lime", 2, 1500)]
print(get_max_profit3(list_of_items, 7, 0))


############
############

# LONGEST COMMON SEQUENCE
# GIVEN s1 and s2, find the longest common sequence

def longest_common_sequence(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return ""
    elif s1[0] == s2[0]:
        return s1[0] + longest_common_sequence(s1[1:], s2[1:])
    else:
        lcs1 = longest_common_sequence(s1[1:], s2)
        lcs2 = longest_common_sequence(s1, s2[1:])

        if len(lcs1) >= len(lcs2):
            return lcs1
        else:
            return lcs2


print(longest_common_sequence("AMEEWMEA", "MEENA"))


#######
#######

# LONGEST PALINDROMIC SEQUENCE
# A Palindrome is a word that reads in the same way forwards or backwards
# can be solved by calling longest_common_sequence(str, str[::-1]
# but for educative purpose lets do another one from scratch

def longest_palindromic_sequence(s, start_index, end_index):
    # base conditions
    if len(s) == 0 or start_index > end_index:
        return ""
    if start_index == end_index:
        return s[start_index]
    if s[start_index] == s[end_index]:
        return s[start_index] + longest_palindromic_sequence(s, start_index + 1, end_index - 1) + s[end_index]
    else:
        a = longest_palindromic_sequence(s, start_index + 1, end_index)
        b = longest_palindromic_sequence(s, start_index, end_index - 1)
        if len(a) >= len(b):
            return a
        else:
            return b


s = "JAKNN!!!NN"
print(longest_palindromic_sequence(s, 0, len(s) - 1))

# Minimum Cost traversing from top of matrix to down
# 2 D Matrix
# each cell has a cost
# start from (0.0) and end at (n-1,n-1)
# find min cost
TwoDList = [
    [4, 7, 8, 6, 4],
    [6, 7, 3, 9, 2],
    [3, 8, 1, 2, 4],
    [7, 1, 7, 3, 7],
    [2, 9, 8, 9, 3]
]


def minimum_cost_path(matrix, row_index, column_index):
    # base conditions
    if row_index == len(matrix) - 1 and column_index == len(matrix[0]) - 1:
        return matrix[row_index][column_index]

    elif row_index >= len(matrix) or column_index >= len(matrix[0]):
        return math.inf

    # recursive case
    else:
        path1 = minimum_cost_path(matrix, row_index + 1, column_index)
        path2 = minimum_cost_path(matrix, row_index, column_index + 1)
        return matrix[row_index][column_index] + min(path1, path2)


print(minimum_cost_path(TwoDList, 0, 0))

# Number of ways to traverse from top of matrix to down within cost limit
# 2 D Matrix
# each cell has a cost
# start from (0.0) and end at (n-1,n-1)
# find min cost
TwoDList = [
    [4, 7, 1, 6],
    [5, 7, 3, 9],
    [3, 2, 1, 2],
    [7, 1, 6, 3]
]


def number_of_paths(matrix, row_index, column_index, cost_reminder):
    # base conditions
    if cost_reminder < 0:
        return 0
    elif row_index >= len(matrix) or column_index >= len(matrix[0]):
        return 0
    elif row_index == len(matrix) - 1 and column_index == len(matrix[0]) - 1:
        if cost_reminder == 0:
            return 1
        else:
            return 0

    # recursive case
    else:
        path1 = number_of_paths(matrix, row_index + 1, column_index, cost_reminder - matrix[row_index][column_index])
        path2 = number_of_paths(matrix, row_index, column_index + 1, cost_reminder - matrix[row_index][column_index])
        return path1 + path2


print(number_of_paths(TwoDList, 0, 0, 25))
