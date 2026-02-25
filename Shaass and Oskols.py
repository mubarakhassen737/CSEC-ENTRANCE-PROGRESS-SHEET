n = int(input())
a = list(map(int, input().split()))

m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    x = x - 1  # convert to zero-based index

    left = y - 1
    right = a[x] - y

    if x > 0:
        a[x - 1] = a[x - 1] + left

    if x < n - 1:
        a[x + 1] = a[x + 1] + right

    a[x] = 0  # the wire that was shot becomes empty

for i in a:
    print(i)