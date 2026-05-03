class TrieNode:
    __slots__ = ("children", "count")
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> int:
        curr = self.root
        n = len(word)
        for i in range(n):
            key = (word[i], word[n - i - 1])
            if key not in curr.children:
                curr.children[key] = TrieNode()
            curr = curr.children[key]
            curr.count += 1
        return curr.count

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        ans = 0
        for word in reversed(words):
            ans += trie.insert(word) - 1
        return ans
