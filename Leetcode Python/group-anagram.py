from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_ = ''.join(sorted(word))
            anagrams[sorted_].append(word)


        return list(anagrams.values())

if __name__ == "__main__":
    solution  = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    result = solution.groupAnagrams(strs)
    print(result)
