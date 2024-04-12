from math import sqrt

def line():
    coef = {
        "A": 0,
        "B": 0,
        "X1": 0,
        "X2": 0
    }

    for key, value in coef.items():
       coef[key] = float(input(f"Ingrese el coeficiente {key}: "))

    for key, value in coef.items():
        print(f"El coeficiente {key} de su ecuación de la recta es: {value}")
    
    print(f"\nPara la siguiente ecuación:\n\tY = " + str(coef["A"]) +"X + " + str(coef["B"]) + "\n")
    
    Ypts = [
        coef['A'] * coef["X1"] + coef["B"],
        coef['A'] * coef["X2"] + coef["B"]
    ]
    
    print(f"Dados los siguientes puntos:\n\tP1 (" + str(coef["X1"]) + ", " + str(Ypts[0]) + ")\n\tP2 (" + str(coef['X2']) +", " + str(Ypts[1]) + ")")
    print(f"\nLa distancia entre ellos es: {sqrt((coef['X1'] - coef['X2'])**2 + (Ypts[0] - Ypts[1])**2)}")
