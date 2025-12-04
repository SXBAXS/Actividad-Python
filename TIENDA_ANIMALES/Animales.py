class Animales:
    def __init__(self, dato_habitat, dato_tamano,dato_nombre, dato_clase_animales):
        self.habitat = dato_habitat
        self.tamano = dato_tamano
        self.nombre = dato_nombre
        self.clase_animales = dato_clase_animales
        
    def mostrar_informacion(self):
        mensaje = (
            f"El animal {self.nombre} pertenece a la clase {self.clase_animales}, "
            f"habita en {self.habitat} y tiene un tamaño de {self.tamano}."
        )
        return mensaje