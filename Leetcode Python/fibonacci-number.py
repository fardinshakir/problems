class Solution:
    def fib(self, n: int) -> int:
        prev, cur = 0, 1
        for q in range(0, n):
            oldcur = cur
            cur = cur + prev
            prev = oldcur
        return prev

if __name__ == "__main__":
    solution  = Solution()
    n = 8
    result = solution.fib(n)
    print(result)
