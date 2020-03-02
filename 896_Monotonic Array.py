'''
Question:
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:

Input: [1,2,2,3]
Output: true

Example 2:

Input: [6,5,4,4]
Output: true


Note:

The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
'''


class Soulution():
    def isMonotonic1(self, A):
        """
        数列单调问题:利用排序解决
        :param A:
        :return:
        """
        return A == sorted(A) or A == sorted(A, reverse=True)

    def isMonotonic2(self, A):
        """
        数列单调问题：利用相邻值比较
        :param A:
        :return:
        """
        if len(A) == 1:
            return True
        else:
            return self.increase(A) or self.decrease(A)

    def increase(self, A):
        return all(A[i] <= A[i + 1] for i in range(len(A)-1))

    def decrease(self, A):
        return all(A[i] >= A[i + 1] for i in range(len(A)-1))


if __name__ == "__main__":
    solu = Soulution()
    print(solu.isMonotonic2([1,2,3]))
