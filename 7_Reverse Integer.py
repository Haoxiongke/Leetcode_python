"""
Problem:
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        整数反转
        :param x: int
        :return: int
        """
        flag = False
        if x < 0:
            x = -x
            flag = True
        str_x = str(x)
        res = []
        for i in range(len(str_x) - 1, -1, -1):
            res.append(str_x[i])
        str_res = int(''.join(res)) if not flag else -int(''.join(res))
        return 0 if str_res < (-2)**31 or str_res > (2**31 - 1) else str_res

    def reverse2(self, x):
        x = int(str(x)[::-1]) if x >= 0 else - int(str(-x)[::-1])
        return x if x < (2**31 -1) and x >= (-2**31) else 0


if __name__ == '__main__':
    print(Solution().reverse2(1534236469))
