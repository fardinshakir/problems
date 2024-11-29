class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        anagram = []
        if len(s) != len(t):
            return False
        for i,letter in enumerate(s):
            if letter in t and s.count(letter) == t.count(letter):
                anagram.append(True)
            else:
                anagram = []

        if len(anagram) != len(s):
            return False
        else:
            return True

        """
        if sorted(s) == sorted(t):
            return True
        else:
            return False
if __name__ == "__main__":
    solution  = Solution()
    s = "anagram"
    t = "nagaram"
    result = solution.isAnagram(s, t)
    print(result)
