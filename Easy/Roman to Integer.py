"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
"""

def romanToInt(self, s: str) -> int:
    roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }




    """
    buf = 0
    for i, letter in enumerate(s):
        if buf != 0:
            num += (roman[letter] - roman[s[i - 1]])
            buf = 0
        elif i + 1 < len(s):
            if roman[letter] >= roman[s[i + 1]]:
                num += roman[letter]
                buf = 0
            else:
                buf = roman[letter]
        else:
            num += roman[letter]
        print("i = ", i, "num = ", num, "buf = ", buf)
    return num
    """

    # go backwards
    num = 0
    i = len(s) - 1
    while i >= 0:
        if i-1 >= 0 and roman[s[i-1]] < roman[s[i]]:
            num += (roman[s[i]] - roman[s[i-1]])
            i -= 2
        else:
            num += roman[s[i]]
            i -= 1
    return num
