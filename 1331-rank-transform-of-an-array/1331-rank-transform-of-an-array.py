class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique = sorted(set(arr))
        rank = {}
        current_rank = 1

        for num in unique:
            rank[num] = current_rank
            current_rank +=1

        answer = []

        for num in arr:
            answer.append(rank[num])

        return answer

        