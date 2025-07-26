class Inventory:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    # inv = Inventory(10)
    # print(inv._Inventory__capacity)  # Outputs: 10
    
    def add_item(self, item):
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return (
                "not enough room in the"
                " inventory"
            )
    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return (
            f"Items: {', '.join(self.items)}.\n"
            # you need to escape the double quotes
            # with single ones
            f"Capacity left: {self.__capacity - len(self.items)}"
        )
