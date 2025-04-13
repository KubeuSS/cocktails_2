import pandas as pd
def drop_columns(dataset, columns_to_drop):
    dataset.drop(columns=columns_to_drop, inplace=True)