class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i, character in enumerate(s):
            curr = numbers.get(character)
            if i > 0:
                prev = numbers.get(s[i-1])
                if curr - prev > 0:
                    number += (curr-2*prev)
                else:
                    number += curr

            else:
                number += curr

        return number
if __name__ == "__main__":
    solution  = Solution()
    number = "MCMXCIV"
    result = solution.romanToInt(number)
    print(result)
