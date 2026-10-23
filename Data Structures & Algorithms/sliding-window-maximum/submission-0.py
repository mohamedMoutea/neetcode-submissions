class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l,r = 0,k-1
        maxx = 0
        for i in range(k):
            if nums[i] > maxx:
                maxx = nums[i] 
        while r < len(nums):
            if nums[r] > maxx:
                maxx = nums[r]
            
            r +=1
            l += 1
            res.append(maxx)
        return res


        