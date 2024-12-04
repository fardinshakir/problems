from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        dupes = {}
        while i < len(nums):
            if nums[i] in dupes.keys():
                nums.pop(i)

            else:
                dupes[nums[i]] = 1
                i +=1
        return len(nums)


if __name__ == "__main__":
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = solution.removeDuplicates(nums)
    print(result)
