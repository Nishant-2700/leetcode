class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_list = max(nums)
        min_list = min(nums)
        for i in range(min_list,0,-1):
            if max_list %i == 0 and min_list %i == 0:
               return i
               

       

        