# README File

## Proces odtworzenia danych:

1. Pierwotne dane znajdują się w folderze original_data w pliku o nazwie 11_SLA.csv. Z racji tego, że plik jest formacie csv to jest gotowy do wczytania.

2. Wczytanie i czyszczenie danych odbywa się w pliku o nazwie explory_data.ipynb dane zostały zaimportowane przy użyciu biblioteki pandas.

3. Po wstępnym przeanalizowaniu zbioru danych stwierdziłem, że braki w danych występują tylko w kolumnie "Wiek kupujacego" na 453 wiersze bylo ich aż 51, lecz nie było sensu usuwania tych wierszy ponieważ utracilibyśmy wtedy znaczną część potrzebnych informacji na temat innych kategorii. W tym celu jawie zamianiłem puste komórki wartośćią np.nan

4. Proces czyszczenia tego zbioru był bardzo trywialny z tego względu po zastąpieniu tych pustych komórek dane mogłem zapisać w pliku w celu dalszej analizy. Ścieżka do pliku wygląda następująco /analisys_data/analisys_data.csv

5. Dalszą analize przeprowadziłem w pliku data_appendix.ipynb znajdującego się w katalogu command_files
Dla każdej ze zmiennych wyrysowałem histogram lub wykres słupkowy.

Wnoski z tych wykresów znajdują się w katalogu documents w pliku o nazwie data_appendix.md

