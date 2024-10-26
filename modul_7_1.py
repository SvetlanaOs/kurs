from pprint import pprint
class Product:
    def __init__(self, name :str, weight: float, category: str):
        self. name = name
        self. weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self._file_name = 'products.txt'
    def get_products(self):
        file = open('products.txt', 'r')
        print(file.read())
        file.close()
    def add(self, *products):
        file = open(self._file_name, 'r')
        x = str(file.read())
        file.close()
        for i in  products:
            if str(i) in x:
                print(f'Продукт {i} уже есть в магазине')
            else:
                file = open(self._file_name, 'a')
                file.write(f'{str(i)}\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)# __str__

s1.add(p1, p2, p3)

print(s1.get_products())