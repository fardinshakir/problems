class Solution:
    def mySqrt(self, x: int) -> int:
        if x == "0":
            return 1
        elif x < 0:
            return False
        left, right = 0, x
        while left <= right:
            mid = (left+right)//2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
if __name__ == "__main__":
    solution = Solution()
    x = 8
    result = solution.mySqrt(x)
    print(result)
