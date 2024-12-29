# Need to review
class Solution:
    def climbStairs(self, n: int) -> int:
# Dynamic programming

                if n <= 3:
                    return n
                pre1 = 3
                pre2 = 2
                cur = 0
                for _ in range(3, n):
                    cur = pre1 + pre2
                    pre2 = pre1
                    pre1 = cur
                return cur

# Recursion
"""
        if n == 1:
            return 1
        if n == 2:
            return 2
        my_val = self.climbStairs(n-1) + self.climbStairs(n-2)
        print(my_val)
        return my_val
"""
if __name__ == "__main__":
    solution = Solution()
    n = 5
    result = solution.climbStairs(n)
    print(result)
