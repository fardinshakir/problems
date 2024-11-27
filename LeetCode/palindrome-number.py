class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 1:
            return True
        check = [int(i) for i in str(x)]
        inverse = check[::-1]

        for i in check:
            if check[i] == inverse[i]:
                pass
            else:
                return False
        return True


if __name__ == "__main__":
    solution  = Solution()
    number = 121
    result = solution.isPalindrome(number)
    print(result)
