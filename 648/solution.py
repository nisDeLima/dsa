class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

    def find_shortest(self, word):
        curr = self.root
        for idx, c in enumerate(word):
            if c in curr.children:
                curr = curr.children[c]
                if curr.is_word:
                    return idx
            else:
                return -1
        return -1

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        s_array = sentence.split(" ")

        for prefix in dictionary:
            trie.insert(prefix)

        for idx, word in enumerate(s_array):
            shortest = trie.find_shortest(word)
            if shortest != -1:
                s_array[idx] = word[0:shortest + 1]

        return " ".join(s_array)
