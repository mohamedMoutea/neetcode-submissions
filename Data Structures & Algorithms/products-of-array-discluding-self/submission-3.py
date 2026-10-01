class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        point = 0
        output = [1]* len(nums)

        while point < len(nums):
            for i , val in enumerate(nums):
                if i != point:
                   output[point] = output[point] * val 
                
            point += 1
        return output 



        