import numpy as np

#Función para checar si un numero es primo (Devuelve Booleano)
def Primo(num):
    if num==0 or num==1:
        return False
    for n in range(2,num):
        if(num%n)==0:
            return False
    return True

#Funcion que genera "n" numeros primos (Devuelve una lista)
def genPrimo(num):
    lista=[]
    n=0
    while len(lista)<num:
        if Primo(n):
            lista.append(n)
            n+=1
        else:
            n+=1
    return lista

#Código principal
m=int(input("Introduce el número dimensión 𝑚 de una matriz, mayor o igual a 3: "))
if m>=3:
    l= genPrimo(m**2)
    a=np.array(l).reshape(m,m)
    suma=0
    print("\nLa matriz {}x{} de números primos consecutivos es:\n".format(m,m))
    tu_numero=len(str(l[-1]))
    for i in range(m):
        for j in range(m):
            if j>=i:
                suma+=a[i][j]
                t_numero=len(str(a[i][j]))
            print("{}{}".format(a[i][j],(tu_numero-t_numero+2)*" "),end="")
        print("")
    print("\nLa suma de los elementos en la matriz diagonal superior es: ",suma,"\n")
else:
    print("La dimensión 𝑚 debe ser mayor o igual a 3")