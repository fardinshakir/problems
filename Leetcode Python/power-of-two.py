class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n != 2:
            if n == 2 or n == 1:
                return True
            if n % 2 != 0 or n <= 0:
                return False
            else:
                n = int(n/2)
        return True

if __name__ == "__main__":
    solution = Solution()
    n = 49201237895324
    result = solution.isPowerOfTwo(n)
    print(result)
