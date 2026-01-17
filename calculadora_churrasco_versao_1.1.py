# --- 1. Configurações e Dados ---

import flet as ft

# Preços dos itens do churrasco
precos = {
    "carne": 35.90, # Reais por Kg
    "cerveja": 4.50, # Reais por Lata
    "refrigerante": 3.00 # Reais por Lata
}

# --- 2. Função Principal ---

def main(page: ft.Page):
    # 1. Configurações da Janela
    page.title = "Calculadora de Churrasco"
    # Centralizando o conteúdo da página
    page.vertical_alignment = "center" 
    page.horizontal_alignment = "center"
    # Adicionei rolagem caso a tela seja pequena
    page.scroll = "adaptive"

    # 2. Elementos da Interface
    titulo = ft.Text("Calculadora de Churrasco", size=30, weight=ft.FontWeight.BOLD) # Título

    # Inputs para número de participantes
    homens_input = ft.TextField(label="Número de Homens", width=210, keyboard_type=ft.KeyboardType.NUMBER)
    mulheres_input = ft.TextField(label="Número de Mulheres", width=210, keyboard_type=ft.KeyboardType.NUMBER)
    criancas_input = ft.TextField(label="Número de Crianças", width=210, keyboard_type=ft.KeyboardType.NUMBER)

    # Área para exibir o resultado
    resultado_text = ft.Markdown("", extension_set="gitHubWeb")

    def calcular_churrasco(e):
        try: 
            # Tratando inputs vazios
            if not homens_input.value: homens_input.value = "0"
            if not mulheres_input.value: mulheres_input.value = "0"
            if not criancas_input.value: criancas_input.value = "0"

            #  Pegando valores dos inputs
            homens = int(homens_input.value)
            mulheres = int(mulheres_input.value)
            criancas = int(criancas_input.value)
        except ValueError: 
            # Tratamento de erro
            resultado_text.value = "Por favor, insira apenas números."
            page.update()
            return
        
    # 3. Cálculos
        # Cálculo das quantidades necessárias
        carne_total = (homens * 0.4) + (mulheres * 0.3) + (criancas * 0.2) # Total de carnes já em Kg
        cerveja_total = (homens * 3) + (mulheres * 2) # Latas bebidas alcoólicas
        refrigerante_total = (criancas * 2) # Latas de refrigerante

        # Cálculo dos custos
        custo_carne = carne_total * precos["carne"] # Custo da carne
        custo_cerveja = cerveja_total * precos["cerveja"] # Custo da cerveja
        custo_refrigerante = refrigerante_total * precos["refrigerante"] # Custo do refrigerante
        custo_total = custo_carne + custo_cerveja + custo_refrigerante # Custo total

        # Total de participantes
        total_participantes = homens + mulheres + criancas

        # Custo por adulto
        total_adultos = homens + mulheres
        if total_adultos > 0:
            total_divido = custo_total / total_adultos
        else:
            total_divido = 0

        # Exibindo resultados
        resultado_text.value = ( 
            f"\n**--- PARTICIPANTES ---**\n\n" 
            f"Participantes: {homens_input.value} homens, {mulheres_input.value} mulheres, {criancas_input.value} crianças\n\n"
            f"Total de participantes: {total_participantes}\n\n"
            f"\n**--- QUANTIDADES NECESSÁRIAS ---**\n\n"
            f"Total de carne necessária: {carne_total:.2f} Kg\n\n" 
            f"Total de cerveja necessária: {cerveja_total} Latas\n\n"
            f"Total de refrigerante necessário: {refrigerante_total} Latas\n\n"
            f"\n**--- CUSTOS ---**\n\n"
            f"💰 O custo total do churrasco será: R$ {custo_total:.2f}\n\n"
            f"👤 O custo por adulto será: R$ {total_divido:.2f}"
        ) 

        # Atualizando a página
        page.update()

    # Botão de Calcular    
    # Correção: Criar o botão diretamente sem atribuir a um container desnecessariamente
    botao = ft.ElevatedButton(
        content=ft.Text("Calcular Churrasco"), 
        color="white",
        bgcolor="green",
        on_click=calcular_churrasco
    )

    # Correção: Container para o botão
    calcular_button = ft.Container(
        content=botao,
        margin=ft.margin.only(top=20, bottom=20)
    )

    calcular_button.content = botao  # Corrigido para referenciar o botão corretamente
    # 4. Adicionando Elementos à Página
    page.add(   
        titulo,
        ft.Row([homens_input, mulheres_input, criancas_input], alignment="center"),
        calcular_button,
        ft.Divider(),
        ft.Container(
            content=resultado_text,
            padding=20,
            bgcolor="grey", # "grey" simples
            border_radius=10
        )
    )
    
# --- 3. Execução do Programa ---

# Iniciando a aplicação Flet
ft.app(target=main)