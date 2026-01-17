
# 🥩 Calculadora de Churrasco

![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUÍDO&color=ORANGE&style=for-the-badge) ![Badge Python](http://img.shields.io/static/v1?label=LINGUAGEM&message=PYTHON&color=blue&style=for-the-badge)

## 📝 Descrição

Este projeto é uma ferramenta desenvolvida em **Python 3** para auxiliar no planejamento de churrascos. O programa calcula automaticamente a quantidade necessária de comida e bebida baseada no perfil dos convidados (Homens, Mulheres e Crianças) e, além disso, gera uma estimativa financeira do custo total e do valor por pessoa.

O foco do projeto foi a aplicação de **Modularização (Funções)** e **Lógica Matemática** aplicada a problemas reais.

## 🚀 Funcionalidades

- **👥 Input Personalizado:** Entrada de dados separada por demografia (Homens, Mulheres, Crianças).
- **🍖 Cálculo de Insumos:**
  - Carne (com conversão automática de gramas para Kg).
  - Cerveja (para adultos).
  - Refrigerante (para crianças).
- **💰 Módulo Financeiro:**
  - Cálculo do custo total baseado em uma tabela de preços configurável.
  - Divisão automática do custo ("racha") entre os adultos pagantes.
- **🛡️ Tratamento de Erros:** Uso de Recursividade para validar entradas numéricas inválidas.
- **🔄 Loop de Execução:** Permite realizar múltiplos cálculos sem fechar o programa.

## 💻 Tecnologias e Conceitos

- **Python 3**
- **Funções com Retorno (`return`):** Para passar dados processados de um módulo para outro.
- **Dicionários (`dict`):** Para armazenar a tabela de preços.
- **Fluxo de Dados:** Armazenamento de resultados em variáveis intermediárias para uso em funções posteriores.

## 📂 Como Executar

### Pré-requisitos
Você precisa ter o **Python 3.x** instalado.

### Passo a passo

1. Clone o repositório:
```bash
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPO.git](https://github.com/SEU_USUARIO/NOME_DO_REPO.git)

```

2. Execute o arquivo:

```bash
python churrasco.py

```

3. Siga as instruções no terminal para inserir o número de convidados.

## 🧠 Destaques de Lógica

A modularização permite que o cálculo financeiro receba dados prontos de outras funções, mantendo o código limpo e organizado:

```python
# O código calcula primeiro as quantidades físicas
qtd_carne = calcular_carne(h, m, c)
qtd_bebidas = calcular_churrasco_bebidas(h, m)

# Depois, passa esses valores para o módulo financeiro
calcular_custos(qtd_carne, qtd_bebidas, qtd_refri, h, m)

```

---
### 🔄 A Evolução do Projeto

O projeto passou por duas grandes fases de desenvolvimento:

1.  **Versão 1.0 (CLI):** Focada na lógica matemática e execução via terminal.
2.  **Versão 2.0 (GUI - Atual):** Implementação de uma **Interface Gráfica** moderna usando a biblioteca **Flet**. Agora o usuário interage com botões e campos de texto, não mais com o console preto.

## 🚀 Funcionalidades (v2.0)

- **🖥️ Interface Visual:** Janela interativa, centralizada e responsiva.
- **📝 Formatação Rica:** Uso de **Markdown** para exibir os resultados com negrito e organização visual.
- **🛡️ Tratamento de Erros Visual:** Mensagens de alerta aparecem na própria tela se o usuário inserir dados inválidos (não quebra o app).
- **💰 Cálculo Automático:**
  - Carnes (Kg), Cerveja (Latas) e Refrigerante (Latas).
  - Rateio de custos entre os adultos pagantes.

## 💻 Tecnologias Utilizadas

- **Python 3.x**
- **Flet:** Framework para construção de interfaces gráficas (Frontend em Python).
- **Lógica de Markdown:** Para estilização de texto dinâmica.

## 📸 Preview

*<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/514e4d78-984e-4299-b82f-27eb39a7ab49" />
*

## 🔧 Como Executar o Projeto

Como esta versão utiliza interface gráfica, é necessário instalar uma biblioteca extra.

### Pré-requisitos

1. Tenha o Python instalado.
2. Instale o **Flet** via terminal:
```bash
pip install flet

```

### Rodando o App

Execute o arquivo principal:

```bash
python nome_do_arquivo.py

```

Uma janela da aplicação se abrirá automaticamente.

## 🧠 Aprendizados

A migração do Terminal para o Visual exigiu uma mudança de mentalidade:

* **De:** Fluxo linear (`input` -> `processamento` -> `print`).
* **Para:** Orientação a Eventos (O app desenha a tela e aguarda o `on_click` do botão para agir).

---
