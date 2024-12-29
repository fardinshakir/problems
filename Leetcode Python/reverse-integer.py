class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            mult = -1
            x = str(x)[1:]
        elif x > 0:
            mult = 1
            x = str(x)
        else:
            return 0
        new = ""
        for n in x:
            new = n + new
        new = int(new.strip('0'))*mult
        if new < -2**31 or new > 2**31-1:
            return 0
        return new
if __name__ == "__main__":
    solution = Solution()
    x =
    result = solution.reverse(x)
    print(result)
