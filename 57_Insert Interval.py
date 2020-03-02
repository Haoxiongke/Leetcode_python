"""
Question:
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""


class Solution:
    def insert(self, intervals, newInterval):
        """
        插入区间
        :param intervals: List[List[int]]
        :param newInterval: List[int]
        :return: List[List[int]]
        """
        start, end = newInterval[0], newInterval[1]
        l, r = [], []
        for interval in intervals:
            if interval[1] < start:
                l.append(interval)
            elif interval[0] > end:
                r.append(interval)
            else:
                start = min(start, interval[0])
                end = max(end, interval[1])
        return l + [[start, end]] + r


if __name__ == '__main__':
    solu = Solution()
    print(solu.insert([[1, 3], [6, 9]], [2, 5]))
