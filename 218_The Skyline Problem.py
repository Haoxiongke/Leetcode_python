"""
Problem:
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance.
Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A),
write a program to output the skyline formed by these buildings collectively (Figure B).

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building,
respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline.
A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline,
and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

    The number of buildings in any input list is guaranteed to be in the range [0, 10000].
    The input list is already sorted in ascending order by the left x position Li.
    The output list must be sorted by the x position.
    There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable;
    the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]


url: https://leetcode-cn.com/problems/the-skyline-problem/
"""

"""
1、基本的思想是对输入buildings做一个线性扫描，并且只处理它的两个点（即开始点和结束点）；
2、还有一个关键点是要使用一个优先队列(priority_queue)来记录所有处于"alive"状态的buildings（处于alive状态的建筑是指那么在后面的变量过程中可能会被使用到的建筑）；
3、优先队列需要根据高度和结束点x坐标来进行排序（优先队列的队首元素是高度值最大，如果存在高度值相同的点，结束点x坐标大的点位于队首）；
4、对buildings执行迭代操作，找到当前正在处理的点（即可能的拐点），当前正在处理的点要么是下一个building的开始点，要么是优先队列中队首元素的结束点；
5、如果当前的building的开始点的x坐标大于优先队列中队首元素的结束点x坐标，那么首先处理优先队列中的队首元素：将优先队列中的元素弹出直到它为空或者找到第一个结束点x坐标大于当前处理点的。
6、否则，如果当前的building的开始点x坐标小于等于优先队列中堆首元素的结束点x坐标，那么处理当前的building：将它的高度和结束点x坐标放到优先队列中；判断高度值是否发生了变化，如果发生了变化，将它放入到结果集中。
"""

import heapq

class Solution(object):
  def getSkyline(self, buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    hs = []
    heap = []
    for b in buildings:
      hs.append((b[0], -b[2]))
      hs.append((b[1], b[2]))
    hs.sort()
    ans = []
    pre = cur = None
    for h in hs:
      pos = h[0]
      height = h[1]
      if height < 0:
        heapq.heappush(heap, height)
      else:
        i = heap.index(-height)
        heap[i] = heap[-1]
        heap.pop()
        if i < len(heap):
          heapq._siftup(heap, i)
          heapq._siftdown(heap, 0, i)
      if heap:
        cur = heap[0]
        if cur != pre:
          ans.append((pos, -1 * cur))
          pre = cur
      else:
        ans.append((pos, 0))

    return ans


  def getSkyline2(self, buildings):
      events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
      res, hp = [[0, 0]], [(0, float("inf"))]
      for x, negH, R in events:
          while x >= hp[0][1]:
              heapq.heappop(hp)
          if negH:
              heapq.heappush(hp, (negH, R))
          if res[-1][1] + hp[0][0]:
              res += [x, -hp[0][0]],
      return res[1:]


if __name__ == '__main__':
    print(Solution().getSkyline2([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))