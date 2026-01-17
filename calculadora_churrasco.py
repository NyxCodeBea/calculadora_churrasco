# --- 1. Configurações e Dados ---

precos = {
    "carne": 35.90, # Reais por Kg
    "cerveja": 4.50, # Reais por Lata
    "refrigerante": 3.00 # Reais por Lata
}

def calcular_churrasco_recebimento(): # Receber dados do usuário
    print("\nCalculadora de Churrasco")
    try:
        homens = int(input("Número de homens: "))
        mulheres = int(input("Número de mulheres: "))
        criancas = int(input("Número de crianças: "))
        print(f"\nParticipantes: {homens} homens, {mulheres} mulheres, {criancas} crianças")
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros.")
        return calcular_churrasco_recebimento()
    return homens, mulheres, criancas

def calcular_carne(homens, mulheres, criancas): # Calcular a quantidade de carne necessária
        carne_homens = homens * 400
        carne_mulheres = mulheres * 300
        carne_criancas = criancas * 200
        print(f"\nTotal de carne: Homens: {carne_homens}g, Mulheres: {carne_mulheres}g, Crianças: {carne_criancas}g")
        total_carne = ((carne_homens + carne_mulheres + carne_criancas) / 1000) # Somar todas as quantidades de carne em kg
        print(f"Total de carne necessária: {total_carne} kg")
        return total_carne

def calcular_churrasco_bebidas(homens, mulheres): # Refletir consumo de bebidas alcoólicas
    bebidas_homens = homens * 3
    bebidas_mulheres = mulheres * 2
    print(f"\nTotal de bebidas: Homens: {bebidas_homens} latas, Mulheres: {bebidas_mulheres} latas")
    total_bebidas = bebidas_homens + bebidas_mulheres # Somar todas as quantidades de bebidas alcoólicas
    print(f"Total de bebidas alcoólicas necessárias: {total_bebidas} latas")
    return total_bebidas

def calcular_churrasco_refri(criancas): # Refletir consumo de refrigerantes
    refri_criancas = criancas * 2
    print(f"\nTotal de refrigerantes para crianças: {refri_criancas} latas")
    return refri_criancas

def calcular_custos(total_carne, total_bebidas, refri_criancas, homens, mulheres): # Calcular custos totais
    custo_carne = total_carne * precos["carne"]
    custo_cerveja = total_bebidas * precos["cerveja"]
    custo_refrigerante = refri_criancas * precos["refrigerante"]
    total = custo_carne + custo_cerveja + custo_refrigerante
    total_adultos = homens + mulheres
    if total_adultos > 0:
        total_divido = total / total_adultos
    else:
        total_divido = 0
    print(f"\n--- CUSTOS ---")
    print(f"O custo total do churrasco será: R$ {total:.2f}")
    print(f"O custo por adulto será: R$ {total_divido:.2f}")
    return total

# --- 2. Execução do Programa ---
while True:
    resposta = input("\nDeseja calcular a quantidade de carne e bebidas para o seu churrasco? Sim (S) ou  Não (N): ").upper()
    if resposta == 'N':
        print("Encerrando o programa.....")
        break
    elif resposta == 'S':
        print("Iniciando o cálculo do churrasco...")
        h, m, c = calcular_churrasco_recebimento() # Chamar função para receber dados do usuário
        qtd_carne = calcular_carne(h, m, c) # Chamar função para calcular carne
        qtd_bebidas = calcular_churrasco_bebidas(h, m) # Chamar função para calcular bebidas alcoólicas
        qtd_refri = calcular_churrasco_refri(c) # Chamar função para calcular refrigerantes
        calcular_custos(qtd_carne, qtd_bebidas, qtd_refri, h, m) # Chamar função para calcular custos
    else:
        print("Resposta inválida. Por favor, digite 'S' para sim ou 'N' para não.")