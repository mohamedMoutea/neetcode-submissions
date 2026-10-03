class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        count=1
        countp = 1

        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            if (nums[i+1] - nums[i] ) == 1:
                count +=1
            else:
                if count> countp:
                    countp = count
                    count = 1
                else:
                    count = 1
        
        max_seq = max(count,countp)
        return max_seq 
        


 
        