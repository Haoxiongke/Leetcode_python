"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

Note:
    1.The number of elements of the given matrix will not exceed 10,000.
    2.There are at least one 0 in the given matrix.
    3.The cells are adjacent in only four directions: up, down, left and right.
"""

class Solution():
    def updateMatrix(self, matrix):
        """
        matrix
        :param matrix: List[List[int]]
        :return: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        ans = matrix
        index_zero , none_zero = [],[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    index_zero.append((i, j))
                else:
                    none_zero.append((i, j))

        for i, j in none_zero:
            min_dist = m + n
            for l, k in index_zero:
                dist = abs(l - i) + abs(k - j)
                min_dist = min(dist, min_dist)
            ans[i][j] = min_dist
        return ans


class Solution2:
    def updateMatrix(self, matrix):
        """
        matrix
        :param matrix: List[List[int]]
        :return: List[List[int]]
        """
        import numpy as np

        matrix = np.array(matrix)
        ans = np.zeros(matrix.shape, dtype=int)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    ans[i][j] = 0
                else:
                    ans[i][j] = self.dfs(matrix, i, j)

        return ans

    def dfs(self, matrix, i, j):
        index_zero = []
        for m in range(len(matrix)):
            for n in range(len(matrix[m])):
                if matrix[m][n] == 0:
                    index_zero.append((m, n))

        min_dist = matrix.shape[0] + matrix.shape[1]
        for m, n in index_zero:
            dist = abs(m - i) + abs(n - j)
            min_dist = min(dist, min_dist)

        return min_dist
    
class Solution3:
    def updateMatrix(self, matrix):
        """
        matrix
        :param matrix: List[List[int]]
        :return: List[List[int]]
        """
        from collections import deque
        queue = deque([])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for i in range(len(matrix)):
          for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
              queue.append((i, j))
            if matrix[i][j] == 1:
              matrix[i][j] = -1

        while queue:
          i, j = queue.popleft()
          for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] == -1:
              matrix[ni][nj] = matrix[i][j] + 1
              queue.append((ni, nj))
        return matrix

class Solution4():
    def updateMatrix(self, matrix):
        """
        matrix
        :param matrix: List[List[int]]
        :return: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        ans = matrix
        index_zero , none_zero = [],[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    index_zero.append((i, j))
                else:
                    none_zero.append((i, j))

        while none_zero:
            i,j = none_zero.pop()
            min_dist = m + n
            for l, k in index_zero:
                dist = abs(l - i) + abs(k - j)
                min_dist = min(dist, min_dist)
            ans[i][j] = min_dist
        return ans

class Solution5(): # DP solution
    def updateMatrix(self, matrix):
        m,n = len(matrix),len(matrix[0])
        res = [[1000000 for i in range(n)] for j in range(m)]
        for i in range(m):  #First pass: check for left and top
            for j in range(n):
                if matrix[i][j]==0:
                    res[i][j] = 0
                else:
                    if i>0:
                        res[i][j] = min(res[i][j],res[i-1][j]+1)
                    if j>0:
                        res[i][j] = min(res[i][j],res[i][j-1]+1)
        for i in range(m-1,-1,-1): #Second pass: check for bottom and right
            for j in range(n-1,-1,-1):
                if i<m-1:
                    res[i][j] = min(res[i][j],res[i+1][j]+1)
                if j<n-1:
                    res[i][j] = min(res[i][j],res[i][j+1]+1)
        return res


if __name__ == '__main__':
    solu = Solution3()
    print(solu.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
