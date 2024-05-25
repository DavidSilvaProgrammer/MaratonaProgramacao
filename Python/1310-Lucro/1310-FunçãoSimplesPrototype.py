# Função para calcular o máximo de dinheiro que George pode ganhar
def max_ganho_circo(N, custoPorDia, receitas):
    max_ganho = 0
    for receita in receitas:
        lucro_diario = receita - custoPorDia
        if lucro_diario > 0:
            max_ganho += lucro_diario
    return max_ganho

# Exemplo de entrada
N = 6
custoPorDia = 20
receitas = [18, 35, 6, 80, 15, 21]

# Calcula e imprime o máximo de dinheiro que George pode ganhar
print(max_ganho_circo(N, custoPorDia, receitas))
