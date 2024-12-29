from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        mylist = []
        for num in range(1, n+1):
            output = ""
            if num % 3 == 0:
                output += 'Fizz'
            if num % 5 == 0:
                output += 'Buzz'
            if not output:
                output = str(num)
            mylist.append(output)
        return mylist
if __name__ == "__main__":
    solution  = Solution()
    n = 3
    result = solution.fizzBuzz(n)
    print(result)
