import random

nums_simulation = 30000
fixed_cost = 50000

def market_condition():
    units = 0
    price = 0
    condition = random.randint(1,3)
    # Good
    if condition == 1:
        units = 100000
        price = 10.5
    # Fair
    elif condition == 2:
        units = 80000
        price = 8.5

    #3 Bad
    else:
        units = 50000
        price = 7.5

    return units, price

def situation():
    cost = 0
    cost_situation = random.randint(1, 3)
    if cost_situation == 1:
        cost = 2.5
    elif cost_situation == 2:
        cost = 3.5
    else:
        cost = 5

    return cost

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    total = 0
    for x in range(0,nums_simulation):
        units, price = market_condition()
        cost = situation()
        profit = ((price - cost)*units) - fixed_cost
        total += profit

    print('Average profit: ' + "{0:,.2f}".format(total/nums_simulation))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
