"""
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  
Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

Note:

    1 <= time.length <= 60000
    1 <= time[i] <= 500

"""

class Solution1:
    def numPairsDivisibleBy60(self, time):
        """
        总持续时间可被 60 整除的歌曲
        :param time: List[int]
        :return: int
        """
        num = 0
        for i in range(len(time)):
            for j in range(i+1,len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    num += 1
        return num

class Solution2:
    def numPairsDivisibleBy60(self, time):
        """
        总持续时间可被 60 整除的歌曲
        :param time: List[int]
        :return: int
        """
        res = 0
        hashmap = dict().fromkeys([i for i in range(60)],0)
        for t in time:
            res += hashmap[(60 - t%60)%60]
            hashmap[t%60] += 1
        return res


from collections import defaultdict
class Solution3:   
    def numPairsDivisibleBy60(self, time):
        d = defaultdict(int)
        for t in time:
            d[t%60] += 1
        res = 0
        #print(d)
        for k in d.keys():
            if k != 0 and k != 30:
                res += d.get(60-k, 0) * d[k]
        res = res // 2
        res += d[0] * (d[0]-1) // 2
        res += d[30] * (d[30]-1) // 2
        return res


if __name__ == '__main__':
    print(Solution3().numPairsDivisibleBy60([20,40]))
    