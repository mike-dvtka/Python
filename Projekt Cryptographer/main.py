from cryptographer import Cryptographer
from rot_n import RotN
from polybius import Polybius

N = 13

while True:
    fileInName = input("Podaj nazwę pliku do odczytu: ")
    try:
        test = open(str(fileInName) + ".txt", "r")
    except FileNotFoundError:
        print("Niepoprawna nazwa pliku lub plik nie istnieje")
    else:
        break
test.close()

fileOutName = input("Podaj nazwę pliku do zapisu (jeśli plik nie istnieje to zostanie utworzony): ")

cg = Cryptographer()

print("\n1) Szyfruj ROT"+str(N))
print("2) Deszyfruj ROT"+str(N))
print("3) Szyfruj Polibiusz")
print("4) Deszyfruj Polibiusz")
print("5) Zakończ i wyjdź")

while True:
    answer = input("\nWybierz zadanie: ")

    if answer.startswith("1"):
        cg.encrypt_or_decrypt(fileInName, fileOutName, RotN(N))
        print("Wykonano szyfrowanie ROT"+str(N))

    elif answer.startswith("2"):
        cg.encrypt_or_decrypt(fileInName, fileOutName, RotN(N), False)
        print("Wykonano deszyfrowanie ROT"+str(N))

    elif answer.startswith("3"):
        cg.encrypt_or_decrypt(fileInName, fileOutName, Polybius())
        print("Wykonano szyfrowanie szachownicą Polibiusza")

    elif answer.startswith("4"):
        cg.encrypt_or_decrypt(fileInName, fileOutName, Polybius(), False)
        print("Wykonano deszyfrowanie szachownicą Polibiusza")

    elif answer.startswith("5"):
        print("Kończenie pracy...")
        exit()

    else:
        print("Wpisz odpowiednią cyfrę")
