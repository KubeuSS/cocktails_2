import pandas as pd
def data_reading(file_location):
    """
    Wczytuje dane z pliku JSON i zwraca z nich dataset.

    Parameters:
    file_location (str): Ścieżka do pliku JSON, który ma zostać wczytany.

    Returns:
    : Funkcja zwraca zbiór danych jako pandas dataframe
    """
    df = pd.read_json(file_location)
    return df
