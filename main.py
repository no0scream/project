from sys import stdin

lines = []
for line in stdin:
    lines.append(line.strip('\n'))
summa=0
for s in lines:
    s = s.split()
    for a in s:
        summa = summa + int(a)

print(summa)
print('3')
print(3)