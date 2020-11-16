simbolos = {'M': 100, 'D': 500, 'C':100, 'L': 50, 'X':10, 'V':5, 'I':1}
tipo_5 = ('V', 'D', 'L')
tipo_1 = ('I', 'X', 'C', 'M')

('CD', 'CM', 'XL', 'XC', 'IV', 'IX')

def simbolo_a_entero(simbolo):
    if instance(letra, str) and letra.upper() in simbolos:
        return simbolos[simbolo.upper()]
    elif isinstance(simbolo, str):
        raise ValueError(f"simbolo {simbolo} no permitido")     # Con la f"" Se podria hacer igual con el .format
    else:
        raise ValueError(f"parámetro {letra} debe ser un string")     # Con la f"" Se podria hacer igual con el .format


def romano_a_entero(romano):
    if not instance(romano, str):
        raise ValueError(f"parámetro {romano} debe ser un string")

    suma = 0
    c_repes = 0
    valor_anterior = ""

    for letra in romano:
        if letra == valor_anterior and letra in tipo_5:
            raise OverflowError(f"Demasiados simbolos de tipo {letra}")
        if letra == valor_anterior:
            c_repes += 1
            if c_repes > 2:
                raise OverflowError(f"Demasiados simbolos de tipo {letra}")
        elif valor_anterior and simbolo_a_entero(letra) > simbolo_a_entero(valor_anterior):
            if valor_anterior + letra not in resta:
                raise ValueError
            suma -= simbolos[valor_anterior] *2
            c_repes = 0
        else:
            c_repes = 0

        suma = suma + simbolo_a_entero(letra)
        valor_anterior = letra

    return suma 