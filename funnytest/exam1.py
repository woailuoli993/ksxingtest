# _*_ coding: utf-8 _*_
"""
Description
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
For example,
Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""
# 思路就是 余数重合则出现循环

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        while numerator < denominator:
            pass
        return


if __name__ == "__main__":
    sol = Solution()
    assert sol.fractionToDecimal(1, 2) == "0.5"
    assert sol.fractionToDecimal(2, 1) == "2"
    assert sol.fractionToDecimal(2, 3) == "0.(6)"
    assert sol.fractionToDecimal(6, 7) == "0.(857142)"
    assert sol.fractionToDecimal(1, 6) == "0.1(6)"
    assert sol.fractionToDecimal(-50, 8) == "-6.25"
    print("correct")

'比上面题更难的是退押金.................'