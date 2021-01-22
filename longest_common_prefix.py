

def longestCommonPrefix(strs):
    highestPrefix = None
    highestCounter = 0
    for idx, str in enumerate(strs):
        prefix = str[0:2]
        counter = 1
        if prefix == highestPrefix:
            continue
        for id, word in enumerate(strs):
            if idx == id:
                continue
            if word[0:2] == str[0:2]:
                counter += 1
            if highestCounter > len(strs) / 2:
                return highestPrefix
        print('prefix', prefix)
        print('highestPrefix', highestPrefix)
        print('highestCounter', highestCounter)
        if highestCounter < counter:
            highestPrefix = prefix
            highestCounter = counter
        elif highestCounter == counter:
            highestPrefix = ""
            highestCounter = counter

    return highestPrefix or ""


# print('answer', longestCommonPrefix(["flower","flow","flight", "cat", "car"]))
# print('answer', longestCommonPrefix(["a"]))
# print('answer', longestCommonPrefix(["dog","racecar","car"]))
print('answer', longestCommonPrefix(["","b"]))

