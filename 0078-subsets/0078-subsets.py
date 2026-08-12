class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def Backtrack(start,path):
            res.append(path.copy())

            for i in range(start,len(nums)):
                path.append(nums[i])
                Backtrack(i+1,path)
                path.pop()

        Backtrack(0,[])
        return res


        # n = len(nums)
        # subsets = []

        # for i in range(1<<n):
        #     subset = []

        #     for j in range(n):
        #         if i & (1<<j):
        #             subset.append(nums[j])
        #     subsets.append(subset)

        # return subsets
