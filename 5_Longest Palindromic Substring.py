"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:
Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s):
        """        
        :type s: str
        :rtype: str
        """
        res = ""        
        for i in range(len(s)):                        
            tmp = self.helper(s,i,i)            
            #odd case like aba            
            if(len(tmp)>len(res)):                
                res = tmp                            
            
            tmp = self.helper(s,i,i+1)            
            #even case like abba            
            if(len(tmp)>len(res)):                
                res = tmp        
        
        return res                
        
        # get the longest palindrome, l, r are the middle indexes       
        # # from inner to outer                
    def helper(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:            
            l -=1            
            r +=1        
        return s[l+1:r]

if __name__ == "__main__":
    print(Solution().longestPalindrome('aba'))