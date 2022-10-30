#Creo una clase llamada Alumno que tenga los atributos nombre y nota
class Alumno():
    #Creo el constructor de la clase con el que imprimo por pantalla si el alumno ha aprobado o suspendido en base a su nota
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumnno {} creado con exito".format(self.nombre))
    def calificacion(self):
        if self.nota < 5:
            print("Ha suspendido")
        else:
            print("Ha aprovado") 

#Creo algunos alumnos y ejecuto el método calificacion para cada uno de ellos
alumno1 = Alumno("Pedro", 8)
alumno1.calificacion()
alumno2 = Alumno("Javier", 7)
alumno2.calificacion()
alumno3 = Alumno("Julia", 8)
alumno3.calificacion()
alumno4 = Alumno("Esteban", 4)
alumno4.calificacion()