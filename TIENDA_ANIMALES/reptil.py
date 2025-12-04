from Animales import  Animales
class Reptil(Animales):
    def __init__(self, dato_habitat, dato_tamano,dato_nombre, dato_clase_animales, dato_tipo_escamas):
        super().__init__(dato_habitat, dato_tamano,dato_nombre, dato_clase_animales)
        self.tipo_escamas = dato_tipo_escamas

    def mostrar_informacion(self):
        mensaje = (
            f"El {self.nombre} pertenece a la clase {self.clase_animales}, "
            f"habita en {self.habitat}, tiene un tamaño {self.tamano} "
            f"y su tipo de escamas es {self.tipo_escamas}."
        )
        return mensaje