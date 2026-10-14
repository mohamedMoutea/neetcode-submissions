class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            max_1 = - heapq.heappop(maxHeap)
            max_2 = - heapq.heappop(maxHeap)
            if max_2 < max_1: 
                val = -(max_1 - max_2)
                heapq.heappush(maxHeap,val)
        
        maxHeap.append(0)
        return abs(maxHeap[0]) 

        

        