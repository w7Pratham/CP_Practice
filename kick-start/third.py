for x in range(int(input())):
    input()
    res = 0
    ls = list(map(int, input().split()))
    for i in range(len(ls)):
        for j in range(i+1,len(ls)+1):
            cac = ls[i:j]
            s = sum(ls[i:j])
            if s < 0:
                break
            else:
                res += s
    print(f"Case #{x+1}: {res}")
