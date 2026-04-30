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

def max_subarray_product(nums):
    if len(nums) == 0 or len(nums) > 2 * 10**4:
        return None
    for i, num in enumerate(nums):
        if num <= -10 or num >= 10:
            return None
        if i == 0:
            max_product = num
            current_product = num
        else:
            current_product = max(current_product * num, num)
            if current_product > max_product:
                max_product = current_product
    return max_product

def min_sorted_rotated_array(nums):
    if len(nums) == 0 or len(nums) > 5000:
        return None
    for i, num in enumerate(nums):
        if num <= -5000 or num >= 5000:
            return None
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        print(f"Left: {left}, Mid: {mid}, Right: {right}")
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

def search_in_rotated_sorted_array(nums, target):
    if len(nums) == 0 or len(nums) > 5000:
        return None
    if nums[0] <= -10000 or nums[len(nums) - 1] >= 10000:
        return None
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1          
    return -1

def ThreeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

def main():
    nums = [1, 2, 3, 4]
    nums2 = [5,2,-7,-1,3,0,6,8]
    nums3 = [4,5,6,1,2,3]
    nums4 = [-3,2,5,-1]
    nums5 = [-10,11]
    print(ThreeSum(nums4))
    print(ThreeSum(nums2))


main()