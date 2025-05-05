from math import sqrt
from scipy.stats import norm
#caso de revision periodica - pag 12 - clase 3
def revisionPeriodica():
    invEx = float(input("Existencia en inventario: ")) # existencia en inventario en el momento de la orden
    costJ = float(input("J: ")) # costo de revisar el inventario
    k = float(input("k: "))
    #sugerencia para el tamano del orden
    Ed = float(input("E(D): "))
    h = float(input("h: "))
    #
    Q = sqrt((2*(k+costJ))*(Ed)/h)
    #
    resp = int(input(" con demanda acumulada?(1) o con perdida de ventas por escasez?(2)"))
    if(resp==1):
        #REVISION PERIODICA - CON DEMANDA ACUMULADA:
        #T -> longitud del ciclo T
        #T = float(input("T: "))
        #T = sqrt(2*k/D*h) --> chequeo constante *
        pA = int(input("costo de demanda acumulados: "))
        #T se calcula por...
        #p(Dl+t) >= Q - invEx = T*h / Pa
        prob = T*h / pA # prob = prob de Dl+t
        print(f" valor de prob = {round(prob,2)}")
        #prob
        z = abs(norm.ppf(prob))
        print(f" z = {z}")
        #
        #
        #
        #
        #Rval = (z * zigma) + 
        xVal = (Q - invEx) / (1/z)
        #print("Luego de despejar, tenemos el valor de punto de reorden (R)")
        #print(f"R = {round(Rval,3)}")
        print("...")
    elif(resp==2):
        #REVISION PERIODICA - CON PERDIDA DE VENTAS POR ESCASEZ
        pN = int(input("costo de faltantes no acumulados: "))
        #T se calcula por...
        T = float(input("T: "))
        #p(Dl+t) >= Q - invEx = T*h / T*h + Pn
        prob = T*h / T*h + pN # prob = prob de Dl+t
        #
        #
        #
        #
        print("...")
    else:
        print("Uy! esa opcion no es valida")

if __name__ == '__main__': 
    revisionPeriodica()






