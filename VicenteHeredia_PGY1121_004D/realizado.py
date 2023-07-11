import os
import numpy as np
import validacionesexamen as val
os.system("cls")
op=0

dep=np.empty([10,4], type(int))


val.llenarMatriz(dep)


while(op!=4):
    print(" ******* CASA FELIZ  ****** ")
    print("1. Comprar departamento ")    
    print("2. Mostrar departamentos disponibles ")
    print("3. Ver,listado de compradores ")
    print("4. Mostrar ganancias totales ")
    print("5. Salir")


    op=val.menuvalido(op)


    

    if(op==1):
       
        val.mostrardispo(dep)
        numdep=val.validanumdep()
        comprueba= val.buscarDisponible(dep,numdep)
        if comprueba:      
            print("Felicidades, el departamento esta disponible")
            pagar=val.comprardep(dep, numdep)
            print("\t Usted va a pagar: ", pagar)
        else: 
            print("\t El departamento no esta disponible")
        os.system("pause")




    if(op==2):
    
        val.mostrardispo(dep)
        os.system("pause")
    




    if(op==3):
        print("no alcanzo a hacerla")



    if (op==4):
        
        suma=0
        suma=val.totalVenta(dep)
        if (suma==0):
            print("\t No hay departamentos vendidos")
        else:
            print("\t El total vendido $ es: ", suma)
 

        os.system("pause")

        




    if(op==5):

        print("\tAdios, Esperamos que vuelva pronto!")
        print("Vicente Heredia, 11/7/2023")
        break



