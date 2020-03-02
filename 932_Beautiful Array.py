"""
Problem:
For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)

Example 1:

Input: 4
Output: [2,1,4,3]

Example 2:

Input: 5
Output: [3,1,2,5,4]

Note:

    1 <= N <= 1000
"""

"""
解题思路：
漂亮数组中任一一个元素加减乘后得到的数组任然是漂亮数组

1、迭代生成，左边生成奇数数组，右边生成偶数数组，左右两边的数组均是漂亮数组，保证拼接后的数组任然是漂亮数组
2、成倍的生成数组，然后删除掉数组中超过N范围的数组
"""


class Solution:
    def beautifulArray(self, N):
        """
        漂亮数组
        :param N: int
        :return: List[int]
        """
        res = [1]
        while len(res) < N:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]

        return [i for i in res if i <= N]

    def beautifulArray2(self, N):
        """
        漂亮数组
        :param N: int
        :return: List[int]
        """
        if N == 1:
            return [1]
        odd = [i * 2 - 1 for i in self.beautifulArray(N / 2 + N % 2)]
        even = [i * 2 for i in self.beautifulArray(N / 2)]
        return odd + even

    def beautifulArray3(self, N): # 法三 利用二进制进行奇偶数的排序
        return sorted(range(1, N + 1), key=lambda x: bin(x)[:1:-1])


if __name__ == '__main__':
    print(Solution().beautifulArray(5))
    print(Solution().beautifulArray2(5))
    print(Solution().beautifulArray3(8))
