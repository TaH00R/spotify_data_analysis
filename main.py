from src.data_loader import load_csv, view_basic_info
from src.data_cleaner import clean_data
from src.analyzer import playlist_overview
from src.visualizer import (
    plot_top_artists,
    plot_artist_pie_chart,
    plot_artist_distribution
)
from src.summary import generate_text_summary, save_summary

def main():
    print("\nLoading dataset...")
    df = load_csv()
    view_basic_info(df)

    print("\nCleaning dataset...")
    df = clean_data(df)

    print("\nAnalyzing dataset...")
    stats = playlist_overview(df)
    print(stats)

    print("\nGenerating visualizations...")
    plot_top_artists(df, n=10)
    plot_artist_pie_chart(df, n=10)
    plot_artist_distribution(df, max_artists=50)

    print("\nCreating summary report...")
    text = generate_text_summary(stats)
    save_summary(text)

    print("\n===== ANALYSIS COMPLETE! =====")

if __name__ == "__main__":
    main()
