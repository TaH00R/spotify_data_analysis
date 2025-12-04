import pandas as pd

def total_tracks(df):
    return len(df)


def unique_artists(df):
    return df['artistname'].nunique()


def top_artists(df, n=10):
    return df['artistname'].value_counts().head(n)


def artist_frequency_table(df):
    return df['artistname'].value_counts()


def artist_diversity_score(df):
    total = total_tracks(df)
    unique = unique_artists(df)
    return unique / total


def playlist_overview(df):
    return {
        "total_tracks": total_tracks(df),
        "unique_artists": unique_artists(df),
        "diversity_score": artist_diversity_score(df),
        "top_10_artists": top_artists(df, 10)
    }
