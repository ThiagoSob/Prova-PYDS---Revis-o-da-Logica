# Você foi contratado para desenvolver um programa que auxiliará no processo de compra de produtos em uma loja. 
# O programa deve permitir que o usuário insira o nome e o preço de diversos produtos, e após a inserção de cada produto, 
# deve perguntar se o usuário deseja adicionar mais produtos à lista. O processo de inserção de produtos continuará até que o usuário opte por parar.

# Ao término das inserções, o programa deve fornecer um resumo da compra com as seguintes informações:

# A) Total gasto na compra: O programa deve calcular e exibir a soma de todos os preços dos produtos inseridos.

# B) Quantidade de produtos que custam mais de R$1000: O programa deve contar e exibir quantos dos produtos cadastrados têm preço superior a R$1000.

# C) Nome do produto mais barato: O programa deve identificar e exibir o nome do produto com o menor preço.

# VARIÁVEIS:

total_gasto = 0
prod_maior_mil = []
prod_mais_barato =''
valor_prod_mais_barato = 9999999999
op = 0 # VARIÁVEL DE OPÇÃO

# INTRODUÇÃO:

print('====='*10)
print('\n\n')
print('Ajudante de Compras ao seu dispor!')
print('\n\n')
print('====='*10)

while True:
    print('\n\n')
    print('Lista de Compras:\n[A] Para adicionar um produto a sua Lista de Compras\n[S] Para Sair.')
    print('\n\n')
    op = input('O que deseja fazer: ')
    op.lower()
    print('\n\n')
    print('====='*10)
    if op == 's':
        break
    elif op == 'a':
        print('\n\n')
        produto = input('Qual o produto que deseja adicionar: ')
        valor = float(input(f'Qual o valor do produto {produto}: '))
        if valor < valor_prod_mais_barato:
            prod_mais_barato = produto
            valor_prod_mais_barato = valor
        total_gasto += valor
        if valor > 1000:
            prod_maior_mil.append(produto)
        print('\n\n')
        print('====='*10)
        continue
    else:
        print('\n\n')
        print('Opção Invalida\n\nTente novamente')
        print('\n\n')
        continue

# Calculando o tamanho da lista dos produtos mais caro que R$1.000,00:
qt = len(prod_maior_mil)

# FINALIZAÇÃO

print('\n\n')
print('Extrato:')
print('\n')
print(f'O Total gasto: R${total_gasto:.2f}')
print(f'Temos {qt} produtos acima de R$1.000,00')
print(f'O produto mais barato foi o {prod_mais_barato}')
print('\n\n')
print('====='*10)