#
#
#tipo de demandas - comparacion
D1 = [800,830, 825, 795, 810, 815, 810, 820, 790, 820, 805, 815, 800, 810, 805]
D2 = [800, 620, 50, 990, 980, 850, 985, 990, 890, 60, 100, 820, 950, 990, 980]

#metodo para determinar tipo de demanda - si es probabilistica o deterministica
def detTipoDemanda(D, p):
    n = len(D)
    #
    dBar = sum(D) / n
    des = ((sum([x ** 2 for x in D])) - n*(pow(dBar,2))) / n - 1
    s = pow(des,2)/(pow(dBar,2))
    if(s<p):
        print(f"la demanda es deterministica")
    else:
        print(f"la demanda es probabilistica")
    print("\n")

def menu():
    p = float(input("Ingrese el valor de p: \n"))
    print(f"Demanda - vector 1:")
    detTipoDemanda(D1, p)
    print(f"Demanda - vector 2:")
    detTipoDemanda(D2, p)
menu()

