import random

class RandomizedSet:
    def __init__(self):
        """
        Initialize the RandomizedSet object.
        """
        self.elements = []  # List to store elements
        self.index_map = {}  # Dictionary to map elements to their index

    def insert(self, val: int) -> bool:
        """
        Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
        """
        if val in self.index_map:
            return False

        self.index_map[val] = len(self.elements)
        self.elements.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes an item val from the set if present. Returns true if the item was present, false otherwise.
        """
        if val not in self.index_map:
            return False

        last_element = self.elements[-1]
        val_index = self.index_map[val]

        self.index_map[last_element] = val_index
        self.elements[val_index] = last_element

        self.elements.pop()
        del self.index_map[val]

        return True

    def getRandom(self) -> int:
        """
        Returns a random element from the current set of elements.
        """
        return random.choice(self.elements)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
