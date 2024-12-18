# Need to review
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while left < right:
            width = right-left
            working_height = min(height[right], height[left])
            max_area = max(max_area, width*working_height)
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return max_area
if __name__ == "__main__":
    solution  = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    result = solution.maxArea(height)
    print(result)
