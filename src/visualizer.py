import matplotlib.pyplot as plt
import os

def ensure_output_folder():
    charts_path = os.path.join("outputs", "charts")
    os.makedirs(charts_path, exist_ok=True)
    return charts_path


def plot_top_artists(df, n=10):
    charts_path = ensure_output_folder()
    top_artists = df['artistname'].value_counts().head(n)

    plt.figure(figsize=(10, 6))
    plt.bar(top_artists.index, top_artists.values)
    plt.title(f"Top {n} Artists")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Number of Occurrences")
    plt.tight_layout()

    save_path = os.path.join(charts_path, f"top_{n}_artists.png")
    plt.savefig(save_path)
    plt.close()
    print(f"Saved bar chart: {save_path}")


def plot_artist_pie_chart(df, n=10):
    charts_path = ensure_output_folder()
    top_artists = df['artistname'].value_counts().head(n)

    plt.figure(figsize=(16, 16))
    plt.pie(
        top_artists.values,
        labels=top_artists.index,
        autopct='%1.2f%%',
        startangle=140
    )
    plt.title(f"Artist Share (Top {n})")
    plt.tight_layout()

    save_path = os.path.join(charts_path, f"artist_pie_top_{n}.png")
    plt.savefig(save_path)
    plt.close()
    print(f"Saved pie chart: {save_path}")


def plot_artist_distribution(df, max_artists=50):
    charts_path = ensure_output_folder()
    freq = df['artistname'].value_counts().head(max_artists)

    plt.figure(figsize=(14, 6))
    plt.plot(freq.index, freq.values, marker='o')
    plt.xticks(rotation=45, ha='right')
    plt.title("Artist Frequency Distribution")
    plt.ylabel("Occurrences")
    plt.tight_layout()

    save_path = os.path.join(charts_path, f"artist_distribution_top_{max_artists}.png")
    plt.savefig(save_path)
    plt.close()
    print(f"Saved distribution chart: {save_path}")
