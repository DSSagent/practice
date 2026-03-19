def two_sum(nums, target):
    for i in range(len(nums)):
        if i + 1 < len(nums):
            if nums[i] + nums[i + 1] == target:
                print([i, i + 1])
                


def main():
    nums = [2, 7, 11, 15]
    target = 9
    two_sum(nums, target)
    
main()