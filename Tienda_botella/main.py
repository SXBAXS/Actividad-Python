from botella import Botella
from botella_plastica import Botella_plastica
from botella_vidrio import Botella_vidrio

# Crear objeto de Botella
obj_botella = Botella("Aluminio", "1.5 Litros", "Cónica")

# Llamar funciones
dato_atributo = obj_botella.get_material()
dato_liquido = obj_botella.contener_liquido("COCA COLA")
print(dato_liquido)
print(dato_atributo)
# Botella plástica
obj_botella_plastica = Botella_plastica("\nPlástico", "3 Litros", "Ovalada", "Azul Translúcido", "Grande")
imprimir_plastico = obj_botella_plastica.imprimir_datos()
print(imprimir_plastico)
# Botella vidrio
obj_botella_vidrio = Botella_vidrio("\nVidrio", "2 Litros", "Circular", "Templado", "Grande")
imprimir_vidrio = obj_botella_vidrio.imprimir_datos()
print(imprimir_vidrio)

