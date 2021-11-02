while True:
    liczba = input("Podaj liczbe rzeczywista: ")
    if liczba.lower()== "stop":
        break
    try:
        liczba = float(liczba)
        print('%.2f %.2f' % (liczba, liczba ** 3))
    except:
        print("Blad, podaj liczbe rzeczywista")
