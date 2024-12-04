class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        if needle in haystack:
            while i < len(haystack):
                if haystack[i:len(needle)+i] == needle:
                    return i
                i+=1
        else:
            return -1

if __name__ == "__main__":
    solution = Solution()
    haystack = "mississippi"
    needle = "issip"
    result = solution.strStr(haystack, needle)
    print(result)
