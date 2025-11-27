class Botella:
    def __init__(self, dato_material, dato_capacidad, dato_forma):
        self.material = dato_material
        self.capacidad = dato_capacidad
        self.forma = dato_forma

    def contener_liquido(self, dato_liquido):
        mensaje = f"La botella contiene {dato_liquido} y tiene una capacidad de {self.capacidad}"
        return mensaje

    def get_material(self):
        return self.material

    def set_material(self, dato_material):
        self.material = dato_material

    def imprimir_datos(self):
        mensaje = (
            f"La botella está hecha de {self.material}, "
            f"tiene una capacidad de {self.capacidad} y tiene forma {self.forma}"
        )
        print(mensaje)
    
