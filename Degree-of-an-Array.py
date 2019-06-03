class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first,last = {},{}
        for i, v in enumerate(nums):
            first.setdefault(v,i)
            last[v] = i
        c = collections.Counter(nums)
        print(c)
        degree = max(c.values())
        print(degree)
        return min(last[v]-first[v]+1 for v in c if c[v]== degree)
