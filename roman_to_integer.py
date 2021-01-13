
roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def romanToInt(s):
    val = 0
    previous = 0
    for char in s:
        current = roman.get(char)
        print('current', char, current)
        if current > previous:
            val -= previous
            print('current', current)
            print('previous', previous)
            print('sub', current - previous)
            current = current - previous
            print('sub', current)
        val += current
        print('val', val)
        previous = roman.get(char)
        print('----')
    print('value is', val)
    return val

def romanToIntLoop(s):
    val = 0
    previous = None
    arr = list(s)
    for i in range(len(arr), 0, -1):
        idx = i - 1
        char = arr[idx]
        current = roman.get(char)
        if previous:
            if current < previous:
                current *= -1
        val += current
        previous = roman.get(char)
    return val

s = "MCMXCIV"
# romanToInt(s)
print(romanToIntLoop(s))