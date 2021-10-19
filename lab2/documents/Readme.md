Plik weather1.txt znajduje się w folderze o nazwie ../original_data/ zawiera on zbiór pomiarów z stacji pogodowej MX17004 w Meksyku dane zawierają pomiary od 1955 do 2011 roku.
Naszym zadaniem było wyodrębnienie danych z pierwszych 5 miesięcy roku 2010.

1. w pierwszym kroku odfiltrowałem interesujące nas dane z pierwszych 5 miesięcy roku 2010.
2. Następnie podzieliłem dane wg następującego klucza:
    - Nazwa stacji
    - rok 
    - miesiąc 
    - element, typ pomiaru TMAX, TMIN, itp.
    - Temperatury z poszczególnych dni miesiaca
3. pomiary zawierające jakieś artefakty tj, wartości S, S-9999, -9999 zastąpiłem wartością 'inf'
4. Następnie wyodrębniłem tylko te wartości, której kolumny nie zawierały infa
5. W kolejnym kroku połączyłem kolumny year, month, day w jedną kolumne o nazwie data zawierającą date w następującej postaci: year-month-day
6. Ostatnim krokiem było rozdzielenie kolumny o nazwie element na 3 kolumny:
    - TMAX
    - TMIN
    - PRCP
7. W ostatnim kroku zapisałem przefiltrowany DataFrame do pliku o nazwie final_data.txt
