"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxLength = max(len(a), len(b)) * -1
        counter = -1
        carry = 0
        binary = ""
        a = a.rjust((maxLength * -1), '0')
        b = b.rjust((maxLength * -1), '0')
        while (counter > maxLength - 1):
            added = int(a[counter]) +  int(b[counter]) + carry
            value = str(max(int(a[counter]), int(b[counter]), carry))
            if added == 2:
                value = '0'
                carry = 1
            elif added == 3:
                value = '1'
                carry = 1
            else:
                carry = 0
            binary = value + binary
            counter -= 1
        if carry:
            binary = '1' + binary
        return binary
solution = Solution()
print(solution.addBinary("101", "1101"))