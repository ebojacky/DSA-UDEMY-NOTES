class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]

            else:
                node.children[char] = TrieNode()
                node = node.children[char]

        node.end_of_string = True

    def search_word(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            else:
                node = node.children[char]

        if node.end_of_string:
            return True

        return False

    def delete_word_simple(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return
            else:
                node = node.children[char]

        node.end_of_string = False

    def print_helper(self, root: TrieNode, word):
        if root.end_of_string:
            print(word)

        for char, next_node in root.children.items():
            new_word = word + char
            self.print_helper(next_node, new_word)

    def print_all_words(self):
        self.print_helper(self.root, "")

    def delete_word_complex(self, word):

        def dfs(node: TrieNode, word, depth):

            if len(word) == depth:
                if node.end_of_string:
                    node.end_of_string = False
                if len(node.children) == 0:
                    return True
                else:
                    return False

            char = word[depth]
            if char not in node.children:
                return False

            delete_current_reference = dfs(node.children[char], word, depth + 1)

            if delete_current_reference:
                node.children.pop(char) # or del node.children[char]

            return False

        dfs(self.root, word, 0)





my_trie = Trie()
my_trie.insert_word("EBO")
my_trie.insert_word("EBOW")
my_trie.insert_word("ESTEE")
my_trie.insert_word("EST")
my_trie.insert_word("EMONEY")
my_trie.insert_word("JOJO")
print(my_trie.search_word("EBOW"))
print(my_trie.search_word("JOJO"))
my_trie.delete_word_simple("JOJO")
print(my_trie.search_word("JOJO"))
my_trie.insert_word("JOJOE")
print(my_trie.search_word("JOJOE"))
my_trie.insert_word("UNDER")
my_trie.insert_word("UNDERSTAND")
print("---")
my_trie.delete_word_simple("UNDER")
print(my_trie.search_word("UNDER"))
print(my_trie.search_word("UNDERSTAND"))
my_trie.print_all_words()
print("---")
my_trie.delete_word_complex("EBOW")
my_trie.print_all_words()
print("---")
my_trie.delete_word_complex("EST")
my_trie.print_all_words()

