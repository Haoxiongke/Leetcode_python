"""
Problem:
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

"""
solution:
翻译过来：

    先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
    再找出另一个最大索引 l 满足 nums[l] > nums[k]；
    交换 nums[l] 和 nums[k]；
    最后翻转 nums[k+1:]。
"""

class Solution:
    def nextPermutation(self, nums):
        """
        :param nums: List[int]
        Do not return anything, modify nums in-place instead.
        """
        firstIndex = -1
        n = len(nums)

        def reverse(nums,i,j):
            while i < j :
                nums[i],nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                firstIndex = i
                break
        
        if firstIndex == -1:
            reverse(nums,0,n-1)
            return nums
        
        secondIndex = -1
        for j in range(n-1,-1,-1):
            if nums[j] > nums[firstIndex]:
                secondIndex = j
                break
        
        nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]

        reverse(nums,firstIndex+1,n-1)

        return nums

if __name__ == "__main__":
    print(Solution().nextPermutation([1,1,5]))
        