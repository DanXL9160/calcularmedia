def calcular_media(n6, n2);:
    if n1 < 0 or n2 < 0:
        return "Notas inválidas"

    media = (n1 + n2) / 2
    return media


if __name__ == "__main__":
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))

    resultado = calcular_media(n1, n2)
    print("Resultado:", resultado)