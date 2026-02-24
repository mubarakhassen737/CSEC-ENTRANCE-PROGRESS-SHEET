n = int(input())
events = list(map(int, input().split()))

police = 0
untreated = 0

for e in events:
    if e > 0:
        police += e
    else:
        if police > 0:
            police -= 1
        else:
            untreated += 1

print(untreated)