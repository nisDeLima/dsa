Prefix–Suffix Trie Approach

The main idea was to store both prefix and suffix information in the same Trie, instead of using two separate ones.

Using two different Tries (one for prefixes and one for suffixes) would cause problems when trying to count only the words that are both a prefix and a suffix of the same word.
Otherwise, you could end up counting a word that is a prefix of one word and a suffix of another, which isn’t what we want.
To fix that using two Tries, you’d have to track indexes for every match and then cross-reference them to find overlaps. That would increase time complexity and make the logic unnecessarily messy.

The clean solution was to create a single Trie built on pairs (s, e), where:

s is the character from the start of the word (left to right),

e is the character from the end of the word (right to left).

By inserting words using these (s, e) pairs, each node directly represents the combined prefix–suffix state at a given position.
This allows us to determine whether a word is both a prefix and a suffix of another word immediately, without any extra lookups or index comparisons.

To keep counting efficient, each Trie node stores a simple count attribute, tracking how many words have passed through that node.
That’s all that’s needed to know how many existing words match a new one’s prefix–suffix pattern.
