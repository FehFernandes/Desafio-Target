# Valores de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcular o valor total mensal
total_mensal = sum(faturamento_estados.values())

# Calcular o percentual de representação de cada estado
percentuais = {estado: (valor / total_mensal) * 100 for estado, valor in faturamento_estados.items()}

# Exibir os resultados com duas casas decimais
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")