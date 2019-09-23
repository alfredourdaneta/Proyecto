def valInt(*args):
    if len(args) == 1:
        if type(args[0]) != int:
            isInt = False
        else:
            isInt = True
    elif len(args) == 2:
        if type(args[0]) != int:
            raise TypeError("El primer argumento debe ser un numero entero")
        elif type(args[1]) != tuple and type(args[1]) != list:
            raise TypeError("El segundo argumento debe ser de tipo tupla o lista ")
        elif len(args[1]) != 2:
            raise ValueError("El tamano de la tupla o lista es de dos terminos")
        elif  args[1][0] > args[1][1]:
            raise ValueError("El primer termino no puede ser mayor que el segundo")
        elif type(args[1]) == list:
            if args[0] in range(args[1][0],args[1][1]+1):
                isInt = True
            else:
                isInt = False
        elif type(args[1]) == tuple:
            if args[0] in range(args[1][0] + 1,args[1][1]):
                isInt = True
            else:
                isInt = False
    return isInt

def valFloat(*args):
    if len(args) == 1:
        if type(args[0]) != float:
            isInt = False
        else:
            isInt = True
    elif len(args) == 2:
        if type(args[0]) != float:
            raise TypeError("El primer argumeto debe ser un numero Irracional")
        elif type(args[1]) != tuple and type(args[1]) != list:
            raise TypeError("El segundo argumento debe ser de tipo tupla o lista ")
        elif len(args[1]) != 2:
            raise ValueError("El tamano de la tupla o lista debe ser de dos terminos")
        elif  args[1][0] > args[1][1]:
            raise ValueError("El primer termino no puede ser mayor que el segundo")
        elif type(args[1]) == list:
            if args[0] in range(float(args[1][0]),float(args[1][1]+1)):
                isInt = True
            else:
                isInt = False
        elif type(args[1]) == tuple:
            if args[0] in range(args[1][0] + 1,args[1][1]):
                isInt = True
            else:
                isInt = False
    return isInt


def valComplex(*args):
    if len(args) == 1:
        if type(args[0]) != complex:
            isInt = False
        else:
            isInt = True
    elif len(args) == 2:
        if type(args[0]) != complex or type(args[1]) != tuple and type(args[1]) != list:
            raise TypeError("El primer argumeto debe ser un numero complejo y el segundo tiene que ser de tipo lista o tupla")
        elif len(args[1]) != 2:
            raise ValueError("El tamano de la tupla o lista es de dos terminos")
        elif type(args[1]) == list:
            if args[0] in range(args[1][0],args[1][1]+1):
                isInt = True
            else:
                isInt = False
        elif type(args[1]) == tuple:
            if args[0] in range(args[1][0] + 1,args[1][1]):
                isInt = True
            else:
                isInt = False
    return isInt
