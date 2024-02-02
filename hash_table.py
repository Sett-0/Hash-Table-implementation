class HashTable():
    def __init__(self, List=None, size=10) -> None:
        self.size = size
        self.grow_factor = 0.75
    
    def hash(self, key):
        if isinstance(key, int):
            return key % self.size 
        elif isinstance(key, str) and len(key) != 0:
            hash_value = 0
            for letter in key:
                hash_value += ord(letter)
                hash_value *= ord(letter)
            return hash_value % self.size
        else:
            raise Exception('Invalid key!')

    def add(self, key, data=None):
        pass 
    
if __name__ == '__main__':
    table = HashTable()
    names = ['oleg', 'igor', 'sasha']
    print('------\t START \t------')
    for name in names:
        print(name + '\t: %d' % table.hash(name))
    print('------\t END \t------')
        