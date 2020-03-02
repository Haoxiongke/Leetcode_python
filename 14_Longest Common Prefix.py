"""
Problem：
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix1(self, strs):
        """
        最大子前缀
        :param strs: List[str]
        :return: str
        """
        if (len(strs) == 0):
            return ''
        i, j, end = 0, 0, 0
        while j < len(strs) and i < len(strs[j]):
            if j == 0:
                char = strs[j][i]
            else:
                if char != strs[j][i]:
                    break

            if j == len(strs) - 1:
                i += 1
                j = 0
                end += 1
            else:
                j += 1
        return strs[j][:end]

    def longestCommonPrefix2(self, strs): # 利用python特性进行排序，比较第一个和最后一个的前缀
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        print(strs)
        p = ''
        for x, y in zip(strs[0], strs[-1]):
            print(x,y)
            if x == y:
                p += x
            else:
                break
        return p

    def longestCommonPrefix3(self, strs):
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        p = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                p += list(set(i))[0]
            else:
                break
        return p


if __name__ == '__main__':

    solu = Solution()
    print(solu.longestCommonPrefix3(["flower","flow","flight"]))