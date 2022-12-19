n = int(input())
cut = 0
p = 1

while p < n:
    cut += 1
    p *= 2
print(cut)
