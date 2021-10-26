line = "dbd\nzo\nib\tasr\nlaz\taete"
a = line.split()
i = 0
longest = 0
word = ""
while i < len(a):
    if (len(a[i]) >= longest):
        longest = len(a[i])
        word = a[i]
    i = i+1
print("Slowo:", word, "Dlugosc:", longest)
