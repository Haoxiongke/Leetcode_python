class Solution:
    def hIndex(self, citations):
        """
        H指数
        :param citations: List[int]
        :return: int
        """
        res, length = 0, 0
        citations.sort(reverse=True)
        for i in citations:
            if i > res:
                length += 1
                res = min(length, i)
                if length == i:
                    return res
        # return res


if __name__ == "__main__":
    print(Solution().hIndex([3,0,6,1,5]))