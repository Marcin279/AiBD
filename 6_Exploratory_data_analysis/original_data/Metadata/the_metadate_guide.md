# Metadata guide

### Zbior danych znajduje się w folderze .../original_data a plik ma nazwę 11_SLA.csv 

### Plik posiada oceny odkurzaczy w jednej z sieci sklepów dla województwa śląskiego. Plik posiada następujące zmienne:

- Dni od zakupu - reprezentuje czas jaki upłynął od momentu zakupu danego odkurzacza w dniach, typ danych: [int]
- Marka - przechowuje informacje o marce danego odkurzacza, typ danych: [str]
- Wiek kupujacego podana w latach. Nie wszyscy użytkownicy podali informacje o wieku dlatego niektóre komórki są puste, typ danych: [int]
- Płeć kupującego M/K/bd, typ danych: [str]
- Ocena - zmienna ta zawiera informacje o ocenie danego produktu w skali od 0 do 5, typ danych: [int]