
from importlib.metadata import PackageNotFoundError
import numpy as np

import os

def menuvalido(op):
    while(True):
        try:
            op=int(input(" Elija opción: "))
            if(op>=1 and op<=5):
                break
            else:
                print("debe ingresar una opcion que se muestre en pantalla (un numero entre 1 y 5)")
        except ValueError:
            print("Debe ingresar un numero entero entre 1 y 5")
    return op


##

def llenarMatriz(mat):
    p=1
    for i in range(10):
        for j in range(4):
            mat[i,j]=p
            p+=1






   
def mostrardispo(dep):
    os.system("cls")

    print("         A       B               C       D    ")
    for i in range(10):
        print("\n") 
        for j in range(4):
            if(j==1):
                print("\t",dep[i,j], end="        ")
            else:
                print("\t",dep[i,j], end="    ")
    print("\n\n")
    
def validanumdep():
    numdep=0
    while True:
        try: 
            numdep=int(input("Ingrese número del departamento que desea comprar 1-40: "))
            if (numdep>=1 and numdep<=40):
                break
            else:
                print(" Error.. ingrese numero de departamento entre  1 y 40")
        except ValueError:
            print(" Error.. ingrese umero de departamento entre  1 y 40")
    return numdep
def buscarDisponible(dep, numdep):
    for x in range(10):
        for i in range(4):
            if (numdep==dep[x,i]):
                return True
    return False 



def ValidaRut(rut):
    os.system=""
    while(len(rut1)<=0):
        rut1=input("Por favor ingrese su rut:  ")
        if(len(rut1)<8):
            print("ingrese su rut sin puntos ni guion")
            rut1=""
    rut.append(rut1)



def comprardep(dep, numdep):
  
    for x in range(10):
        for i in range(4):
            if (dep[x,i]==numdep):
                dep[x,i]="x"         
                if i==0: 
                    pago=3800 
                    

                if i==1 :
                    pago=3000
                   

                if i==2 :
                    pago=2800   
                   
                if i==3 :
                    pago=3500
                    



    return pago







def totalVenta(dep):
    suma=0
   
    for x in range(10):
        for i in range(4):
            if (dep[x,i]==0):
                if (i==0 ):
                    suma+=3800
                  


                if (i==1 ):
                    suma+=3000
                   


                if (i==2):
                    suma+=2800
                    
                if (i==3):
                    suma+=3500  
                
    return suma




