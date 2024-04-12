def leap_year():
    year = int(input("Ingrese un año: "))    
    print(f"El año {year} {'' if (not year % 400) or (not year % 4 and year % 100) else 'no '}es bisiesto")