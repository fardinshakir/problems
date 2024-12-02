from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = set(sorted(nums))
        longest = 0
        for n in sorted_nums:
            if n-1 not in sorted_nums:
                length = 1
                while n+length in sorted_nums:
                    length+=1
                longest = max(longest, length)
        return longest

"""
        start = sorted_nums[0]
        longest = 1
        for i, n in enumerate(sorted_nums[1:]):
            #print(f"{i}, {sorted_nums[1:][i]} - {start} = {sorted_nums[1:][i] - start}")
            if sorted_nums[1:][i] - start == 1:
                start = sorted_nums[1:][i]
                longest += 1
            else:
                start = sorted_nums[1:][i]
                longest = 1
        return longest
"""
if __name__ == "__main__":
    solution  = Solution()
    nums = [0,3,7,2,5,8,4,6,0,1, 1, 1]

    result = solution.longestConsecutive(nums)
    print(result)
