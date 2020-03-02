"""
Problem:
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums):  # 因为题目要求重要的个数要大于n/2，故众数只有一个。所以可以利用排序解决问题
        """
        求众数
        :param nums: List[int]
        :return: int
        """
        dic = dict()
        l = len(nums) / 2
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1

        for i in dic:
            if dic[i] > l:
                return i

    def majorityElement2(self, nums):
        """
        求众数
        :param nums: List[int]
        :return: int
        """
        return sorted(nums)[len(nums) // 2]

if __name__ == '__main__':
    print(Solution().majorityElement([2,2,1,1,1,2,2]))

