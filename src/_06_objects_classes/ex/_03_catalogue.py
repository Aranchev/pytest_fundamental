class Catalogue:

#    self.products = []  makes it per instance
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)
    
    def get_by_letter(self, first_letter: str):
        c = []
        for i in self.products:
            if i.startswith(first_letter):
                c.append(i) 
        return c
    
    def __repr__(self):
        output = f"Items in the {self.name} catalogue:\n"
        output += '\n'.join(sorted(self.products))
        return output
