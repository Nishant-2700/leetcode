class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            sum_of_digit = 0
            
            if n in seen:
                return False

            seen.add(n)

            while n>0:
                digit = n%10
                square = pow(digit,2)
                sum_of_digit +=square
                n = n//10

            n =  sum_of_digit

        return True