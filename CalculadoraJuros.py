"""
Calculadora simples de juros para compras parceladas.

Funcionalidades:
- Recebe o valor de um pedido
- Recebe a quantidade de parcelas desejada
- Aplica juros de acordo com a quantidade de parcelas
- Calcula o valor de cada parcela
- Exibe o valor total da compra parcelada

Projeto desenvolvido como exercício de lógica de programação em Python.
"""

#Apresentação da aplicação
print('Seja bem-vindo(a) a Calculadora de Juros!\n')

#inserção do valor do pedido e da quantidade de parcelas
valorPedido = float(input('Qual o valor do seu pedido? '))
parcelas = int(input('E a quantidade de parcelas? '))

#Aplicação dos juros conforme número de parcelas
if parcelas < 4:
  Juros = 0
  print('Não houve acréscimo de juros em sua compra!\n')
elif parcelas >= 4 and parcelas < 6:
  Juros = 4/100 #juros de 4%
  print('Houve acréscimo de 4% juros em sua compra.\n')
elif parcelas >= 6 and parcelas < 9:
  Juros = 8/100 #juros de 8%
  print('Houve acréscimo de 8% juros em sua compra.\n')
elif parcelas >= 9 and parcelas < 13:
  Juros = 16/100 #juros de 16%
  print('Houve acréscimo de 16% juros em sua compra.\n')
else:
  Juros = 32/100 #juros de 32%
  print('Houve acréscimo de 32% juros em sua compra.\n')

#Cálculo do valor das parcelas e do valor final
valorDaParcela = (valorPedido * (1 + Juros))/parcelas
TotalParcelado = valorDaParcela * parcelas

#Apresentação dos valores para o cliente
print(f'O valor de cada parcela ficou de R${valorDaParcela: .2f}')
print(f'O valor total parcelado ficou de R${TotalParcelado: .2f}')