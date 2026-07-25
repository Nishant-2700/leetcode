class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        for i in nums1:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        ans = []
        count = 0
        for num in nums2:
            if num in freq and freq[num] > 0:
                ans.append(num)
                freq[num] -=1

        return ans