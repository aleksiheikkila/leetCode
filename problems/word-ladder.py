# https://leetcode.com/problems/word-ladder

#from string import ascii_lowercase
from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """Improved by using word neighbors"""
        
        wordset = set(wordList)
        if endWord not in wordset:
            # cannot get there
            return 0

        neighb_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # from s we can go to neighb_words[s] (list) words
                s = word[:i] + "_" + word[i+1:]
                neighb_words[s].append(word)
        
        N = len(endWord)
        
        level = 1
        q = deque([(beginWord, level)])
        
        # remove from wordset, to block from going back to already discovered nodes
        # Do this when we add stuff to the queue
        if beginWord in wordset:
            wordset.remove(beginWord)
        
        # Queue: append to add, popleft to remove
        while q:
            curr_word, level = q.popleft()
            
            # for every position, try possible valid word neighbors
            for i in range(N):
                s = curr_word[:i] + "_" + curr_word[i+1:]
                for new_word in neighb_words[s]:
                    if new_word == endWord:
                        return level + 1
                    
                    if new_word in wordset:
                        q.append((new_word, level + 1))
                        wordset.remove(new_word)

        # else not found
        return 0