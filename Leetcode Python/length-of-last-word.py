class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()

        if not words:
            return 0

        return len(words[-1])
if __name__ == "__main__":
    solution = Solution()
    s = "Hello World"
    result = solution.lengthOfLastWord(s)
    print(result)
