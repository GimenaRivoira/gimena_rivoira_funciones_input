from Validate import *

def get_int(mensaje:str, mensaje_error:str, minimo: int, maximo:int, reintentos:int) -> int|None:
    """
    Funcion para pedir un numero por consola y retornar ese numero o none si no cumple con las validaciones

    Args:
        mensaje (str): Mensaje que se va a imprimir antes de pedirle al usuario el dato por consola
        mensaje_error (str): Mensaje de error en el caso de que el dato ingresado sea invalido.
        minimo (int): Valor minimo admitido
        maximo (int): Valor maximo admitido
        reintentos (int): Cantidad de veces que se volverá a pedir el dato en caso de error.

    Returns:
        int|None: Numero
    """
    print(mensaje)
    numero = validate_number(mensaje_error, minimo, maximo, reintentos)

    return numero

#print(get_int("BIENVENIDO/A", "INTENTE NUEVAMENTE", 1,10,2))

def get_float(mensaje:str, mensaje_error:str, minimo: int, maximo:int, reintentos:int) -> int|None:
    """
    Funcion para pedir un numero por conla y retornar ese numero o none si no cumple con las validaciones

    Args:
        mensaje (str): Mensaje que se va a imprimir antes de pedirle al usuario el dato por consola
        mensaje_error (str): Mensaje de error en el caso de que el dato ingresado sea invalido.
        minimo (int): Valor minimo admitido
        maximo (int): Valor maximo admitido
        reintentos (int): Cantidad de veces que se volverá a pedir el dato en caso de error.

    Returns:
        int|None: Numero
    """
    print(mensaje)
    numero = validate_number(mensaje_error, minimo, maximo, reintentos)

    return numero

#print(get_int("BIENVENIDO/A", "INTENTE NUEVAMENTE", 1.10,10.10,2))

def get_string(mensaje:str, mensaje_error: str, longitud: int) -> None:
    print(mensaje)
    palabra = validate_length(mensaje_error, longitud)
    print(f"La longitud se su palabra es {len(palabra)}")

get_string("BIENVENIDO/A", "INTENTE NUEVAMENTE", 2)

