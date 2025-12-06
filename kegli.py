n, m = map(int, input().split())
keg = [0] * n

for i in range(m):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        keg[i] = 1

ans = sum(keg)
print(ans)
