def transpuestaMV(v):
    transpuesta = []
    for i in range(len(v[0])):
        transpuesta.append([])
        for j in range(len(v)):
            transpuesta[i].append(v[j][i])
    return transpuesta

def prodrealesMv(v, w):
    if len(v) != len(w[0]):
        return 'No'

    prod = []
    i = 0
    while i < len(v[0]):
        prod.append([])
        j = 0
        while j < len(w):
            k = 0
            suma = 0

            while k < len(v):
                suma = suma + v[k][i] * w[j][k]
                k += 1
            prod[i].append(suma)
            j += 1
        i += 1
    return transpuestaMV(prod)

def sumacplx(a,b):
	real=(a[0]+b[0])
	img=(a[1]+b[1])
	return (real,img)

def multcplx(a,b):
	real=(a[0]*b[0])-(a[1]*b[1])
	img=(a[0]*b[1])+(a[1]*b[0])
	return (real,img)


def prodMv(v,w):
    if len(v)!=len(w[0]):
        return 'No'

    prod=[]
    i=0
    while i<len(v[0]):
        prod.append([])
        j=0
        while j<len(w):
            k=0
            suma=(0,0)

            while k<len(v):
                suma=sumacplx(suma,multcplx(v[k][i],w[j][k]))
                k+=1
            prod[i].append(suma)
            j+=1
        i+=1


    return transpuestaMV(prod)


def llenarArr(cadena):
    arr = cadena.split(" ")
    for i in range(len(arr)):
        arr[i] = tuple(arr[i])
    return arr


def crearMatriz(tam):
    res = []
    for i in range(tam):
        print("\nIngrese el vector ", i, " dejando un espacio entre los numeros")
        vector = input("? ")
        res.append(llenarArr(vector))
    return res


def clicksClasico(matriz, arr, clicks):
    arr = [arr]
    i = 0
    while i < clicks:
        # print(matriz)
        arr = prodrealesMv(matriz, arr)
        i += 1
    return arr[0]

def clicksCuantico(matriz, arr, clicks):
    arr = [arr]
    i = 0
    while i < clicks:
        # print(matriz)
        arr = prodMv(matriz, arr)
        i += 1
    return arr[0]

def vectorEstado(tam,target):
    vec=[0 for i in range(0, target + tam+1)]
    vec[0]=1
    return vec

def Matrix(matrixD):
  for i in range(0,len(matrixD)):
    p_filas=""
    for j in range(0,len(matrixD[i])):
      p_filas+=str(matrixD[j][i])+" "
      p_filas = p_filas[:-1]
      p_filas += ""
    print(p_filas)

def crearMatrizDobRen(vec,tam,target):
    vec=llenarArr(vec)
    matrixD = [[0 for i in range(0, target + tam+1)] for j in range(0, target + tam+1)]

    i=1
    while i<=tam:
        matrixD[0][i]=vec[i-1]
        i+=1

    for i in range(tam+1,len(matrixD)):
        for j in range(tam+1,len(matrixD)):
            if i==j:
                matrixD[i][j]=1

    if tam%2==0:
        if target % tam == 0:
            eachOne = (target / tam)+1
            comp = 2
        else:
            eachOne = (target // tam)+1
            comp=1
    else:
        comp = 2
        eachOne = (target // tam) + 2
        if target%tam==0:
            eachOne = (target / tam) + 2
            comp = 3

    base=int(tam+1)
    sum=int(eachOne+base)
    print("\nIngrese las probabilidades")
    for i in range(1,tam+1):
        for j in range(base,sum):
            print(i,"->",j)
            matrixD[i][j]=float(int(input("? ")))
        base=int(base+eachOne-comp)
        sum=int(sum+eachOne-comp)
    return matrixD

def vectorEstadoQ(tam,target):
    vec=[(0,0) for i in range(0, target + tam+1)]
    vec[0]=(1,0)
    return

def ingresoComplejo():
    real = float(input("real "))
    img = float(input("img "))
    return (real, img)

def crearMatrizDobRenQ(tam,target):
    matrixD = [[(0, 0) for i in range(0, target + tam+1)] for j in range(0, target + tam+1)]
    print(matrixD)

    for i in range(1,tam+1):
        print("Rendija",i)
        matrixD[0][i]=ingresoComplejo()

    for i in range(tam+1,len(matrixD)):
        for j in range(tam+1,len(matrixD)):
            if i==j:
                matrixD[i][j]=(1,0)

    if tam%2==0:
        if target % tam == 0:
            eachOne = (target / tam)+1
            comp = 2
        else:
            eachOne = (target // tam)+1
            comp=1
    else:
        comp = 2
        eachOne = (target // tam) + 2
        if target%tam==0:
            eachOne = (target / tam) + 2
            comp = 3
    base=int(tam+1)
    sum=int(eachOne+base)
    print("\nIngrese las probabilidades")
    for i in range(1,tam+1):
        for j in range(base,sum):
            print(i,"->",j)
            matrixD[i][j]=ingresoComplejo()
        base=int(base+eachOne-comp)
        sum=int(sum+eachOne-comp)
    return matrixD




