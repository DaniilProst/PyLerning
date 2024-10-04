from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        f_product = open(self.__file_name, 'r')
        return f_product.read()

    def add(self, *products):

        f_product = open(self.__file_name, 'a')
        existing_products = self.get_products().strip().split('\n')
        existing_product_names = {product.split(', ')[0] for product in existing_products}

        for i in products:
            if i.name in existing_product_names:
                print(f"Продукт {i.name} уже есть в магазине")
            else:
                f_product.write(str(i) + '\n')

        f_product.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
