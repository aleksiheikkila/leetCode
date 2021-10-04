# https://leetcode.com/problems/design-add-and-search-words-data-structure

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode("")
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                newNode = TrieNode(c)
                node.children[c] = newNode
            node = node.children[c]
        node.is_end = True
        

    def search(self, word: str) -> bool:
        # in BFS manner
        stack = [self.root]
        
        for c in word:
            new_stack = []
            while stack:
                node = stack.pop()
                if c in node.children:
                    new_stack.append(node.children[c])
                elif c == ".":
                    # need to continue to explore all children
                    for child in node.children.values():
                        new_stack.append(child)                
            
            if not new_stack:
                return False
            stack = new_stack

        # There was a path to the search word
        # need to still check that that is an end of word for at least one of them
        return any(node.is_end for node in stack)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)