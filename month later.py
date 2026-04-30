def two_sum(nums, target):
    if len(nums) <= 3 or len(nums) > 10**4:
        return None
    for num in nums:
        if num <= -10**9 or num >= 10**9:
            return None
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return None

def stock_buying_and_selling(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

def main():

    prices = [7, 1, 0, 3, 6, 4]
    result = stock_buying_and_selling(prices)
    print(result)

main()