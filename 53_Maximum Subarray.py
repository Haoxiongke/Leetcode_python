"""
Question:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


class Solution:
    def maxSubArray1(self, nums):
        """
        最大子序和
        :param nums: list[int]
        :return: int
        """
        if len(nums) == 0:
            return 0
        preSum = maxSum = nums[0]
        for i in range(1, len(nums)):
            preSum = max(preSum + nums[i], nums[i])
            maxSum = max(maxSum, preSum)
        return maxSum

    def maxSubArray2(self, nums):
        """
        最大自序和
        :param nums: list[int]
        :return: int
        """
        if len(nums) == 0:
            return 0
        maxSum, ans = nums[0], 0

        for i in nums:
            if ans < 0:
                ans = 0
            ans += i
            maxSum = max(maxSum, ans)

        return maxSum


if __name__ == '__main__':
    solu = Solution()
    print(solu.maxSubArray2([1]))
