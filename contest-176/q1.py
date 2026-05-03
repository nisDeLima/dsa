#Q1. Weighted Word Mapping
#Solved
#Easy
#3 pt.
#You are given an array of strings words, where each string represents a word containing lowercase English letters.
#
#You are also given an integer array weights of length 26, where weights[i] represents the weight of the ith lowercase English letter.
#
#The weight of a word is defined as the sum of the weights of its characters.
#
#For each word, take its weight modulo 26 and map the result to a lowercase English letter using reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a').
#
#Return a string formed by concatenating the mapped characters for all words in order.

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return ''.join(
            chr(ord('z') - sum(weights[ord(c) - ord('a')] for c in word) % 26)
            for word in words
        )
