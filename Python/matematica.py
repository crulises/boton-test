def suma(a, b):
    """Suma dos valores"""
    return a + b

def resta(a, b):
    """Resta dos valores"""
    return a - b

def multiplicacion(a, b):
    """Multiplica dos valores"""
    return a * b

def division(a, b):
    """Divide dos valores"""
    if b == 0:
        return "Error: División por cero no permitida"
    return a / b