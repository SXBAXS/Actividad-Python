from mamifero import Mamifero
from reptil import Reptil
from escarabajo import escarabajo
from Pato import Pato

def main():
    # Crear instancia de Mamifero
    mamifero1 = Mamifero("Praderas", "Grande", "Caballo", "Mamífero", "Marrón")
    print(mamifero1.mostrar_informacion())
    
    print()  # Línea en blanco para separar las salidas
    
    # Crear instancia de Reptil
    reptil1 = Reptil("Desiertos", "Mediano", "Lagarto", "Reptil", "Escamas rugosas")
    print(reptil1.mostrar_informacion())
    
    print()  # Línea en blanco para separar las salidas
    
    # Crear otra instancia de escarabajo
    
    escarabajo1 = escarabajo("Bosques", "Pequeño", "Escarabajo rinoceronte", "Insecto", "Duras y resistentes")
    print(escarabajo1.mostrar_informacion())
    
    print()  # Línea en blanco para separar las salidas
    
    Pato1 = Pato("Lagos", "Mediano", "Pato mandarín", "Ave", "Ancho y plano")
    print(Pato1.mostrar_informacion())
    
    
if __name__ == "__main__":
    main()
    