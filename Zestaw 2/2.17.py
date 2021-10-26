line = "dbd\nzo\nib\tasr\nlaz\taete\nasdttfgdf\tsdefgf\nkdhfs"
print(line.split())
print("Posortowane alfabetycznie:", sorted(line.split()))
print("Posortowane po dlugosci:", sorted(line.split(), key=len))