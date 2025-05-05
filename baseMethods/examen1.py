#Examen 1 - Natalia Mora L. V-30.416.997 - Resuelto: 3/4
from math import *
#SIN faltantes ni nada de eso
def calcsLoteEconomico(medidaCalcs):
    if(medidaCalcs==1):
        #
        print("Medida elegida: Diario - Calculos x Dia \n")
        nombreMedida = "diaria/diario"
        #
    elif(medidaCalcs==2):
        #
        print("Medida elegida: Semanal - Calculos x Semana \n")
        nombreMedida = "semanal"
        #
    elif(medidaCalcs==3):
        #
        print("Medida elegida: Anual - Calculos x Año \n")
        nombreMedida = "anual"
        #
    else:
        print("Uy! Error, medida incorrecta, vuelve a ejecutar el programa y elige una opcion\n")
    #
    #
    print("--------------------------------------------------------------------------------------------------------------------------")
    producto = (input("Que tipo de producto se está manejando para ésta producción?\n"))
    print("--------------------------------------------------------------------------------------------------------------------------")

    print(f" * IMPORTANTE!! NO OLVIDE *")
    print(f" TODOS los valores solicitados a continuacion deben estar en unidades/medidas: {nombreMedida} \n")
    print("--------------------------------------------------------------------------------------------------------------------------")

    D = float(input("Ingrese el valor de la demanda(D): \n"))
    #D = d/52

    c = float(input("Ingrese el valor del costo por producto (c): \n"))

    L = float(input("Ingrese el valor del tiempo de entrega (L): \n"))
    #L = lWeekly / 52
    
    k = float(input("Ingrese el valor del costo de produccion (k): \n"))
    
    #
    h = float(input("ingrese el valor del costo de almacenamiento / inventario (h): \n"))
    
    #porc = float(input("Para calcular el costo anual de (h), ingrese el porcentaje del valor del inventario promedio (Ej: 0.20) (h): \n"))
    #h =  porc*c
    #
    #print(f"h ={h}")
    #--------------------------------------
    m = 0
    #Calc Q: 
    Q = round(sqrt((2*k*D/h)),2)
    #
    print(f"Q = {Q} {producto}")
    #
    R = -1
    T = 0
    #
    #Calc T:
    T = Q/D
    #si T > L
    if(T > L):
        R = D * L
        print(f"Cuando T > L, R = {round(R,2)} {producto}")
    else:
        #si L > T
        while (R==-1):
            if((L - m*T) > 0 and (L - (m+1)*T) < 0):
                #d
                R = D * (L - m*T)
                print(f" Cuando L > T, R = {round(R,2)} {producto}")
            else:
                m+=1
    #costo total
    C = (c*D) + (k * (D/Q)) + (1/2 * h * Q)
    #salida
    print(f"Costo total {nombreMedida}:")
    print(f"Cost (Q) = {round(C,2)}")
    #------------------------------------------------------------------------------------
#
#calcsHere()
#CALC DE DEMANDA CUANDO SE TIENE PUNTO DE REORDEN R, Q, L   y demas datos basicos de entrada
def calcDemanda():
    R = float(input("Ingrese el valor del punto de reorden (R): \n"))
    Q = float(input("Ingrese la cantidad de productos a pedir (Q): \n"))
    L = float(input("Ingrese el valor del tiempo de entrega (L): \n"))
    c = float(input("Ingrese el valor del costo unitario (c): \n"))
    k = float(input("Ingrese el valor del costo de produccion(k): \n"))
    h = float(input("Ingrese el valor del costo de almacenamiento / inventario (h): \n"))
    #
    D = R/L
    print(f"Demanda: D = {round(D,3)}")
    #
    #costo total
    C = (c*D) + (k * (D/Q)) + (1/2 * h * Q)
    #salida
    print(f"Costo total:")
    print(f"Cost (Q) = {round(C,2)}")
#
def menu():
    #medidas para los calculos - se definen al iniciar antes de procesar todos los datos
    #esta medida se elige solo 1 VEZ, si no se elige una de las 3 opciones disponibles
    #el menu le permite al usuario volver a elegir, si elige una, por esa medida
    #se haran todos los calculos
    print("--------------------------------------------------------------------------------------------------------------------------")
    print(" --ALGORITMO EN PYTHON - CALCULOS DE LOTE ECONOMICO --")
    print(f" Bienvenido! Antes de iniciar por favor elige una opcion")
    print("\n")
    print(f"Dia:1     Semana:2    Año:3  Otro(Calculo demanda por despeje):4 \n")
    opc = int(input("Coloca la opcion de la medida que prefieres para tus calculos aqui aqui: \n"))
    if(opc==1):
        #
        print("Dia")
        calcsLoteEconomico(opc)
        #
    elif(opc==2):
        #
        print("Semana")
        calcsLoteEconomico(opc)
        #
    elif(opc==3):
        #
        print("Año")
        calcsLoteEconomico(opc)
    elif(opc==4):
        #
        print(" Insertar entradas para calcular Demanda: ")
        calcDemanda()
        #
    else:
        print("Uy! esa opcion no es valida, chequea")
        #recursividad - menu opcion else
        opcBack  = int(input("quieres volver a las opciones disponibles? Si(1) No(2): \n"))
        if(opcBack==1):
            menu()
        else:
            print("Cerrando...")
menu()

