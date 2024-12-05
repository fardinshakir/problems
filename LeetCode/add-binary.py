# Need to review
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), 'b')
if __name__ == "__main__":
    solution = Solution()
    a ="11"
    b = "11"
    result = solution.addBinary(a, b)
    print(result)
