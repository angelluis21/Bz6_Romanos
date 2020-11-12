simbolos = {'M': 100, 'D': 500, 'C':100, 'L': 50, 'X':10, 'V':5, 'I':1}

def romano_a_entero(romano):
    if instance(romano, str) and romano.upper() in simbolos:
        return simbolos[romano.upper()]
    elif isinstance(romano, str):
        raise ValueError(f"simbolo {romano} no permitido")     # Con la f"" Se podria hacer igual con el .format
    else:
        raise ValueError(f"parámetro {romano} debe ser un string")     # Con la f"" Se podria hacer igual con el .format
