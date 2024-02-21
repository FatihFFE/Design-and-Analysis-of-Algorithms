def min_coins(total_amount, coins):
    coins.sort(reverse=True)

    num_coins= 0
    i = 0

    while total_amount > 0 and i< len(coins):
        if total_amount >= coins[i]:
            num_coins += total_amount // coins[i]
            total_amount %= coins[i]
        i += 1
    return num_coins

total_amount = 11
coins = [1, 2, 5]
result = min_coins(total_amount, coins)
print(result)