from math import sqrt, exp
from scipy.stats import norm
#caso de revision periodica - pag 12 - clase 3
#servidor: por ej, caja, impresora
def teoriaColas():
    #DATOS DE ENTRADA
    landa = float(input("Tasa de llegada landa: ")) # Tasa de llegada  --- cliente/hora-min-seg
    miu = float(input("Tasa de servicio miu: ")) # Tasa de servicio --- cliente/hora-min-seg
    pRho = landa/miu #Factor de utilizacion - Rho - % de tiempo q el sist esta ocupado
    #
    t = float(input(" Tiempo de espera t:")) #par aprobs exponenciales?
    n = float(input(" nro de clientes existentes (n para probs?):")) #(n para probs?)
    #
    # CALCS INICIALES
    
    L= landa/(miu-landa) # L= Cantidad promedio de clientes en el sistema (incluyendo los clientes que se estan atendiendo en el momento)
    Lq= (landa**2)/(miu*(miu-landa)) # Lq= Cantidad promedio de clientes exclusivamente/unicamente en la cola
    #Ls = float(input("Cant de clientes en el sistema (Ls): "))
    W= 1/(miu-landa) # W= Tiempo total del cliente en el sistema hasta ser atendido
    Wq= pRho/(miu-landa) # Wq= Tiempo del cliente cuando esta en la cola
    # 
    #PROBABILIDADES --  DESPEJE O CALC POR ELECCION?

    # P(W > t) = e ^ -miu * (1-pRho) * t
    ProbW = exp((-1 * miu) * (1-pRho) * t)
    # P(Wq > t)
    ProbWq = pRho * exp((-1 * miu) * (1-pRho) * t)

    #Para calcular las probabilidades: 
    Po = (1-pRho) #P0/Po= Promedio cuando no hay clientes en el sistema/para calcular tiempo ocioso
    #Po = (1-pRho)

    Pn = (1-pRho)* (pRho**n) #Pn= Nro. promedio de clientes en el sistema (Promedio de n): "
    #Por ejemplo, si es P1 (Probabilidad de que haya 1 cliente promedio en el sistema):
    #P1 = (1-pRho)* (pRho**1)

    # Para las probs de L usamos Pn
    #ProbL = Probabilidad de que P(L> n)
    #para ProbL se debe primero calcular P0, luego P1, y asi cada Pn por el valor de n, luego:
    #ProbL = 1 - (P0+P1+...+Pn)


    #ProbW = Probabilidad de que (W > t) 
    #P(W > t)  = e ^ -miu * (1-pRho) * t
    ProbW = exp((-1 * miu) * (1-pRho) * t) # 

    #ProbWq = Probabilidad de que (Wq > t) 
    #P(Wq > t) = pRho * e ^ (-miu * (1-pRho) * t)
    ProbWq = pRho * exp((-1 * miu) * (1-pRho) * t) 
    

    # P0, Pn, (W > t), (Wq > t)
    #how to y pendientes:
    # ver apuntes hojitas sueltas; tienen las meras forms en limpio con notas
    # chequear las forms y tratar de usar las ecuacs. de landa y miu / y/o prho
    # invg de nuevo y probar tema de los exponenciales / nro de euler / exponentes elevados en python
    # ver en el enunciado cm tal cuales son y cuales no las probs a calc
    # analizar si las salidas iran en la ventana por tbox c/u o en un txarea grande (tmb seria mejor la vd); en 
    # mssgebox NO pq eso es momentaneo y necesitamos q las salidas/ calcs no se cierren con la mera ventana emergente
    #es def mejor en una ventana donde sta todo cm tal
    #por ult, probar y corregir cualquier posible error + preguntar QUE GRAFICA usar aqui


"""resp = int(input(" W > t (1) o Wq > t(2)"))

    if(resp==1):
        #W > t
        #eNmb = ??
        #prob1 = eNmb ** (-miu*(1-pRho)*t)
        #z = abs(norm.ppf(prob))
        #print(f" z = {z}")
        #
        #
        #
        ##print("Luego de despejar, tenemos el valor de punto de reorden (R)")
        #print(f"R = {round(Rval,3)}")
        print("...")
    elif(resp==2):
        #Wq > t
        #eNmb = ??
        prob2 = pRho*eNmb ** (-miu*(1-pRho)*t)
        #z = abs(norm.ppf(prob))
        #print(f" z = {z}")
        #
        #
        #
        ##print("Luego de despejar, tenemos el valor de punto de reorden (R)")
        #print(f"R = {round(Rval,3)}")
        print("...")
    else:
        print("Uy! esa opcion no es valida")"""
