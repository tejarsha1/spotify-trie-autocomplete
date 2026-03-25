class TrieNode:
    def __init__(self):
        self.children = {}
        self.songs = []
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, metadata):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]
            node.songs.append(metadata)

        node.is_end = True

    def search_prefix(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        sorted_songs = sorted(
            node.songs,
            key=lambda x: x["popularity"],
            reverse=True
        )

        return sorted_songs[:5]