class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        holder = 0
        longest = 0
        my_vals = {}

        start = 0
        for i, c in enumerate(s):
            if c in my_vals and my_vals[c] >= start:
                start = my_vals[c] + 1

            my_vals[c] = i
            holder = i - start + 1
            longest = max(longest, holder)
        return longest

if __name__ == "__main__":
    solution = Solution()
    s = "aababcabcd"
    result = solution.lengthOfLongestSubstring(s)
    print(result)
