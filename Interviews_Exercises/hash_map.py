def twoSum(nums, target):
    hashMap = {}  # val : index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[n] = i
    return


nums = [1, 4, 7, 9]
target = 11
a = twoSum(nums, target)
print(a)
print(nums[a[0]] + nums[a[1]])
