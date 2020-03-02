"""
Question:
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has,
please find out a way you can make one square by using up all those matchsticks. You should not break any stick,
but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length.
Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
"""

class Solution:
    def makesquare(self, nums):
        total, n = sum(nums), len(nums)
        if total % 4 != 0 or n < 4: return False
        target = total/4
        nums.sort(reverse=True)  # 降序排序
        used = [False] * n  # 记录

        def dfs(i, tar):  # 判断数字 i, 是否可以组成长为tar， 的边
            print(i,"******",n)
            if i >= n: return tar % target == 0
            if used[i]: return dfs(i+1, tar)  # 当前位置已经使用，跳到下个位置
            used[i] = True  # 位置 i 的值没有过，现在使用
            if nums[i] == tar: return True
            if nums[i] < tar:
                tar -= nums[i]
                not_used = [j for j in range(i+1, n) if not used[j]]  # 记录没有使用过的位置
                for x in not_used:
                    if dfs(x, tar):
                        return True
            used[i] = False  # 恢复未使用状态
            return False

        for i in range(n):  # 遍历所有元素，确保每一个元素都可以分配边
            if not dfs(i, target): return False
        return True


if __name__ == '__main__':
    nums = [2, 1, 2, 1, 2, 2, 1, 2, 1, 2]
    solu = Solution()
    print(solu.makesquare(nums))
