a = [7,12,9,14,15,18,12]
b = [9,14,8,3,15,17,15]
big = [ ]
i = 0
while i < len(a):
    big.append(max(a[i],b[i]))
    i = i + 1
print(big)
