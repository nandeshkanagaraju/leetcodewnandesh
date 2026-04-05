class Solution(object):
    def topKFrequent(self, nums, k):
        cnt = Counter(nums)
        ans = heapq.nlargest(k, cnt, key=cnt.get)

        return list(ans)




