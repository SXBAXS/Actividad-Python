from Animales import Animales
class Mamifero(Animales):
    def __init__(self, dato_habitat, dato_tamano,dato_nombre, dato_clase_animales, dato_color_pelo):
        super().__init__(dato_habitat, dato_tamano,dato_nombre, dato_clase_animales)
        self.color_pelo = dato_color_pelo

    def mostrar_informacion(self):
        mensaje = (
            f"El {self.nombre} pertenece a la clase {self.clase_animales}, "
            f" habita en {self.habitat}, tiene un tamaño {self.tamano} "
            f"y su color de pelo es {self.color_pelo}."
        )
        return mensaje