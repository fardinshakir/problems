# Need to solve
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1].lower()
        print(s)
        word = ""
        i = 0
        found = False
        while found is not True:
            try:
                if s[i].isalnum():
                    word += s[i]
                else:
                    if s[i+1] == " ":
                        i +=1
                    elif s[i+1].isalnum():
                        return True
                i += 1
            except:
                return len(s)
        return len(word)
if __name__ == "__main__":
    solution = Solution()
    s = "Racecar aw  "
    result = solution.lengthOfLastWord(s)
    print(result)
