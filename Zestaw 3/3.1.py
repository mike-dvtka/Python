x = 2; y = 3;   
if (x > y):     
    result = x; 
else:
    result = y; 

#Kod działa ale nie jest poprawny składniowo. Na końcu linii nie stawiamy średników, klamerek itd.
#Przypisanie kilku wartości jednej linii powinno wyglądać inaczej. Nawiasy w warunku mogą być ale nie muszą.
#Przykładowa wersja poprawnego kodu:

x, y = 2, 3
if x > y:     
    result = x
else:
    result = y

-------------------------------------------------------------------------------------------------------------
for i in "qwerty": if ord(i) < 100: print (i)

#Kod nie działa, brakuje wcięć (każde wcięcie 4 spacje)
#Przykładowa wersja poprawnego kodu:

for i in "qwerty": 
    if ord(i) < 100: 
        print (i)

-------------------------------------------------------------------------------------------------------------
for i in "axby": print (ord(i) if ord(i) < 100 else i)

#Kod działa i jest poprawny składniowo, bo przy instrukcjach prostych można zrezygnować z wcięcia.
