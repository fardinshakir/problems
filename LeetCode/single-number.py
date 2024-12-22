from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n) == 1:
                return n

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2, 6, 6]
    result = solution.singleNumber(nums)
    print(result)
