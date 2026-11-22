class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        heap = []
        for key, value in freqMap.items():
            heap.append((-1 * value, key))

        heapq.heapify(heap)
        res = []
        for i in range(k):
            value, key = heapq.heappop(heap)
            res.append(key)

        return res