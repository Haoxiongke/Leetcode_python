"""
Probelm:
need to find the minimum number of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key one by one by
rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

    You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step.
    The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
    If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step.
    After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.

Example:
Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.
"""

# import collections

class Solution:
    def findRotateSteps(self, ring, key): # 利用python写超时，利用C++和java写可以在时间范围内
        """
        自由之路
        :param ring: str
        :param key: str
        :return: int
        """
        m = len(key)
        n = len(ring)

        dp = [[0] * (n) for _ in range(m+1)]

        for i in range(m-1,-1,-1):
            for j in range(n):
                dp[i][j] = 10000
                for k in range(n):
                    if ring[k] == key[i]:
                        dis = abs(j-k)
                        step = min(dis, n-dis)
                        # print(dp[i][k])
                        dp[i][j] = min(dp[i][j],step+dp[i+1][k])

        return dp[0][0] + m

    def findRotateSteps2(self, ring, key):
        """
        自由之路
        :param ring: str
        :param key: str
        :return: int
        """
        m = len(key)
        n = len(ring)

        dp = [[0] * n for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(n):
                dp[i][j] = 10000
                for k in range(n):
                    if ring[k] == key[m-i]:
                        dis = abs(j - k)
                        step = min(dis,n-dis)
                        dp[i][j] = min(dp[i][j],step + dp[i-1][k])

        print(dp)
        return dp[m][0] + m

if __name__ == "__main__":
    print(Solution().findRotateSteps2("godding","gd"))
