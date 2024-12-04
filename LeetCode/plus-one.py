from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        number = 0
        for i, n in enumerate(digits):
            if i > 0:
                number += n * (10**i)
            else:
                number += n
        number +=1
        value = [int(n) for n in str(number)]
        return value
if __name__ == "__main__":
    solution = Solution()
    digits = [9]
    result = solution.plusOne(digits)
    print(result)
