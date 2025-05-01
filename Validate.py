def validate_number(mensaje_error, minimo, maximo, reintentos) -> int:
    """
    Validacion para pedir un numero por consola y retornar ese numero o none si no cumple con las validaciones

    Args:
        mensaje (str): Mensaje que se va a imprimir antes de pedirle al usuario el dato por consola
        mensaje_error (str): Mensaje de error en el caso de que el dato ingresado sea invalido.
        minimo (int): Valor minimo admitido
        maximo (int): Valor maximo admitido
        reintentos (int): Cantidad de veces que se volverá a pedir el dato en caso de error.

    Returns:
        int|None: Numero
    """
    numero = int(input("Ingrese un numero: "))
    bandera_reintentos = 1

    while numero < minimo or numero > maximo and bandera_reintentos < reintentos:
        bandera_reintentos += 1
        print(mensaje_error) 
        numero = int(input("Ingrese un numero: "))

    if bandera_reintentos >= reintentos:
        numero = None

    return numero
    
def validate_length(mensaje_error, longitud: int) -> None:
    palabra = input("Ingrese una palabra: ")

    while (len(palabra)) > longitud:
        print(mensaje_error)
        palabra = input("Ingrese una palabra: ")

    return palabra