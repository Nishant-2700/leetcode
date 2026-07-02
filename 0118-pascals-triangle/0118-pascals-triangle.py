class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for row in range (1,numRows):
            previous  = result[-1]
            current  = [1]
            for i in range(len(previous)-1):
                current.append(previous[i]+previous [i+1])

            current.append(1)
            result.append(current)
        return result



            

        return 
