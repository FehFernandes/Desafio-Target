import json

# Carregar os dados do arquivo JSON
with open('C:/Users/Felipe/OneDrive/Ambiente de Trabalho/Desafio Target/dados.json', 'r') as file:
    dados = json.load(file)

# Filtra os dias com faturamento maior que zero
faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Calcular o menor e o maior valor de faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Calcular a média mensal de faturamento
media_mensal = sum(faturamento) / len(faturamento)

# Conta o número de dias com faturamento superior à média mensal
dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

# Exibir os resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")