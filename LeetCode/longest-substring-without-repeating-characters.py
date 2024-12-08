# Need to solve
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        holder = 1
        longest = []
        my_vals = {}
        for i, c in enumerate(s):
            print(c, holder, longest)
            print(my_vals)
            if c in my_vals or c == s[-1]:
                longest.append(holder)
                holder = 1
                my_vals = {}

            elif c not in my_vals:
                holder += 1
                my_vals[c] = 1

        print(longest)
        return max(longest)

if __name__ == "__main__":
    solution = Solution()
    s = ""
    result = solution.lengthOfLongestSubstring(s)
    print(result)
