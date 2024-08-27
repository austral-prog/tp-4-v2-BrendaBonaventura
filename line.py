def line():
    coefA=float(input("Ingrese el coeficiente A: "))
    coefB=float(input("Ingrese el coeficiente B: "))
    coefX1=float(input("Ingrese el coeficiente X1: "))
    coefX2=float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {coefA}")
    print(f"El coeficiente B de su ecuación de la recta es: {coefB}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coefX1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coefX2}")
    print("\nPara la siguiente ecuación:")
    print(f"\tY={coefA}X + {coefB}")
    print("\nDados los siguientes puntos:")
    cord1=coefA*coefX1+coefB
    print(f"\tP1 ({coefX1}, {cord1})")
    cord2=coefA*coefX2+coefB
    print(f"\tP2 ({coefX2}, {cord2})")
    distancia=((coefX2-coefX1)**2+(cord2-cord1)**2)**(1/2)
    print(f"\nLa distancia entre ellos es: {distancia}")
