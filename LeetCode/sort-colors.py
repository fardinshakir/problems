from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n):
            for j in range(1, n - i):
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]

        return nums

if __name__ == "__main__":
    solution  = Solution()
    nums = [2,0,2,1,1,0]
    result = solution.sortColors(nums)
    print(result)
