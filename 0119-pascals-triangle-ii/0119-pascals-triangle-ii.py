class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        current = [1]
        for row in range(rowIndex):
            previous = current
            current = [1]
            for i in range(len(previous)-1):
                sum = previous[i] + previous [i+1]
                current.append(sum)

            current.append(1)

        return current  








        return current

            