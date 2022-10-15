for x in range(int(input())):
    need= 0
    no_part, no_days, john_id = map(int, input().split())
    scoreboard = []
    for _ in range(no_part):
        scoreboard.append(list(map(int, input().split())))
    scoreboard = list(zip(*scoreboard))
    for row in scoreboard:
        if row[john_id - 1] != max(row):
            need += max(row) - row[john_id - 1]
    print(f"Case #{x+1}: {need}")
