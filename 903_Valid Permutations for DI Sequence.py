"""
Problem:
We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

    If S[i] == 'D', then P[i] > P[i+1], and;
    If S[i] == 'I', then P[i] < P[i+1].

How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.

 

Example 1:

Input: "DID"
Output: 5
Explanation: 
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)

Note:

    1 <= S.length <= 200
    S consists only of characters from the set {'D', 'I'}.

"""

# time: O(n^2)
# space: O(n^2)
class Solution:
    def numPermsDISequence(self, S): 
        """
        DI 序列的有效排列
        S: str
        return: int
        """
        mod = 10 ** 9 + 7
        n = len(S)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[0][i] = 1
        
        for i,c in enumerate(S):
            if c == 'I':
                count = 0
                for j in range(n-i):
                    dp[i+1][j] = (count + dp[i][j]) % mod
                    count = dp[i+1][j]                                                
            else:
                count = 0
                for j in range(n-i-1,-1,-1):
                    dp[i+1][j] = (count + dp[i][j+1]) % mod
                    count = dp[i+1][j]
        
        return dp[n][0]


# time: O(n^2)
# space: O(n)
class Solution2:
    def numPermsDISequence(self, S: str) -> int:
        dp = [1] * (len(S) + 1)
        for c in S:
            if c == "I":
                dp = dp[:-1]
                for i in range(1, len(dp)):
                    dp[i] += dp[i - 1]
            else:
                dp = dp[1:]
                for i in range(len(dp) - 1)[::-1]:
                    dp[i] += dp[i + 1]
        return dp[0] % (10**9 + 7)

if __name__ == '__main__':
    print(Solution().numPermsDISequence("DID"))
    