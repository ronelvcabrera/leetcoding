import sys

romanValues = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

def integerToRoman(num):
    if num in romanValues:
        return romanValues[num]
    keys = list(romanValues.keys())
    idx = 0
    roman = ''
    while num != 0:
        value = keys[idx]
        if num - value >= 0:
            roman += romanValues[keys[idx]]
            num = num - value
        else:
            idx += 1
    return roman

print('return', integerToRoman(int(sys.argv[1])))

