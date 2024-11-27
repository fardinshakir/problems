from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myvalues = {}
        for i, num in enumerate(nums):
            check = target - num
            #print(f"{check} = {target} - {num}")
            if check in myvalues:
                return [myvalues[check], i]

            myvalues[num] = i

if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)
