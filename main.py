def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).
    :param peso: Peso en kilogramos (float).
    :param altura: Altura en metros (float).
    :return: El IMC calculado (float) o mensaje de error (str).
    """
    if altura <= 0 or altura > 3:
        return "La altura debe estar en metros (ejemplo: 1.80)."
    if peso <= 0:
        return "El peso debe ser mayor a 0."

    imc = peso / (altura ** 2)
    return imc


def clasificar_imc(imc):
    """
    Clasifica el IMC según las categorías de la OMS.
    :param imc: IMC calculado (float).
    :return: Categoría del IMC (str).
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"


# Solicitar datos al usuario
try:
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros (ejemplo: 1.80): "))

    # Calcular y clasificar el IMC
    imc = calcular_imc(peso, altura)
    if isinstance(imc, str):  # Si se devuelve un mensaje de error
        print(imc)
    else:
        print(f"Tu IMC es: {imc:.2f}")
        print(f"Clasificación: {clasificar_imc(imc)}")
except ValueError:
    print("Por favor, ingresa valores numéricos válidos.")
