import matematica

def main():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")

        if operacion == '+':
            resultado = matematica.suma(num1, num2)
        elif operacion == '-':
            resultado = matematica.resta(num1, num2)
        elif operacion == '*':
            resultado = matematica.multiplicacion(num1, num2)
        elif operacion == '/':
            resultado = matematica.division(num1, num2)
        else:
            print("Operación no válida")
            return

        print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
    except ValueError:
        print("Error: Ingrese solo números válidos.")

if __name__ == "__main__":
    main()
