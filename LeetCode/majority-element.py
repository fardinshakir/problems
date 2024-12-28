from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res = major = 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > major:
                res = n
                major = count[n]
        return res
if __name__ == "__main__":
    solution = Solution()
    nums = [6,5,5]
    result = solution.majorityElement(nums)
    print(result)
