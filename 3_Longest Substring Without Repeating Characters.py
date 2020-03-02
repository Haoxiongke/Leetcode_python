"""
Problem:
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):  # 时间复杂度太高，超时
        """
        无重复字符的最长子串
        :param s: str
        :return: int
        """
        if len(s) == 1:
            return 1
        num = 0
        for i, k in enumerate(s):
            res = []
            for j, l in enumerate(s[i:]):
                if j == len(s[i:]) - 1:
                    if l in res:
                        num = max(len(res), num)
                    else:
                        num = max(len(s[i:]),num)
                else:
                    if l in res:
                        num = max(len(res), num)
                        break
                    else:
                        res.append(l)
        return num

    def lengthOfLongestSubstring2(self, s): # 满足要求
        res = []
        num = 0
        for i,k in enumerate(s):
            if k in res:
                while k in res:
                    res.pop(0)
                res.append(k)
            else:
                res.append(k)
            num = max(num,len(res))
            # print(num,res)

        return num

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring2(" a"))
