from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        test = [1,2,3,4,5]
        map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for character in s:
            if character in map.values():
                stack.append(character)
            elif character in map.keys():
                if not stack or map[character] != stack.pop():
                    return False

        return not stack
if __name__ == "__main__":
    solution  = Solution()
    input = "()"
    result = solution.isValid(input)
    print(result)
