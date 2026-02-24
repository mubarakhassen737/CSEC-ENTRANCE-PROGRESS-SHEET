a, b = map(int, input().split())

m = max(a, b)
favorable = 6 - m + 1

from math import gcd
g = gcd(favorable, 6)

print("%d/%d" % (favorable//g, 6//g))