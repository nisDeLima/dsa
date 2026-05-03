from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)  # O(1) lookup instead of O(n)
        visited = set()
        queue = deque([(beginWord, 1)])  # (word, distance)
        visited.add(beginWord)
        
        while queue:
            currentWord, distance = queue.popleft()
            
            # Check if we reached the target
            if currentWord == endWord:
                return distance
            
            # Try all possible one-character changes
            for i in range(len(currentWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == currentWord[i]:
                        continue
                    
                    # Create new word with one character changed
                    newWord = currentWord[:i] + c + currentWord[i+1:]
                    
                    # If new word is valid and not visited
                    if newWord in wordSet and newWord not in visited:
                        visited.add(newWord)
                        queue.append((newWord, distance + 1))

        return 0
