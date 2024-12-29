from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    result = solution.search(nums, target)
    print(result)
