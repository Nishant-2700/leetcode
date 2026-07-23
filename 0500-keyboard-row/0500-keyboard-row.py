class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        for word in words:
            lower = word.lower()
            valid = True
            if lower[0] in row1:
                for ch in lower:
                    if ch not in row1:
                        valid = False
                        break
                if valid:
                    ans.append(word)
            elif lower[0] in row2:
                for ch in lower:
                    if ch not in row2:
                        valid = False
                        break
                if valid:
                    ans.append(word)
            else:
                for ch in lower:
                    if ch not in row3:
                        valid = False
                        break
                if valid:
                    ans.append(word)
        return ans


