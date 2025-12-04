import pandas as pd
import os

def get_file_path():
    return os.path.join("datasets", "playlists_dataset.csv")


def load_csv():
    file_path = get_file_path()

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found at: {file_path}")

    df = pd.read_csv(file_path, on_bad_lines='skip')
    return df


def view_basic_info(df):
    print("\n===== DATASET OVERVIEW =====\n")
    print("➡ Total Rows:", df.shape[0])
    print("➡ Total Columns:", df.shape[1])
    print("\n➡ Column Names:", list(df.columns))
    print("\n➡ First 5 Rows:\n")
    print(df.head())
