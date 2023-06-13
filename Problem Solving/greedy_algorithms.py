# Activity Selection Problem
# ==============================
# Given a list of activities with start and end times,
# Selected the max number of activities that can be done by 1 person
# Assume the person can do one activity at a time

activities = [
    ["A1", 0, 6],
    ["A2", 3, 4],
    ["A3", 1, 2],
    ["A4", 5, 8],
    ["A5", 5, 7],
    ["A6", 8, 9]
]

activities.sort(key=lambda x: x[2])
list_of_activities = [activities[0]]

for i in range(1, len(activities)):
    if activities[i][1] >= list_of_activities[-1][2]:
        list_of_activities.append(activities[i])

print(f"{list_of_activities}: number = {list_of_activities.__len__()}")

# Coin Selection Problem
# =======================
# Find the minimum number of coins to make up a given value
denoms = [1, 2, 5, 10, 20, 50, 100]
denoms.sort(reverse=True)
value = 389
ans = []

remainder = value
while True:
    if remainder <= 0:
        break
    for d in denoms:
        if d <= remainder:
            ans.append(d)
            remainder = remainder - d
            break
print(ans)


# Fractional Knapsack Problem
# ===========================
# Given a list of items with value and weight,
# fill a box with max weight = X where the total items in the box gives maximum value

class Item:
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
        self.density = self.value / self.weight
        self.fraction = 0

    def __str__(self):
        return f"{self.name}: V={self.value}: W={self.weight}: D={self.density}: F={self.fraction}"


list_of_items = [Item("ITEM_A", 60, 5), Item("ITEM_B", 100, 20), Item("ITEM_C", 120, 30)]
for i in list_of_items:
    print(i)

# sort by density. the best density comes last
list_of_items.sort(key=lambda x: x.density)
list_max_value = []
remainder_weight = 50

while list_of_items:
    if remainder_weight <= 0:
        break
    item = list_of_items.pop()
    if item.weight <= remainder_weight:
        item.fraction = 1
        list_max_value.append(item)
        remainder_weight -= item.weight
    elif item.weight > remainder_weight:
        item.fraction = remainder_weight / item.weight
        list_max_value.append(item)
        remainder_weight -= item.weight

print("List OF MAX VALUE")
for i in list_max_value:
    print(i)
