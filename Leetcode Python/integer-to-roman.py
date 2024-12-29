class Solution:
    def intToRoman(self, num: int) -> str:
        """ v1
        roman = ''
        if num >= 1000:
            roman += (num // 1000) * 'M'
            num -= (num // 1000) * 1000

        if num >= 900:
            roman += 'CM'
            num -= 900
        elif num >= 500:
            roman += 'D'
            num -= 500
        elif num >= 400:
            roman += 'CD'
            num -= 400
        if num >= 100:
            roman += (num // 100) * 'C'
            num -= (num // 100) * 100

        if num >= 90:
            roman += 'XC'
            num -= 90
        elif num >= 50:
            roman += 'L'
            num -= 50
        elif num >= 40:
            roman += 'XL'
            num -= 40
        if num >= 10:
            roman += (num // 10) * 'X'
            num -= (num // 10) * 10

        if num >= 9:
            roman += 'IX'
            num -= 9
        elif num >= 5:
            roman += 'V'
            num -= 5
        elif num >= 4:
            roman += 'IV'
            num -= 4

        if num >= 1:
            roman += num * 'I'
            num -= num

        return roman
        """
        # v2
        roman_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        roman = ''
        for value, symbol in roman_map:
            count = num // value
            roman += symbol * count
            num -= value * count
        return roman

if __name__ == "__main__":
    solution = Solution()
    num = 972
    result = solution.intToRoman(num)
    print(result)
