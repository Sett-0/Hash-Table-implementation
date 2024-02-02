class HashTable():
    def __init__(self, List=None, size=10, grow_factor=2, size_threshold=0.75):
        self.grow_factor = grow_factor
        self.size_threshold = size_threshold
        if List is None:
            self.size = size
            self.table = [None] * size
        else:
            self.list_to_hash_table()
    
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
        if self.size * self.size_threshold > len(self.table) + 1:
            self.grow_table()
        index = self.hash(key)
        self.table[index] = (key, data)
        
    def remove(self, key):
        index = self.hash(key)
        self.table[index] = None
        
    def change_data(self, key, data):
        index = self.hash(key)
        self.table[index] = (key, data)
        
    def print(self):
        print('------\t START \t------')
        for el in self.table:
            if el is None:
                print(el)
            else:
                print(el[0], ': ', el[1], sep='')
        print('------\t END \t------')
    
    def list_to_hash_table(self, List):
        pass
    
    def grow_table(self):
        pass
    
if __name__ == '__main__':
    people = HashTable()
    names = ['oleg', 'igor', 'sasha']
    ages = [21, 53, 17]
    for name, age in zip(names, ages):
        people.add(name, age)
    
    people.print()
    people.change_data(names[1], 54)
    people.print()
    people.remove('sasha')
    people.print()