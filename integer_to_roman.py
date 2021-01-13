import sys

romanValues = [
    [1, 'I', True],
    [5, 'V', False],
    [10, 'X', True],
    [50, 'L', False],
    [100, 'C', True],
    [500, 'D', False],
    [1000, 'M', True]
]

def get_repeatable_roman_value(haystack, needle, addition = 0):
    tmp_arr = []
    counter = 0
    tmp_total = 0
    while counter < 3:
        # limit of 3 characters only
        tmp_arr.append(haystack[1])
        tmp_total += haystack[0]
        if addition + tmp_total ==  needle:
            return tmp_arr, tmp_total
        counter +=1
    return None, None

def get_roman_value():
    dataValue = None

    return dataValue

def integerToRoman(num):
    total = 0
    pow = 1
    total_arr = []
    tmpNum = num
    for idx, currentData in enumerate(romanValues, 0):
        if tmpNum == 0:
            break
        currentNumber = tmpNum % (10 ** pow)
        if currentNumber == 0:
            pow = pow + 1
            continue
        nextData = romanValues[idx] if idx == len(romanValues) - 1 else romanValues[idx + 1]
        if currentData[0] == currentNumber:
            total = total + currentData[0]
            total_arr.insert(0, currentData[1])
            tmpNum = tmpNum - currentNumber
            pow = pow + 1
        elif nextData[0] == currentNumber:
            total = total + nextData[0]
            total_arr.insert(0, nextData[1])
            tmpNum = tmpNum - currentNumber
            pow = pow + 1
        elif (currentNumber >= currentData[0] and 
            currentNumber < nextData[0]) or  pow == 4:
            if currentData[2] and (
                    (currentNumber < nextData[0] - (10 ** (pow - 1)))
                    or
                    pow == 4
                ):
                # repeat currentData if currentData is repeatable
                tmp_arr, tmp_total = get_repeatable_roman_value(currentData, currentNumber)
                if tmp_arr:
                    total = total + tmp_total
                    total_arr.insert(0, "".join(tmp_arr))
                    tmpNum = tmpNum - currentNumber
                    pow = pow + 1
                    continue
            elif currentNumber > currentData[0] and currentNumber < nextData[0]:
                # if not repeatable search lower numbers that are repeatable
                data_tmp = reversed(romanValues[:(idx + 1)])
                for data in data_tmp:
                    if not data[2]:
                        continue
                    
                    # do subtraction
                    tmp_arr = []
                    tmp_total = 0
                    if nextData[0] - data[0] == currentNumber:
                        tmp_total = nextData[0] - data[0]
                        tmp_arr = [data[1] + nextData[1]]

                    # do addition
                    if not tmp_total:
                        tmp_arr, tmp_total = get_repeatable_roman_value(data, currentNumber, currentData[0])
                        if tmp_arr:
                            tmp_arr.insert(0, currentData[1])
                            tmp_total = tmp_total + currentData[0]
                    if tmp_total:
                        total = total + tmp_total
                        total_arr.insert(0, "".join(tmp_arr))
                        tmpNum = tmpNum - currentNumber
                        pow = pow + 1
                        break
                    else:
                        pass
            else:
                pass
        else:
            pass
    return "".join(total_arr)

print('return', integerToRoman(int(sys.argv[1])))

