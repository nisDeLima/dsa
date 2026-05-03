class PrefixNode:
    def __init__(self):
        self.children = {}
        self.sentences = set()

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def add_sentence(self, sentence, id):
        curr = self.root
        for char in sentence:
            if char not in curr.children:
                curr.children[char] = PrefixNode()
            curr = curr.children[char]
            curr.sentences.add(id)

    def get_sentences(self, inpt, check=None):
        curr = check if check is not None else self.root
        for char in inpt:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return set(), None
        return curr.sentences, curr

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.current_input = ""
        self.tree = PrefixTree()
        self.sentences = sentences
        self.times = times
        self.check = None
        self.sentence_to_id = {}
        self.sorted_order = []

        for idx, sentence in enumerate(sentences):
            self.tree.add_sentence(sentence, idx)
            self.sentence_to_id[sentence] = idx

        self.sorted_order = sorted(
            range(len(self.sentences)),
            key=lambda i: (-self.times[i], self.sentences[i])
        )

    def input(self, c: str) -> List[str]:
        if c == "#":
            if self.current_input in self.sentence_to_id:
                self.times[self.sentence_to_id[self.current_input]] += 1
            else:
                idx = len(self.sentences)
                self.sentences.append(self.current_input)
                self.times.append(1)
                self.sentence_to_id[self.current_input] = idx
                self.tree.add_sentence(self.current_input, idx)
            self.sorted_order = sorted(
                range(len(self.sentences)),
                key=lambda i: (-self.times[i], self.sentences[i])
            )
            self.current_input = ""
            self.check = None
            return []
        self.current_input += c
        if self.check is not None:
            sentences, self.check = self.tree.get_sentences(c, self.check)
        else:
            sentences, self.check = self.tree.get_sentences(self.current_input)

        res = []
        for idx in self.sorted_order:
            if idx in sentences:
                res.append(self.sentences[idx])
                if len(res) >= 3:
                    return res
        return res
