#Copio la clase del ejércicio anterior y le añado un método -str- que imprimirá por pantalla el nombre y nota del alumno
class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumnno {} creado con exito".format(self.nombre))
    def calificacion(self):
        if self.nota < 5:
            print("Ha suspendido")
        else:
            print("Ha aprovado")    
    def __str__(self):
        return "Alumnno {} tiene un {}".format(self.nombre, self.nota)             

#Creo algunos objeto de la clase Alumno y realizo print para cada uno de ellos (para visualizar por pantalla la información del str)
alumno1 = Alumno("Pedro", 8)
alumno2 = Alumno("Julia", 8)
alumno3 = Alumno("Esteban", 4)
print(alumno1)
print(alumno2)
print(alumno3)
