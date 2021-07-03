class Producto:
    def __init__ (self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, porcentaje, esIncrementado):
        if esIncrementado:
            #self.precio = self.precio + self.precio*porcentaje/100  self.precio*(1 + porcentaje/100)
            self.precio += self.precio*porcentaje/100
        else:
            self.precio -= self.precio*porcentaje/100
        return self

    def print_info(self):
        print("Nombre: ", self.nombre)
        print("Precio: ", self.precio)
        print("categoria: ", self.categoria)
        return self


import store as store
import product as producto

tienda1 = store.Store("tiendita")
prod1 = producto.Producto("Agua mineral", 1000, "Bebidas")
prod2 = producto.Producto("Pan", 1000, "Panaderia")
prod3 = producto.Producto("Tallarines", 1000, "Masas")

tienda1.agregar_producto(prod1).agregar_producto(prod2).agregar_producto(prod3)

print("Productos")
prod1.print_info()
print("")
prod2.print_info()
print("")
prod3.print_info()
print("")
tienda1.eliminar_producto(1)
print("")


print("************************************")
tienda1.actualizar_categoria("Bebidas",10).inflacion(3)

prod1.print_info()
print("")

prod3.print_info()
print("")