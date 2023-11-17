class AllOne:

    def __init__(self):
        self.key_count = {}
        self.count_key = {}

    def inc(self, key: str) -> None:
        count = self.key_count.get(key, 0)
        new_count = count + 1

        # Update key_count dictionary
        self.key_count[key] = new_count

        # Update count_key dictionary
        if new_count not in self.count_key:
            self.count_key[new_count] = [key]
        else:
            self.count_key[new_count].append(key)

        # Remove key from its previous count in count_key
        if count > 0:
            self.count_key[count].remove(key)
            if not self.count_key[count]:
                del self.count_key[count]

    def dec(self, key: str) -> None:
        count = self.key_count.get(key, 0)

        if count == 0:
            return

        # Update key_count dictionary
        new_count = count - 1
        if new_count > 0:
            self.key_count[key] = new_count
        else:
            del self.key_count[key]

        # Update count_key dictionary
        self.count_key[count].remove(key)
        if not self.count_key[count]:
            del self.count_key[count]

        if new_count > 0:
            if new_count not in self.count_key:
                self.count_key[new_count] = [key]
            else:
                self.count_key[new_count].append(key)

    def getMaxKey(self) -> str:
        if not self.count_key:
            return ""
        max_count = max(self.count_key.keys())
        return self.count_key[max_count][0]

    def getMinKey(self) -> str:
        if not self.count_key:
            return ""
        min_count = min(self.count_key.keys())
        return self.count_key[min_count][0]

