class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        total = sum(nums)
        lsum = 0

        expected = n * (n + 1) // 2
        
        return expected-total


        