class Producto:
    def __init__(self,name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent, is_increased=True):
        if percent < 0:
            is_increased = False
        
        if is_increased:
            self.price += self.price * percent / 1000
        else:
            self.price -= self.price * percent / 1000

        return self
    
    def print_info(self):
        print("Nombre: ", self.name)
        print("Precio: ", self.price)
        print("categoria: ", self.category)
        return self

