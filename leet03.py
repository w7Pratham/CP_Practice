def lengthoflongestsubstring(str1):
    charSet = set()
    l = 0
    res = 0
    for r in range(len(str1)):
        while str1[r] in charSet:
            charSet.remove(str1[l])
            l += 1
        charSet.add(str1[r])
        res = max(res, r-l+1)
    return res

print(lengthoflongestsubstring("abcabcbb"))