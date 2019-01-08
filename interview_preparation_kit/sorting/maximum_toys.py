prices = [4,2,3,1]
k = 7

def maximumToys(prices, k):
    sorted_prices = sorted(prices)
    print sorted_prices
    num_toys = 0
    toys_sum = 0
    for price in sorted_prices:
        toys_sum +=price
        if toys_sum < k:
            num_toys +=1
            print toys_sum, k, num_toys
        else:
            return num_toys

result = maximumToys(prices, k)

print result
