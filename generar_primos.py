import numpy as np


def Recolectar_primos_archivo(filename):
    p_numbs = []
    #El código supone que los números empiezan en 2
    with open(filename,"a+") as file:
        data = file.readlines()
        for d in data:
            p_numbs.append(int(d.rstrip('\n')))

    return np.array(p_numbs)

def Escribir_Primos_Archivo(filename,datos):
    with open(filename,"a+") as file:
        for n in datos:
            file.write("{}\n".format(n))

def Criba(a,b,filename="datos.txt"):
    p_numbs = Recolectar_primos_archivo(filename)
    if p_numbs.size == 0:
        p = np.ones((b+1))
        p[0]=p[1]=0
        for i in range(2,int(b**0.5)+1):
            if p[i]==1:
                l = range(i**2,b+1,i)
                p[l]=0
        p_numbs = [i for i,pu in enumerate(p) if pu]        
        print(p)
        Escribir_Primos_Archivo(filename,p_numbs)
    else:
        #Calculamos el array de no-primos anteriores
        p_arr = np.ones((b+1))
        p_arr[0]=p_arr[1]=0
        for p in p_numbs:
            r = range(p**2,b+1,p)
            p_arr[r]=0

        #Calculamos para los siguientes números
        for i in range(max(p_numbs),int(b**0.5)+1):
            if p_arr[i]:
                r = np.array(range(i**2,b+1,i))
                p_arr[r]=0
        
        #Añadimos al archivo
        p_nnumbs = []
        for i in range(max(p_numbs)+1,b):
            if p_arr[i]:
                p_nnumbs.append(i)
        Escribir_Primos_Archivo(filename,p_nnumbs)
Criba(0,1000)