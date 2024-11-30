from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_freq = {}
        for i in nums:
            if i in most_freq:
                most_freq[i] += 1
            else:
                most_freq[i] = 1
        q = sorted(most_freq.items(), key = lambda item: item[1], reverse=True)
        list = []
        for items in q:
            list.append(items[0])

        return list[:k]

if __name__ == "__main__":
    solution  = Solution()
    #nums = [-1, -1]
    nums = [1,1,1,2,2,3]
    k = 2
    result = solution.topKFrequent(nums, k)
    print(result)
