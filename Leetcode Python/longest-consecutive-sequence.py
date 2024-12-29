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

if __name__ == "__main__":
    solution  = Solution()
    nums = [0,3,7,2,5,8,4,6,0]

    result = solution.longestConsecutive(nums)
    print(result)
