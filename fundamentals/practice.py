import csv


class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        #Run validations to the received arguments
        assert price >= 0, f"price {price} is not good!"
        assert quantity >= 0, f"quantity {quantity} is not good!"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        #back sure the pay rate is applied at a instance level (self)
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity'))
            )
        
        #return represented objects in a list all [] istead of obejcts
    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"



# item1 = Item("iphone", 100, 2)
# print(item1.quantity)
# item1.apply_discount()
# print(item1.name)
# print(item1.price)



# item2 = Item("iphone X", 1000, 1)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.name)
# print(item2.price)


# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 6)
# item3 = Item("Cable", 20, 3)
# item4 = Item("Mouse", 50, 3)
# item5 = Item("Keyboard", 75, 2)



Item.instantiate_from_csv()
print(Item.all)


# print(Item.all)

# for instance in Item.all:
#     print(instance.name)