from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                continue
            i+=1
        return i
if __name__ == "__main__":
    solution = Solution()
    nums = [2]
    val = 3
    result = solution.removeElement(nums, val)
    print(result)
