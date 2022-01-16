<h1>Projekt: algorytmy szyfrujące (Projekt Cryptographer)</h1>
<h2>Autor: Michał Dutka</h2>

<h3>Uruchamianie:</h3>
<ol>
  <li>Przygotować sobie plik z rozszerzeniem .txt z tekstem do zaszyfrowania/odszyfrowania</li>
  <li>Uruchomić plik main.py</li>
  <li>Wpisać nazwę pliku wejściowego (pliku z punktu 1.)</li>
  <li>Wpisać nazwę pliku wyjściowego (jeśli nie mamy to się automatycznie stworzy, też z rozszerzeniem .txt)</li>
  <li>W konsoli pojawi się menu, wystarczy wpisać odpowiednia cyfrę i program wykona dane zadanie.</li>
</ol>

<h3>WAŻNE</h3>
Program nie obsługuje polskich znaków (działa na alfabecie angielskim który składa się z 26 znaków).<br>
Nie trzeba zamykać programu żeby zobaczyć plik wyjściowy z zaszyfrowanym/odszyfrowanym tekstem.<br>
Program jest napisany tak, że można do niego dodać dowolny inny algorytm. Musi mieć on jednak 2 metody, jedną o nazwie crypt() do szyfrowania linii tekstu, a drugą o nazwie decrypt() do deszyfrowania linii tekstu.

<h3>Struktura:</h3>
4 pliki<br>

 -<b>main.py</b> - główny plik, zawiera w sobie zmienną globalną N która odpowiada za liczbę w przesunięciu ROT. 
Jest ona ustawiona na wartośc 13 (dzięki czemu mamy szyfrowanie/deszyfrowanie za pomocą ROT13), ale po zmianie na inną wartość np. 9
mamy możliwość szyfrowania/deszyfrowania z użyciem ROT9. Następnie jest krótkie sprawdzenie z użyciem wyjątków czy plik wejściowy istnieje.
Potem już jest tylko pętla dla interfejsu tekstowego która dla odpowiednich if'ów uruchamia wybrane funkcje.

 -<b>cryptographer.py</b> - klasa która ma jedną metodę (encrypt_or_decrypt()) której zadaniem jest obsługa plików. W argumentach podajemy nazwę pliku wejściowego, nazwę pliku wyjściowego, algorytm jakiego chcemy użyć oraz wartość True lub False w zależności czy chcemy szyfrować czy deszyfrować (domyślnie wartość jest ustawiona na True czyli szyfrowanie). Metoda ta pobiera linijkę po linijce z pliku tekstowego i wysyła ją do metody crypt lub decrypt która musi być w algorytmie. Te dwie metody zwracają przetłumaczoną linijkę która następnie jest zapisywana do pliku wyjściowego.

Następnie mamy już klasy z odpowiednimi algorytmami. Te klasy mają podobną budowę, to znaczy obie mają i muszą mieć metody crypt() i decrypt() (muszą je mieć bo do tych metod odwołuje się metoda w klasie cryptographer.py). Metoda crypt() służy do szyfrowania tekstu, a metoda decrypt() służy do odszyfrowania tekstu.

 -<b>rot_n.py</b> - klasa która realizuje algorytm ROT_N bazujący na algorytmie ROT13 (https://pl.wikipedia.org/wiki/ROT13), ale pozwalający na dowolną liczbę przesunięcia. Za tą liczbę przesunięcia odpowiada zmienna globalna N w 5 linii w pliku main.py.

 -<b>polybius.py</b> - klasa która realizuje algorytm szyfrowania za pomocą szachownicy Polibiusza (https://pl.wikipedia.org/wiki/Szachownica_Polibiusza). W mojej wersji rozdzieliłem litery I i J na dwa osobne pola oraz dodałem pole na spację, przez co moja "szachownica" nie ma rozmiaru 5x5 jak w oryginale tylko 5x5 + 1x2. Ta mała modyfikacja nie zmieniła zasady działania.
