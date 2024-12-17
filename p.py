class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        # print('name: ', self.name, 'price: ', self.price)
        print(f'name: {self.name} price: {self.price}')
        # write a method to display the product's name and price

class Book(Product):
    def apply_discount(self, percent):
        discount = self.price * (percent/100)
        total_price = self.price - discount
        # print('Discounted price:',total_price)
        print(f'Discounted price: {round(total_price)}')
        # write a method to calculate the discounted price

class Electronics(Product):
    def warranty_info(self, years):
        # print(self.name, "has", years, "of warranty")
        print(f'{self.name} has {years} of warranty.')
        # write a method to display how many years of warranty the product comes with.

my_name = input("Enter a name: ")
my_price = int(input("Enter a price: "))
obj_1 = Book(my_name, my_price)
obj_1.apply_discount(35)