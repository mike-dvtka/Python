line = "dbd\nzo\nib\tasr\nlaz\taete"
a = line.split()
i = 0
word1 = ""
word2 = ""
while i < len(a):
    word1 = word1+a[i][0]
    word2 = word2+a[i][-1]
    i = i+1
print(word1, word2)