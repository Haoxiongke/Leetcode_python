"""
Problem:
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        寻找两个有序数组的中位数
        :param nums1: List[int]
        :param nums2: List[int]
        :return: float
        """
        num = sorted(nums1 + nums2)
        l = len(num)
        mid = int(l/2)
        if l % 2 == 0:
            return float((num[mid]+num[mid-1])/2)
        else:
            return float(int(num[mid]))


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 2],[3,4]))
