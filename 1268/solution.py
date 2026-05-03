class TrieNode:
    def __init__(self):
        self.children = {}
        self.words_ids = []


class Trie:
    def __init__(self, products):
        self.root = TrieNode()
        products.sort()
        self.products = products
        for idx, product in enumerate(products):
            self.insert(product, idx)
    
    def insert(self, word, idx):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.words_ids.append(idx)

    def find_results(self, word):
        res = []
        curr = self.root
        matched = True

        for char in word:
            if matched and char in curr.children:
                curr = curr.children[char]
                curr_res = [self.products[i] for i in curr.words_ids[:3]]
                res.append(curr_res)
            else:
                matched = False
                res.append([])

        return res


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie(products)
        return trie.find_results(searchWord)


