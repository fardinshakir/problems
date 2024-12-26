class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        new = 0
        q = 5
        while len(str(num)) != 1:

            for n in str(num):
                new += int(n)
            num = new
            new = 0
            q -= 1
        return int(num)



if __name__ == "__main__":
    solution = Solution()
    num = 0
    result = solution.addDigits(num)
    print(result)
