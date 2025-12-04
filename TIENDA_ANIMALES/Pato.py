from Animales import Animales

class Pato(Animales):
    def __init__(self, dato_habitat, dato_tamano, dato_nombre, dato_clase_animales, dato_tipo_pico):
        super().__init__(dato_habitat, dato_tamano, dato_nombre, dato_clase_animales)
        self.tipo_pico = dato_tipo_pico

    def mostrar_informacion(self):
        mensaje = (
            f"El {self.nombre} pertenece a la clase {self.clase_animales}, "
            f"habita en {self.habitat}, tiene un tamaño {self.tamano} "
            f"y su tipo de pico es {self.tipo_pico}."
        )
        return mensaje