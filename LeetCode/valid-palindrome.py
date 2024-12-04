class Solution:
    def isPalindrome(self, s: str) -> bool:
        mstr = ""
        for c in s.lower():
            if c.isalnum():
                mstr+= c
        return mstr == mstr[::-1]



if __name__ == "__main__":
    solution = Solution()
    s = "Racecar"
    result = solution.isPalindrome(s)
    print(result)
