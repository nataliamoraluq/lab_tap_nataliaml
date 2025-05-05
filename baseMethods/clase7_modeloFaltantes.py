#
from scipy.stats import norm
from math import sqrt
#
# LOTE ECONOMICO CON  FALTANTES ACUMULADOS O NO ACUMULADOS, MIU Y ZIGMA
def modeloProbabilistico():
    miu = int(input("miu: "))
    zigma = int(input("zigma: "))
    L = int(input("L: "))
    #
    #
    n = int(input("n - cant.: "))
    h = int(input("costo de almacenamiento/mantenimiento: "))
    k = int(input("costo de pedido por lote: "))
    #

    resp = int(input(" Usaremos el costo de faltantes acumulados(1) o no acumulados?(2) "))
    #
    Esp = n * miu
    print(f"Esperanza: {Esp}")    
    #int(input("Esperanza: "))
    Qval = sqrt((2*k*Esp)/h)
    print(f" Q = {round(Qval,2)}")
    #
    if(resp==1):
        #
        pSub = int(input("costo de faltantes acumulados: "))

        # NORMALIZACION
        prob = (h * Qval) / (pSub * Esp)
        print(f" valor de prob = {round(prob,2)}")
        #prob
        z = abs(norm.ppf(prob))
        print(f" z = {z}")
        Rval = (z * zigma) + miu
        print("Luego de despejar, tenemos el valor de punto de reorden (R)")
        print(f"R = {round(Rval,3)}")
    else:
        #print(f"Aqui va para la vers de faltantes NO acumulados")
        #
        pSub = int(input("costo de faltantes no acumulados: "))
        # NORMALIZACION
        prob = (h * Qval) / (h * Qval + (pSub * Esp))
        print(f" valor de prob = {round(prob,2)}")
        #
        #
        #prob
        z = abs(norm.ppf(prob)) #valor de z - Dl para despeje
        print(f" z = {z}")
        Rval = (z * zigma) + miu
        print("Luego de despejar, tenemos el valor de punto de reorden (R)")
        print(f"R = {round(Rval,3)}")

modeloProbabilistico()
""" 
#OJITO self quote: esto por ahora lo descartamos / no lo profundizamos
# E(Dl) cuando los tiempos son distintos y las demandas son independientes
def probCaso2():
    #??? not quite clear, pag 6
    #espD = L * Esp 
    #Dl = L * D
    print("Aqui van cuando E(Dl) cuando los tiempos son distintos y las demandas son independientes")

def colchon():
    #Es = R - E(Dl)
    print("met de colchon aqui")
"""