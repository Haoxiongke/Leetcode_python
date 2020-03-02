"""
Problem:
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""


class Solution:
    def countSmaller(self, nums):
        """
        计算右侧小于当前元素的个数
        :param nums: List[int]
        :return: List[int]
        """
        res = []
        for index, num in enumerate(nums):
            lr = sorted(nums[index:])
            res.append(lr.index(num))

        return res

    def countSmaller2(self, nums):
        import bisect
        ans, bst = [], []
        for num in reversed(nums):
            idx = bisect.bisect_left(bst, num)
            ans.append(idx)
            bisect.insort(bst, num)
        return ans[::-1]


if __name__ == '__main__':
    print(Solution().countSmaller2([5, 2, 6, 1]))
