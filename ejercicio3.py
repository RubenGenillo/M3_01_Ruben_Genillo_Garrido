#Creo una clase llamada Producto que tenga los atributos código, nombre, precio y tipo
class Producto():
    #Creo el constructor de la clase con el que imprimo por pantalla que el producto se ha creado con éxito
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print("El producto se ha creado con exito")
    #Creo el método __str__ para visualizar por pantalla la información de los productos    
    def __str__(self):
        return"codigo: {}, nombre: {}, precio: {}, tipo: {}".format(self.codigo, self.nombre, self.precio, self.tipo)

#Creo algunos productos y pruebo a mostrar los datos de estos y modificar algún valor
mesa = Producto(18500, "mesa", 49.99, "mueble")
lavadora = Producto(16453, "lavadora", 299.99, "electrodomestico")
microondas = Producto(16464, "microondas", 29.99, "electrodomestico")
print(mesa)
print(lavadora)
print(microondas)
lavadora.precio = 249.99
print(lavadora)
