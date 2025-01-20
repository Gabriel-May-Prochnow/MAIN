import random

def rolar_dado(tipo_dado, quantidade):
    resultados = []
    for _ in range(quantidade):
        resultados.append(random.randint(1, tipo_dado))
    return resultados

def main():
    print("Simulador de Dados de RPG")
    while True:
        try:
            modo = input("Escolha o modo: 'teste' ou 'dano': ").strip().lower()
            if modo not in ["teste", "dano"]:
                print("Modo inválido. Escolha 'teste' ou 'dano'.")
                continue

            tipo = int(input("Digite o tipo de dado (ex.: 4, 6, 8, 10, 12, 20, 100): d"))
            quantidade = int(input("Quantos dados você quer rolar? "))
            
            if tipo <= 0 or quantidade <= 0:
                print("Por favor, insira valores válidos!")
                continue

            resultados = rolar_dado(tipo, quantidade)

            if modo == "dano":
                print(f"Resultados: {resultados}")
                print(f"Soma total: {sum(resultados)}")
            elif modo == "teste":
                print(f"Resultados: {resultados}")
                print(f"Maior dado: {max(resultados)}")
                
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros.")
        
        continuar = input("Deseja rolar novamente? (s/n): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
