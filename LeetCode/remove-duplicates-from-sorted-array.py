from typing import List
# Need to review
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for n in range(1, len(nums)):

            if nums[n] != nums[n - 1]:
                nums[i] = nums[n]
                i += 1
        return i


if __name__ == "__main__":
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = solution.removeDuplicates(nums)
    print(result)
