from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        current = set()
        for number in nums:
            if number in current:
                return True
            else:
                current.add(number)
        return False
if __name__ == "__main__":
    solution  = Solution()
    number = [2,14,18,22]
    result = solution.containsDuplicate(number)
    print(result)
