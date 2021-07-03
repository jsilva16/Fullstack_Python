import product as prod
class Store:
    def __init__(self, name, products=[]):
        self.name = name
        self.product = products


    def add_product(self, new_prod):
        self.product.append(new_prod)
        print(f"Se ha agregado el producto '{new_prod}'")
        return self
    
    def delete_prod(self, id):
        print("Imprimiendo al información del producto a eliminar")
        self.product[id].print_info()
        print("El producto ha sido eliminado")
        del self.product[id]
        return self
    
    def inflation(self,porcentaje):
        for prod in self.product:
            prod.update_price(porcentaje)
        return self

    def update_category(self,category, percent):
        for prod in self.product:
            if prod.category == category:
                prod.update_price(percent, False)
        return self



store1=Store("tienda")
store1.add_product("Agua", 500, "bebidas")
store1.add_product("pan", 900, "panaderia")
print(store1.name)
print(store1.product)
dir(store1)
