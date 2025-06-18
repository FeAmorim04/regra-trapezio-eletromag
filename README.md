# Regra do Trapézio em Eletromagnetismo

Este repositório contém a implementação em Python da **Regra do Trapézio Composta** aplicada ao cálculo de integrais definidas relacionadas ao campo elétrico. O código foi desenvolvido como parte de um artigo acadêmico na área de Engenharia, abordando a aplicação da integração numérica para determinação de potenciais elétricos.

## 🎯 Objetivo

Calcular numericamente a diferença de potencial elétrico entre dois pontos \( V_{AB} \), com base nas contribuições de cargas distribuídas (linha de carga) e pontuais. O método aplicado foi a **Regra do Trapézio Composta**, adequada para funções contínuas com comportamento regular.

## 🧠 Metodologia

O algoritmo implementa:

- Uma função genérica `regra_trapezio(f, a, b, n)` para integrar funções reais em intervalos arbitrários.
- Três funções físicas representando as componentes do campo elétrico:
  - \( E_x(x, 2, 1) \) — carga pontual
  - \( E_y(-2, y, 1) \) — carga pontual + linha de carga
  - \( E_z(-2, 5, z) \) — carga pontual + linha de carga
- As funções foram definidas separadamente para permitir o cálculo individual das cinco integrais envolvidas no problema.

### Fórmula aplicada

A aproximação da integral é dada por:

\[
\int_a^b f(x)\, dx \approx \frac{h}{2}\left[f(x_0) + 2f(x_1) + \ldots + 2f(x_{n-1}) + f(x_n)\right]
\]

## 📁 Arquivos

- `integracao_numerica.py`: contém todas as funções e cálculos numéricos com saída direta do valor de \( V_B \).

## ▶️ Como Executar

### 1. Pré-requisitos

- Python 3.x
- Biblioteca NumPy

### 2. Executar o código

```bash
python integracao_numerica.py
