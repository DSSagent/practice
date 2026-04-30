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

def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(result)

main()