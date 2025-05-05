from math import *
def calcsHere():
    R = -1
    T = 0
    #
    print(f" 1 año - 52 semanas")
    print(f"--------------------------------------------------------------------------------------------------------------------------")
    producto = (input("Que tipo de producto se encuentra en produccion? \n"))
    d = float(input("Ingrese el valor de la demanda semanal (D): \n"))
    D = d/52
    c = float(input("Ingrese el valor del costo por producto (en $) (c): \n"))
    lWeekly = float(input("Ingrese el valor del tiempo de entrega semanal (L): \n"))
    L = lWeekly / 52
    k = float(input("Ingrese el valor del costo de produccion (en $) (k): \n"))
    porc = float(input("Para calcular el costo anual de (h), ingrese el porcentaje del valor del inventario promedio (Ej: 0.20) (h): \n"))
   
    h =  porc*c
    m =0
    #print(f"h ={h}")
    Q = round(sqrt((2*k*D/h)),2)
    #
    print(f"Q = {Q} {producto}")

    T = Q/D
    if(T > L):
        R = d * L
        print(f"Cuando T > L, R = {round(R,2)} {producto}")
    else:
        while (R==-1):
            if((L - m*T) > 0 and (L - (m+1)*T) < 0):
                #d
                R = D * (L - m*T)
                print(f" Cuando L > T, R = {round(R,2)} {producto}")
            else:
                m+=1
    C = (c*D) + (k * (D/Q)) + (1/2 * h * Q)
    print(f"Costo total anual  Cost (Q)= {round(C,2)}")
#
calcsHere()
# vers1 : 
"""
ver clase8_revisionPeriodica, ahi si esta mas desarrollado
def revisionPeriodica(k, D, h):
    T = sqrt((2*k/D*h),2)
    print(f"{round(T,2)}")
    #
    #calcR(Q, L,d, R, T, producto)
    #revisionPeriodica(k, d, h)
    #print(f"R = ")
"""

"""
from math import *

#which one is? XDDD
def modeloSimple():
    R = -1
    T = 0
    #
    print(f" 1 año - 52 semanas")
    print(f"--------------------------------------------------------------------------------------------------------------------------")
    producto = (input("Que tipo de producto se encuentra en produccion? \n"))
    d = float(input("Ingrese el valor de la demanda semanal (D) - llevada a años: \n"))
    p = float(input("Ingrese el valor del costo unitario de penalizacion por faltante anual (p): \n"))
    D = d
    c = float(input("Ingrese el valor del costo por producto (en $) (c): \n"))
    lWeekly = float(input("Ingrese el valor del tiempo de entrega semanal (L): \n"))
    L = lWeekly
    k = float(input("Ingrese el valor del costo de produccion (en $) (k): \n"))
    porc = float(input("Para calcular el costo anual de (h), ingrese el porcentaje del valor del inventario promedio (Ej: 0.20) (h): \n"))
   
    h =  porc*c
    m =0
    #print(f"h ={h}")
    Q = round(sqrt((2*k*D/h)),2)
    #
    print(f"Q = {Q} {producto}")

    e = sqrt((2*k*D)/((h+p)*p))
    print(f"{round(e,2)}")

    T = Q/D
    if(T > L):
        R = D * L - e
        print(f"Cuando T > L, R = {round(R,2)} {producto}")
    else:
        while (R==-1):
            if((L - m*T) > 0 and (L - (m+1)*T) < 0):
                #d
                R = D * (L - m*T)
                print(f" Cuando L > T, R = {round(R,2)} {producto}")
            else:
                m+=1
    #C = (c*D) + (k * (D/Q)) + (1/2 * h * Q)
    C = (c*D) + ((k *D)/Q) + (h * ((Q-e)**2) / 2*Q) + (p*e/2*Q)
    print(f"Costo total anual  Cost (Q)= {round(C,2)}")
#
modeloSimple()
"""
