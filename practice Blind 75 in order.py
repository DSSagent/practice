def two_sum(nums, target):
    for i in range(len(nums)):
        if i + 1 < len(nums):
            if nums[i] + nums[i + 1] == target:
                print([i, i + 1])


def two_sum_different(nums, target):
    for i in nums:
        if i < target:
            if target - i in nums:
                print([nums.index(i), nums.index(target - i)])
                

def buy_and_sell_stock(prices):
    min_price = float('inf')
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i, price in enumerate(prices):
        if price < min_price:
            min_price = price
            buy_day = i
        elif price - min_price > max_profit:
            max_profit = price - min_price
            sell_day = i

    print(max_profit)
    print(f"Buy day: {buy_day}, Sell day: {sell_day}")

def duplicate_finder(nums):
    seen = set()
    if 1 <= len(nums) <= 1000:


        for num in nums:
            if num in seen:
                print(f"Duplicate found: {num}")
                return False
            seen.add(num)
        
        print("No duplicates found.")
        return True
    
    print("Input list unacceptable.")

def bit_constraint_no_division_attempt(nums):
    answer = 1
    answer_list = []
    for i in nums:
            answer *= i
    for i in nums:
        if i != 0:
            answer //= i
            answer_list.append(answer)
    return answer_list

def max_subarray_sum(nums):
    for i, num in enumerate(nums):
        if i == 0:
            max_sum = num
            current_sum = num
        else:
            current_sum = max(current_sum + num, num)
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

def main():
    nums = [1, 2, 3, 4]
    nums2 = [3, -2, 1, 1]
    nums3 = []
    print(max_subarray_sum(nums))
    print(max_subarray_sum(nums2))


main()