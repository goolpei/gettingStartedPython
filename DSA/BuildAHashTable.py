class HashTable:
    def __init__(self):
        self.collection = {}
    
    def __str__(self):
        return str(self.collection)

    def hash(self, string: str) -> int:
        return sum(ord(char) for char in string)

    def add(self, key, value) -> None:
        key_hash = self.hash(key)
        if key_hash in self.collection:
            self.collection[key_hash][key] = value
        else:
            self.collection[key_hash] = {key: value}

        # # If bucket doesn't exist, create it
        # if key_hash not in self.collection:
        #     self.collection[key_hash] = {}
            
        # # Insert key-value pair into the bucket
        # self.collection[key_hash][key] = value

    def remove(self, key) -> None:
        key_hash = self.hash(key)
        if key_hash in self.collection and key in self.collection[key_hash]:
            del self.collection[key_hash][key]
        # Optional: clean up empty buckets
            if not self.collection[key_hash]:
                del self.collection[key_hash]

    def lookup(self, key):
        key_hash = self.hash(key)
        if key_hash in self.collection and key in self.collection[key_hash]:
            return self.collection[key_hash][key]
        return None
        # bucket = self.collection.get(key_hash)
        # if bucket is not None:
        #     return bucket.get(key)
        # return None

h = HashTable()
print(h.hash('a'))
h.add('fcc', 'b')

print(h)
print(h.lookup('cfc'))