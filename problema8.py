#de introdus din rand nou
nume = []
final = []
i = 0

with open('input.txt', 'r') as f:
    for x in f.readlines():
        nume.append(x)
for b in nume:
    if "\n" in b:
        z = str(b.replace("\n", ''))
        final.append(z)
gg = len(nume) - 1
final.append(nume[gg])

for fb in final:
    if fb.islower():
        l = ord(fb[(0)])
        L = l - 32
        fb = fb[:0] + chr(L) + fb[1:]
        final[i] = fb
    i+=1
print(final)
with open("output.txt", 'w') as f2:
    final.sort()
    for x in final:
        f2.write(f'{x} \n')