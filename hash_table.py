class HashTable():
    def __init__(self, List=None, size=13, grow_factor=2, size_threshold=0.75):
        self.grow_factor = grow_factor
        self.size_threshold = size_threshold
        if List is None:
            self.table = [self.LinkedList() for _ in range(size)]
            self.size = size
            self.number_of_elements = 0
        else:
            self.table = self.list_to_hash_table(List)
            self.size = len(self.table)
            self.number_of_elements = len(List)
    
    def hash(self, key):
        if isinstance(key, int):
            return key % self.size 
        elif isinstance(key, str) and len(key) != 0:
            hash_value = 0
            for letter in key:
                hash_value += ord(letter)
                hash_value *= ord(letter)
            return hash_value
        else:
            raise Exception('Invalid key!')

    def index(self, key):
        return self.hash(key) % self.size
    
    class LinkedList:
        def __init__(self):
            self.head = None
        
        def __iter__(self):
            node = self.head 
            while node is not None:
                yield node
                node = node.next
        
        def add_first(self, node):
            node.next = self.head 
            self.head = node 
        
        def remove_node(self, key):
            if self.head is None:
                raise Exception('Element not found!')
            if self.head.data[0] == key:
                self.head = self.head.next
                return
            prev_node = self.head 
            for node in self:
                if node.data[0] == key:
                    prev_node.next = node.next 
                    return 
                prev_node = node 
            raise Exception('Element not found!')
        
        def contains_key(self, key):
            for current_node in self:
                if current_node.data[0] == key:
                    return True 
            return False
        
        class Node:
            def __init__(self, data):
                self.data = data 
                self.next = None 
    
    def list_to_hash_table(self, List):
        size = int(len(List) * self.grow_factor)
        table = [self.LinkedList() for _ in range(size)]
        for el in List:
            if not isinstance(el, tuple):
                el = (el, None)
            index = self.hash(el[0]) % len(table)
            node = self.LinkedList.Node(data=el)
            table[index].add_first(node)
        return table
    
    def add(self, key, data=None):
        index = self.index(key)
        if self.table[index].contains_key(key): 
            return 
        self.table[index].add_first(self.LinkedList.Node(data=(key, data)))
        
        if self.size * self.size_threshold > self.number_of_elements + 1:
            self.grow_table()
        
    def remove(self, key):
        index = self.index(key)
        self.table[index].remove_node(key)
        
    def change_data(self, key, data):
        index = self.index(key)
        for node in self.table[index]:
            if node is None:
                raise Exception('Element not found!')
            if node.data[0] == key:
                node.data = (key, data)
        
    def grow_table(self):
        pass

    def __repr__(self):
        nodes = ["------\t START \t------\n"]
        for llist in self.table:
            node = llist.head 
            if node is None:
                nodes.append("None\n")
            else:
                while node.next is not None:
                    nodes.append(f"{node.data[0]}: {node.data[1]}, ")
                    node = node.next
                nodes.append(f"{node.data[0]}: {node.data[1]}\n")
        nodes.append("------\t END \t------\n")
        return ''.join(nodes)
    
    def contains(self, key):
        index = self.index(key)
        if self.table[index].contains_key(key): 
            return True
        return False 
    
if __name__ == '__main__':
    people = HashTable(size=2)
    names = ['Oleg', 'Igor', 'Sasha']
    ages = [21, 53, 17]
    for name, age in zip(names, ages):
        people.add(name, age)
    
    print(people)
    people.change_data(names[1], 54)
    print(people)
    people.remove('Oleg')
    print(people)
    
    people_list = list(zip(names, ages))
    people = HashTable(people_list)
    print(people)