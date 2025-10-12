class MagicDictionary:

    def __init__(self):
        self.words = set()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words.add(word)

    def search(self, searchWord: str) -> bool:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i, c in enumerate(searchWord):
            for char in alphabet:
                if c != char:
                    temp = searchWord[:i] + char + searchWord[i+1:]
                    if temp in self.words:
                        return True
        return False

            
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)