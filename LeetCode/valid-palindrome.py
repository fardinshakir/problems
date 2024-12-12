class Solution:
    def isPalindrome(self, s: str) -> bool:
        #mstr = ""
        #for c in s.lower():
        #    if c.isalnum():
        #        mstr+= c
        #return mstr == mstr[::-1]

        #return s.lower() == s[::-1].lower()
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum(): l+=1
            while l < r and not s[r].isalnum(): r-=1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    s = "A man, a plan, a canal: Panama"
    result = solution.isPalindrome(s)
    print(result)
