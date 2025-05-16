class Zoo:
    __animals = 0 

    '''double underscore triggers name mangling, where the attribute name is internally changed to include the class name, making it harder to access from outside the class'''

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
            
        Zoo.__animals += 1
    
    def get_info(self, species):
        result = ""
        if species == 'mammal':
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"


        result += f"Total animals: {Zoo.__animals}"
        return result

if __name__ == '__main__':
    
    a = Zoo(str(input()))
    b = int(input())

    for i in range(b):
        c = input().split(' ')
        a.add_animals(c[0], c[1])

    print(a.get_info(input()))









