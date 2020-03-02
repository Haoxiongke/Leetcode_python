"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

# Solution1
# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     d = {}
#     for i, num in enumerate(nums):
#         if target - num in d:
#             # print(d)
#             return [d[target - num], i]
#         d[num] = i

# Solution2  ***best***
def twoSum(nums, target):
        mirrors = {}
        for idx,num in enumerate(nums):
            if num in mirrors:
                print(mirrors)
                return [mirrors[num],idx]
            mirrors[target - num] = idx

if __name__ == '__main__':
    print(twoSum([1,5,3,2],5))

