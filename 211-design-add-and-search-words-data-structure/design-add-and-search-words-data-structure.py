class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def search_in_node(word, node) -> bool:
            for i in range(len(word)):
                char = word[i]
                if char in node.children:
                    node = node.children[char]
                else:
                    if char == '.':
                        for child in node.children:
                            if search_in_node(word[i+1:], node.children[child]):
                                return True
                    return False
            return node.is_end_of_word

        return search_in_node(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
