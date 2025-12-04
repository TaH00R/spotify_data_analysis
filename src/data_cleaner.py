import pandas as pd


def standardize_column_names(df):
    df.columns = (
        df.columns
        .str.strip()  # remove spaces
        .str.replace('"', '')  # remove quotes
        .str.lower()  # lowercase
    )
    return df


def remove_duplicates(df):
    df = df.drop_duplicates()
    return df


def handle_missing_values(df):
    df = df.dropna(subset=['artistname', 'trackname'])
    return df


def clean_data(df):
    df = standardize_column_names(df)
    df = remove_duplicates(df)
    df = handle_missing_values(df)

    return df
