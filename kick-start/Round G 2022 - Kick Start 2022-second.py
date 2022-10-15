import math
for x in range(int(input())):
    rs, rh = map(int, input().split())
    red = []
    for _ in range(int(input())):
        red.append(list(map(int, input().split())))
    yellow = []
    for _ in range(int(input())):
        yellow.append(list(map(int, input().split())))
    red_score = 0
    yellow_score = 0
    for i in red:
        if (((i[0]**2 + i[1]**2)**0.5) - rs) <= rh:
            red_score += 1
            yellow_score -= 1
    for i in yellow:
        if (((i[0]**2 + i[1]**2)**0.5) - rs) <= rh:
            yellow_score += 1
            red_score -= 1
    if yellow_score < 0: yellow_score = 0
    if red_score < 0: red_score = 0
    print(f"Case #{x+1}: {red_score} {yellow_score}")
"""
1
1 5
2
1 0
-3 0
1
0 2

1
10 50
2
-40 -31
-35 70
3
59 0
-10 0
30 40
"""
