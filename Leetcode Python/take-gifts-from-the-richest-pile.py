from typing import List
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
        while k:
            biggest = 0
            piles = [0]
            for i, j in enumerate(gifts):
                if gifts[i] > biggest:
                    biggest = gifts[i]
                    piles = [i]
                    continue
                elif gifts[i] < biggest:
                    continue
                elif gifts[i] == biggest:
                    piles.append(i)
                    continue
            biggest = int(biggest ** 0.5)
            gifts[piles[0]] = biggest
            k -=1
        return sum(gifts)
        """

        while k:
            gifts = sorted(gifts)[::-1]
            pile = gifts[0]
            gifts.pop(0)
            gifts.append(int(pile ** 0.5))
            k -=1
        return sum(gifts)
if __name__ == "__main__":
    solution = Solution()
    gifts = [25,64,9,4,100]
    k = 4
    result = solution.pickGifts(gifts, k)
    print(result)
