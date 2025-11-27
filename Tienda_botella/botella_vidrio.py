from botella import Botella

class Botella_vidrio(Botella):
    def __init__(self, dato_material, dato_capacidad, dato_forma, dato_tipoVidrio, dato_tamano):
        super().__init__(dato_material, dato_capacidad, dato_forma)
        self.tipoVidrio = dato_tipoVidrio
        self.tamano = dato_tamano

    def imprimir_datos(self):
        dato_mensaje = super().imprimir_datos()
        mensaje = dato_mensaje + f". El tipo de vidrio de la botella es {self.tipoVidrio} y su tamaño es {self.tamano}"
        print(mensaje)  
