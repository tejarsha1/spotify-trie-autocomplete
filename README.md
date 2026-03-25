# Spotify Autocomplete Search using Trie

## Overview
This project implements an autocomplete search system using a Trie (prefix tree) data structure on a real-world Spotify dataset containing over 100,000 songs.

The goal is to demonstrate how tree-based algorithms can efficiently perform prefix search on large and noisy real-world datasets.

The system allows users to type the beginning of a song name and receive the top matching results instantly.

Example:
Input:
lov

Output:
1. lovely (with Khalid) - Billie Eilish, Khalid | Popularity: 89 | Genre: pop
2. LOVE DIVE - IVE | Popularity: 85 | Genre: k-pop
3. Lover - Taylor Swift | Popularity: 85 | Genre: pop
4. Love Yourself - Justin Bieber | Popularity: 84 | Genre: pop
5. Love The Way You Lie - Eminem, Rihanna | Popularity: 83 | Genre: hip-hop


## Dataset
The project uses a Spotify Tracks dataset containing more than 100,000 songs with multiple metadata fields, including:

- track name
- artist name
- album name
- popularity score
- genre
- tempo
- energy
- danceability

Since the dataset is collected from real-world music records, it contains noisy data such as:
- duplicate song names across artists
- inconsistent formatting
- punctuation differences
- missing values

This satisfies the assignment requirement of using a real-world dataset with more than 10,000 items.


## Algorithm Used
The main algorithm used is a Trie (Prefix Tree).

A Trie stores text character by character. Each node represents a character of a song title.

This allows efficient prefix-based search.

Example:
When the user types:
lov

The Trie directly navigates through nodes:
l → o → v

and returns matching songs without scanning the entire dataset.

Time Complexity:
- Insert operation: O(n) per title
- Prefix search: O(k), where k is the length of the search prefix

Compared to linear search O(N), Trie search is faster for large datasets.


## Preprocessing
Before inserting song titles into the Trie, the dataset is preprocessed to handle real-world noisy data.

Steps:
- convert text to lowercase
- remove special characters
- handle missing values
- clean formatting inconsistencies
- standardize artist names

This ensures the algorithm works effectively on imperfect real-world data.


## Features
- Fast prefix-based autocomplete search
- Uses Trie data structure
- Works on dataset with more than 100,000 songs
- Returns top 5 matching songs
- Results ranked by popularity
- Displays metadata:
  - artist name
  - popularity score
  - genre


## Project Structure
project-folder

main.py → loads dataset and runs search  
trie.py → Trie data structure implementation  
preprocess.py → text cleaning function  
dataset.csv → Spotify dataset  
proposal.pdf → project proposal  
requirements.txt → dependencies  
README.md → project documentation  


## How to Run

Install dependency:

pip install pandas

Run program:

python main.py


## Example Usage

Enter prefix:
lov

Output:
1. lovely (with Khalid) - Billie Eilish, Khalid | Popularity: 89 | Genre: pop
2. LOVE DIVE - IVE | Popularity: 85 | Genre: k-pop
3. Lover - Taylor Swift | Popularity: 85 | Genre: pop
4. Love Yourself - Justin Bieber | Popularity: 84 | Genre: pop
5. Love The Way You Lie - Eminem, Rihanna | Popularity: 83 | Genre: hip-hop


## Key Learning Outcomes
- Implementation of tree-based data structure (Trie)
- Handling noisy real-world datasets
- Efficient prefix-based search
- Working with metadata fields
- Algorithm performance optimization


## Conclusion
This project demonstrates how Trie data structures can efficiently power autocomplete search systems similar to those used in search engines and music platforms.

The approach shows how algorithmic techniques can scale effectively when working with large real-world datasets.

## AI Usage Statement

AI tools were used only for guidance and clarification during development.

The core components of this project were manually implemented, including:
- Trie data structure implementation
- preprocessing logic for handling noisy real-world data
- prefix search algorithm
- data loading and metadata handling

AI assistance was used only for:
- understanding problem requirements
- improving code readability
- formatting documentation

No AI-generated code was directly used for the core algorithm or preprocessing logic.

All implementation logic, code structure, and algorithm design decisions were written and verified manually.