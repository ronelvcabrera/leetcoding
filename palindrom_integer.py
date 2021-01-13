# from reverse_integer import reverse 

def isPalindrome_old(x):
    reversed = reverse_int(x)
    return x == reversed

def reverse_int(num):
    reversed = 0
    number = num
    while (number != 0):
        last_digit = number % 10
        reversed = (reversed * 10) + last_digit
        number = int(number / 10)
    if reversed > (2 ** 31) - 1 or reversed < -2 ** 31:
        return 0
    return reversed

def isPalindrome(x):
    if x % 10 == 0 or x < 0:
        return False
    revertedNumber = 0
    while (x > revertedNumber):
        last_digit =  x % 10
        revertedNumber = revertedNumber * 10 + last_digit
        x = int(x / 10)
    return int(revertedNumber/10) == x or revertedNumber == x

    
    

print(isPalindrome(12321))