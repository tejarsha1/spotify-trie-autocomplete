import pandas as pd
from trie import Trie
from preprocess import clean_text

# Create Trie
trie = Trie()

# Load dataset
df = pd.read_csv("dataset.csv")

print("Columns:", df.columns)

# Insert songs into Trie
for _, row in df.iterrows():
    track_name = row.get("track_name", "")
    cleaned_title = clean_text(track_name)

    if cleaned_title == "":
        continue

    artist = str(row.get("artists", "Unknown")).replace(";", ", ")

    metadata = {
        "track": track_name,
        "artist": artist,
        "popularity": row.get("popularity", 0),
        "genre": row.get("track_genre", "Unknown")
    }

    trie.insert(cleaned_title, metadata)

# Search loop
while True:
    query = input("\nEnter song prefix: ").strip()

    if query.lower() == "exit":
        print("Exiting program.")
        break

    cleaned_query = clean_text(query)

    if cleaned_query == "":
        print("Please enter a valid prefix.")
        continue

    results = trie.search_prefix(cleaned_query)

    print("\nSuggestions:")
    if not results:
        print("No matching songs found.")
    else:
        for i, song in enumerate(results, start=1):
            print(
                f'{i}. {song["track"]} - {song["artist"]} | '
                f'Popularity: {song["popularity"]} | Genre: {song["genre"]}'
            )