
def reverse(x):
    reverseNum = 0
    multiplier = -1 if x < 0 else 1
    number = abs(x)
    while (number > 0):
        lastDigit = number % 10
        reverseNum = (reverseNum * 10) + lastDigit
        number = int(number / 10)
    result = reverseNum * multiplier
    if (result > (2 ** 31) -1) or (result < -2 ** 31):
        result = 0
    return result
# 1234 - 4 - 0 + 4
# 123 - 3 - 40 + 3
# 12 - 2 - 430 + 2
# 1 - 1 - 432 + 1
# 0 break
# print(reverse(1534236469))