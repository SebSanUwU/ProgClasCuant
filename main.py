import lib

def canicas():
    tam=int(input("\nNumero de vertices: "))
    print("\nIngrese el vector estado dejando un espacio entre los numeros")
    vecEstado=input("? ")
    vecEstado=lib.llenarArr(vecEstado)
    matrizD=lib.crearMatriz(tam)
    clicks=int(input("Ingrese el numero de clicks: "))
    while clicks>=0:
        print("Vector estado al click ",clicks)
        print(lib.clicksClasico(matrizD,vecEstado,clicks))
        clicks=int(input("Ingrese el numero de clicks, -1 para terminar"))

def exDobleRenClas():
    ren=int(input("\nNumero de rendijas: "))
    print("\nIngrese las probabilidades de cada rendija dejando un espacio entre los numeros")
    probRen=input("? ")
    target = int(input("\nNumero de blancos: "))
    vecEstado=lib.vectorEstado(ren,target)
    matrizD=lib.crearMatrizDobRen(probRen,ren,target)
    clicks = int(input("Ingrese el numero de clicks: "))
    lib.Matrix(matrizD)

    while clicks >= 0:
        print("Vector estado al click ", clicks)
        print(lib.clicksClasico(matrizD, vecEstado, clicks))
        clicks = int(input("Ingrese el numero de clicks, -1 para terminar"))

def exDobleRenCuan():
    ren = int(input("\nNumero de rendijas: "))
    target = int(input("\nNumero de blancos: "))
    vecEstado = lib.vectorEstadoQ(ren, target)
    matrizD = lib.crearMatrizDobRenQ(ren, target)
    clicks = int(input("Ingrese el numero de clicks: "))
    lib.Matrix(matrizD)

    while clicks >= 0:
        print("Vector estado al click ", clicks)
        print(lib.clicksCuantico(matrizD, vecEstado, clicks))
        clicks = int(input("Ingrese el numero de clicks, -1 para terminar"))



def main():
    print("PROGRAMA SIMULACIÓN DE LO CLÁSICO A LO CUÁNTICO")
    pick=0
    while pick>=0 and pick<4:
        print("\n1. Los experimentos de la canicas con coeficiente booleanos")
        print("2. Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas")
        print("3. Experimento de las múltiples rendijas cuántico")
        print("4. Cree una función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados. La imagen se debe poder guardar en el computador con un formato de imagen.")
        pick=int(input("? "))
        if pick==1 :
            canicas()
        elif pick==2:
            exDobleRenClas()
        elif pick==3:
            exDobleRenCuan()

    print(":)")

main()
