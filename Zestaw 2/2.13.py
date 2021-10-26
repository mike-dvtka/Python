line = "dbd\nzo\nib\tasr\nlaz\taete"
a = line.split()
print(len(a))
i = 0
suma = 0
while i < len(a):
    suma = suma + len(a[i])
    i = i+1
print(suma)