import pandas as pd
def data_read_and_info(file_location):
    """
    Wczytuje dane z pliku JSON i wyświetla podstawowe informacje na ich temat.

    Parameters:
    file_location (str): Ścieżka do pliku JSON, który ma zostać wczytany.

    Returns:
    : Funkcja nie zwraca żadnej wartości, jedynie drukuje informacje o danych.
    """
    df = pd.read_json(file_location)
    print(df.info())
    print(df.head())
    return pd.read_json(file_location)

print(data_read_and_info("raw_data_cocktail.json").head(10))