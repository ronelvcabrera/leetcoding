def recurse_def(num, data, printme=None):
    print('-----')
    if printme:
        print('printme', printme)
    if data.get(num):
        print('there is this number', num, data.get(num))
        return data[num]
    if num > 5:
        return data
    else:
        num += 1
        data[num] = num
        print('num', num)
        recurse_def(num, data)
        print('checking data', data)
        print('checking num', num)
        recurse_def(num + 1, data, 'next')
        return data


def parentDef(data):
    data['b'] = 2

# data = recurse_def(0, {})
# print('final data', data)

data = { 'a': 1 }
parentDef(data)
print('data', data)

