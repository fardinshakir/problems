class Solution:
    def isHappy(self, n: int) -> bool:
        appeared = set()
        sum = 0
        while sum != 1:
            list_num = [int(i) for i in str(n)]
            for n in list_num:
                sum += n**2
            if sum in appeared:
                return False
            else:
                appeared.add(sum)
            if sum == 1:
                return True
            n = sum
            sum = 0
