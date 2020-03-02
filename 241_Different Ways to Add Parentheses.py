"""
Problem:
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators.
The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
"""


class Solution:
    def diffWaysToCompute(self, input):
        """
        为运算表达式设计优先级
        :param input: str
        :return: List[int]
        """
        m = {}

        res = []
        for i, c in enumerate(input):
            if c == '-' or c == '+' or c == '*':
                lefts = self.diffWaysToCompute(input[0:i])
                rights = self.diffWaysToCompute(input[i + 1:])

                for left in lefts:
                    for right in rights:
                        res.append(eval(str(left) + c + str(right)))

        if not res: # 放在后面防止出现'11'这样的数字
            res.append(int(input))


        return res

if __name__ == '__main__':
    print(Solution().diffWaysToCompute("11"))
