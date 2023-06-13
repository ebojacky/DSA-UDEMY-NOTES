# example of memoization

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


print(fibonacci(100))


# example of tabulation - no recursion

def fibonacci2(n):
    table = [0, 1]

    i = 2
    while True:
        table.append(table[i - 1] + table[i - 2])
        if i == n:
            break
        else:
            i += 1
    return table[n]


print(fibonacci2(100))


def fibonacci2(n):
    table = [0, 1]

    for i in range(2, n + 1):
        table.append(table[i - 1] + table[i - 2])
    return table[n]


print(fibonacci2(100))

# Use Dynamic Programming to solve this

"""
Given N, find the number of ways to to express N as a sum of list of numbers

N = 4
List = [1,3,4] 
"""


def find_factor_combinations(number, factors, memo=None):
    if memo is None:
        memo = {}
    if (number, tuple(factors)) in memo:
        return memo[(number, tuple(factors))]
    if number == 0:
        return [()]
    if number < 0:
        return []

    factor_combinations = []
    for i in range(len(factors)):
        sub_factor_combinations = find_factor_combinations(number - factors[i], factors[i:], memo)
        for sub_factor_combination in sub_factor_combinations:
            factor_combinations.append((factors[i],) + sub_factor_combination)

    memo[(number, tuple(factors))] = factor_combinations
    return factor_combinations


print(find_factor_combinations(4, [1, 3, 4]))


# Solve with tabulation
def find_factor_combinations(number, factors):
    dp = [[] for i in range(number + 1)]
    dp[0] = [()]

    for i in range(1, number + 1):
        for factor in factors:
            if i - factor >= 0:
                for prev_combination in dp[i - factor]:
                    new_combination = prev_combination + (factor,)
                    dp[i].append(new_combination)

    return dp[number]


print(find_factor_combinations(4, [1, 3, 4]))

# Use Dynamic Programming to solve this
"""
House Rubber 

- Given N number of houses along the street with an amount of money:
- Find the max amount of money that can be stolen
- Adjacent houses cannot be stolen
"""


def house_robber(array: list, memo=None):
    if memo is None:
        memo = {}
    if not array:
        return 0
    if len(array) == 1:
        return array[0]
    if tuple(array) in memo:
        return memo[tuple(array)]

    option1 = array[0] + house_robber(array[2:], memo)
    option2 = house_robber(array[1:], memo)
    memo[tuple(array)] = max(option1, option2)

    return memo[tuple(array)]


money_in_each_house = [100, 1000, 5999999, 6000, 7, 80000, 9, 13456]
print(house_robber(money_in_each_house))


# OR THIS. This one does not create new array per function call. Same array is maintained

def house_robber(array, index=0, memo=None):
    if memo is None:
        memo = {}
    if not array:
        return 0
    if index >= len(array):
        return 0
    if index == len(array) - 1:
        return array[index]
    if index in memo:
        return memo[index]

    option1 = array[index] + house_robber(array, index + 2, memo)
    option2 = house_robber(array, index + 1, memo)
    memo[index] = max(option1, option2)

    return memo[index]


money_in_each_house = [100, 1000, 5999999, 6000, 7, 80000, 9, 13456]
print(house_robber(money_in_each_house))


# using tabulation for same problem:

def house_robber(array):
    n = len(array)
    if n == 0:
        return 0
    if n == 1:
        return array[0]

    table = {0: array[0],
             1: max(array[0], array[1])
             }

    for i in range(2, n):
        table[i] = max(array[i] + table[i - 2], table[i - 1])

    return table[n - 1]


print(house_robber(money_in_each_house))

# Use dynamic problem to solve this
"""
S1 and S2 are two given strings
Convert S2 to S1 using delete, insert or replace operations
Find the minimum count of edit operations
This problem uses The Levenshtein distance algorithm
"""


def min_ops_convert_s1_to_s2(s1, s2, memo=None):
    if memo is None:
        memo = {}
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    if (s1, s2,) in memo:
        return memo[(s1, s2,)]

    if s1[0] == s2[0]:
        return min_ops_convert_s1_to_s2(s1[1:], s2[1:], memo)
    else:
        delete = 1 + min_ops_convert_s1_to_s2(s1, s2[1:], memo)
        replace = 1 + min_ops_convert_s1_to_s2(s1[1:], s2[1:], memo)
        insert = 1 + min_ops_convert_s1_to_s2(s1[1:], s2, memo)

        memo[(s1, s2,)] = min([delete, replace, insert])
        return memo[(s1, s2,)]


print(min_ops_convert_s1_to_s2("tableasdasdasd", "tbrlttasdasdasdasdasdsad"))


# solve the same thing with Tabulation

def min_ops_convert_s1_to_s2(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[m][n]


print(min_ops_convert_s1_to_s2("tableasdasdasd", "tbrlttasdasdasdasdasdsad"))

# Solve this with dynamic programming
"""
Given the Weight and Profit of N items:
Find the maximum profit within given capacity C
Items cannot be broken
"""


class Item:
    def __init__(self, n, w, p):
        self.n = n
        self.w = w
        self.p = p
        self.ratio = p / w


items = \
    [Item("Mango", 3, 31), Item("Apple", 1, 26), Item("Orange", 2, 17), Item("Banana", 5, 72), Item("Lime", 2, 1500)]


# recursion with memoization

def get_max_profit(items, capacity, memo=None):
    if memo is None:
        memo = {}
    if (tuple(items), capacity,) in memo:
        return memo[(tuple(items), capacity,)]
    if capacity <= 0 or len(items) == 0:
        return 0

    if capacity - items[0].w >= 0:
        option1 = items[0].p + get_max_profit(items[1:], capacity - items[0].w, memo)
    else:
        option1 = 0

    option2 = get_max_profit(items[1:], capacity, memo)
    memo[(tuple(items), capacity,)] = max(option1, option2)
    return memo[(tuple(items), capacity,)]


print(get_max_profit(items, 7))


# with tabulation

def get_max_profit(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if items[i - 1].w > j:
                dp[i][j] = dp[i - 1][j]
            else:
                option1 = items[i - 1].p + dp[i - 1][j - items[i - 1].w]
                option2 = dp[i - 1][j]
                dp[i][j] = max(option1, option2)

    return dp[n][capacity]


print(get_max_profit(items, 7))
