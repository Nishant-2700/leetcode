class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        largest = nums[-1]
        second = nums[-2]
        third = nums[-3]
        smallest = nums[0]
        second_small = nums[1]
        product1 = largest * second * third
        product2 = smallest * second_small * largest
        if product1 > product2:
            return product1
        else:
            return product2 
    
    