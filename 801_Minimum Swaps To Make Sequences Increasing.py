"""
Problem:
We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.

Note:

    A, B are arrays with the same length, and that length will be in the range [1, 1000].
    A[i], B[i] are integer values in the range [0, 2000].

"""

"""
解题思路：
利用动态规划,存储当前遍历的节点变还是不变，保存
"""


class Solution:
    def minSwap(self, A, B):
        """      
        使序列递增的最小交换次数
        :param A: List[int]
        :param B: List[int]
        :return: int       
        """
        cost = [0, 1]
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                if A[i] > B[i - 1] and B[i] > A[i - 1]:
                    cost = [min(cost), min(cost) + 1]
                else:
                    cost[1] += 1
            else:
                cost = [cost[1], cost[0] + 1]
        return min(cost)

    def minSwap2(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        N = len(A)
        keep = [float('inf')] * N
        swap = [float('inf')] * N
        keep[0] = 0
        swap[0] = 1
        for i in range(1, N):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)

        return min(keep[N - 1], swap[N - 1])

    def minSwap3(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        N = len(A)
        keep, swap = 0, 1
        for i in range(1, N):
            curswap, curkeep = float('inf'), float('inf')
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                curkeep, curswap = keep, swap + 1
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                curkeep, curswap = min(curkeep, swap), min(curswap, keep + 1)
            keep, swap = curkeep, curswap
        return min(keep, swap)


if __name__ == "__main__":
    print(Solution().minSwap([1, 3, 8], [2, 6, 7]))
