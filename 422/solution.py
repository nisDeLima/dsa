class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for col in range(len(words)):
            col_word = []
            for word in words:
                if col < len(word):
                    col_word.append(word[col])
            if "".join(col_word) != words[col]:
                return False
        return True
