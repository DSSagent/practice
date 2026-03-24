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

def bit_constraint_no_division(nums):
    answer = {}
    answer_piece = 0
    counter = 0
    l, r = 0, 1
    while r < len(nums) :
        if counter == 0:
            l = 0
            r = 1
        for i in range(len(nums)):
            if nums[i] == nums[l] + nums[r]:
                answer[answer_piece] = [l, r]
                answer_piece += 1
                l += 1
                r += 1
                break
        if counter == len(nums) - 1:
            counter += 1
            break
    return answer
        
def main():
    nums = [2, 7, 11, 15]
    nums2 = [3, 2, 4, 2]
    nums3 = []
    print(bit_constraint_no_division(nums))


main()