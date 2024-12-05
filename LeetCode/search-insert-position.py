from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] <= target <= nums[-1]:
            try:
                return nums.index(target)
            except:
                i = 0
                while i < len(nums):
                    if target == nums[i]:
                        return i + 1
                    elif nums[i] <= target <= nums[i+1]:
                        return i + 1
                    i += 1
        elif target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 3, 4, 5]
    target = 2
    result = solution.searchInsert(nums, target)
    print(result)
