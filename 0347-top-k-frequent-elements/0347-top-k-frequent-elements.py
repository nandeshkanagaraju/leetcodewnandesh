class Solution(object):
    def topKFrequent(self, nums, k):
        cnt = Counter(nums).most_common(k)

        return [num for num, freq in cnt]




