import os

def ensure_report_folder():
    reports_path = os.path.join("outputs", "reports")
    os.makedirs(reports_path, exist_ok=True)
    return reports_path


def generate_text_summary(stats):
    summary = []
    summary.append("===== PLAYLIST ANALYSIS SUMMARY =====\n")
    summary.append(f"Total Tracks: {stats['total_tracks']}")
    summary.append(f"Unique Artists: {stats['unique_artists']}")
    summary.append(f"Diversity Score: {stats['diversity_score']:.4f}\n")

    summary.append("Top 10 Artists:\n")
    for artist, count in stats["top_10_artists"].items():
        summary.append(f"- {artist}: {count}")

    return "\n".join(summary)


def save_summary(text):
    reports_path = ensure_report_folder()
    save_path = os.path.join(reports_path, "summary.txt")

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Saved summary report: {save_path}")
