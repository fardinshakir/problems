from typing import List
# Need to review
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1] * n, [1] * n
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        print(left, right)
if __name__ == "__main__":
    solution  = Solution()
    nums = [1,2,3,4]
    result = solution.productExceptSelf(nums)
    print(result)
