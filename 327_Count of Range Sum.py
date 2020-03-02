"""
Problem:
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
"""


class Solution:
    def countRangeSum(self, nums, lower, upper):
        """
        区间和的个数
        :param nums: List[int]
        :param lower: int
        :param upper: int
        :return: int
        """
        sums = [0]
        for i in nums:
            sums.append(sums[-1] + i)


        def sort(lo, hi):
            if hi - lo <= 1:  # 如果数组只有一个数，那么下面的算法将不能比较出来，还会将数组长度退化成1，在下面的 sort 会栈溢出
                return 0

            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid, hi)
            i = j = mid  # 放在for 循环的外面，已经计算过的就不再重复，减少计算量
            for left in sums[lo:mid]:  # 对于 lo:mid 和 mid:hi 的所有情况已经在递归中全部计算过了，现在只有右边减去左边的可能没有出现过
                while i < hi and sums[i] - left < lower: i += 1
                while j < hi and sums[j] - left <= upper: j += 1
                count += j - i
            sums[lo:hi] = sorted(sums[lo:hi])  # 如果不排序，就会出现前面较大的数sums[h] (h >=mid)
            # 在索引低位的数 left计算失败后，left后移，而后面较小的数 sums[h+1] 计算不到 left 的情况的情况
            return count

        return sort(0, len(sums))

    def countRangeSum2(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        import bisect
        prefix, thisSum, ans = [0], 0, 0
        for n in nums:
            thisSum += n
            ans += bisect.bisect_right(prefix, thisSum - lower) - bisect.bisect_left(prefix, thisSum - upper)
            bisect.insort(prefix, thisSum)
        return ans

if __name__ == "__main__":
    print(Solution().countRangeSum([-1, 5, -2], -2, 2))
