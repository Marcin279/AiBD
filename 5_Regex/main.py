import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(category, (int, str)):
        return None

    if isinstance(category, int):
        querry: str = ("SELECT film.title, language.name AS languge, category.name AS category FROM film " + 
               "INNER JOIN language ON film.language_id = language.language_id " + 
               "INNER JOIN film_category ON film.film_id = film_category.film_id " +
               "INNER JOIN category ON film_category.category_id = category.category_id " +
               "WHERE category.category_id = {c} " + 
               "ORDER BY film.title, languge").format(c=category)
        
        df = pd.read_sql(querry, con=connection)
        return df
    
    if isinstance(category, str):
        querry: str = ("SELECT film.title, language.name AS languge, category.name AS category FROM film " + 
               "INNER JOIN language ON film.language_id = language.language_id " + 
               "INNER JOIN film_category ON film.film_id = film_category.film_id " +
               "INNER JOIN category ON film_category.category_id = category.category_id " +
               "WHERE category.name LIKE '\{c}\' " + 
               "ORDER BY film.title, languge").format(c=category)
        
        df = pd.read_sql(querry, con=connection)
        return df


def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(category, (int, str)):
        return None

    if isinstance(category, int):
        querry: str = ("SELECT film.title, language.name AS languge, category.name AS category FROM film " + 
               "INNER JOIN language ON film.language_id = language.language_id " + 
               "INNER JOIN film_category ON film.film_id = film_category.film_id " +
               "INNER JOIN category ON film_category.category_id = category.category_id " +
               "WHERE category.category_id = {c} " + 
               "ORDER BY film.title, languge").format(c=category)
        
        df = pd.read_sql(querry, con=connection)
        return df
    
    if isinstance(category, str):
        querry: str = ("SELECT film.title, language.name AS languge, category.name AS category FROM film " + 
               "INNER JOIN language ON film.language_id = language.language_id " + 
               "INNER JOIN film_category ON film.film_id = film_category.film_id " +
               "INNER JOIN category ON film_category.category_id = category.category_id " +
               "WHERE category.name ILIKE '\{c}\' " + 
               "ORDER BY film.title, languge").format(c=category)
        
        df = pd.read_sql(querry, con=connection)
        return df

    
def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(title, str):
        return None
    
    else:
        querry: str = ("SELECT actor.first_name, actor.last_name FROM film " +   
                    "INNER JOIN film_actor ON film.film_id = film_actor.film_id " +   
                    "INNER JOIN actor ON film_actor.actor_id = actor.actor_id " +  
                    "WHERE film.title LIKE '\{t}\' "  
                    "ORDER BY actor.last_name, actor.first_name").format(t=title)

        df = pd.read_sql(querry, con=connection)
        return df

        

def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not isinstance(words, list):
        return None 

    else:
        regex_q = f"'( |^)("
        tmp = "|".join(words)
        regex_q += tmp
        regex_q += ")+( |$)'"

        querry: str = ("SELECT film.title " + 
                    "FROM film " + 
                    "WHERE film.title ~* {r_q} "
                    "ORDER BY film.title").format(r_q=regex_q)

        df = pd.read_sql(querry, con=connection)

        return df