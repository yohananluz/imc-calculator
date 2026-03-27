def calcular_imc(peso, altura):
    """Calcula o IMC e retorna o valor e a classificação."""
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        categoria = "Peso normal"
    elif 25 <= imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
        
    return imc, categoria

def main():
    print("--- Calculadora de IMC Profissional ---")
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (m): "))
        
        if peso <= 0 or altura <= 0:
            print("Erro: Peso e altura devem ser maiores que zero.")
            return

        resultado, classificacao = calcular_imc(peso, altura)
        
        print(f"\nSeu IMC é: {resultado:.2f}")
        print(f"Classificação: {classificacao}")
        
    except ValueError:
        print("Erro: Por favor, insira apenas números usando ponto para decimais.")

if __name__ == "__main__":
    main()