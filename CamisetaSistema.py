"""
Sistema de cobrança para pedidos de camisetas.

Funcionalidades:
- Permite escolher o modelo de camiseta
- Calcula descontos com base na quantidade solicitada
- Permite selecionar o tipo de frete
- Calcula o valor total do pedido

Projeto desenvolvido como exercício de lógica de programação em Python.
"""

#Sistema de cobrança de uma fábrica de camisetas
print('Seja bem-vindo(a) a fábrica de camisetas SHIRTs!\n')
print('Modelos disponíveis:')
print('MCS - Manga Curta Simples')
print('MLS - Manga Longa Simples')
print('MCE - Manga Curta com Estampa')
print('MLE - Manga Longa com Estampa\n')

#Definição da função do modelo das camisas
def escolha_modelo():
  while True:
    modelo = input('Qual o modelo desejado? ').upper()
    if modelo not in ('MCS','MLS','MCE','MLE'): #Se o valor inserido não for igual a MCS, MLS, MCE ou MLE vai repetir o laço.
      print('Modelo inválido. Tente novamente!\n')
      continue
    elif modelo == 'MCS':
      return 1.80
    elif modelo == 'MLS':
      return 2.10
    elif modelo == 'MCE':
      return 2.90
    else:
      return 3.20

#Definição da função da quantidade de camisetas com desconto
def num_camisetas():
  while True:
    try: #teste para verificar se o valor inserido é numérico
      print('')
      qtde = int(input('Quantas unidades deseja? '))
    except:
      print('Valor informado Deve ser numérico. Tente novamente! \n')
      continue

    #desconto das peças de acordo com a quantidade solicitada no pedido
    if qtde > 20000:
      print('Não aceitamos pedidos na quantidade informada. Tente novamente.\n')
      continue
    elif qtde < 20:
      return qtde
    elif qtde >= 20 and qtde < 200:
      desc = qtde - (qtde * (5/100))
      return desc
    elif qtde >= 200 and qtde < 2000:
      desc = qtde - (qtde * (7/100))
      return desc
    else:
      desc = qtde - (qtde * (12/100))
      return desc

#Definição da função do frete
def frete():
  print('')
  print('Fretes disponíveis:')
  print('1 - Frete por transportadora - R$100.00')
  print('2 - Frete por Sedex - R$200.00')
  print('0 - Retirar pedido na fábrica - R$0.00\n')
  while True:
    try: #teste para verificar se o valor inserido é numérico
      trans = int(input('Qual o tipo do frete? '))
    except:
      print('Valor informado deve ser numérico. Tente novamente!\n')
      continue

    #valor do frete escolhido
    if trans not in(0, 1, 2):
      print('Frete não encontrado. Tente novamente.\n')
      continue
    elif trans == 1:
      return 100
    elif trans == 2:
      return 200
    else:
      return 0

#código principal (main)
modelo1 = escolha_modelo()
num1 = num_camisetas()
frete1 = frete()

total = (modelo1 * num1) + frete1
print('')
print(f'O Valor total do serviço é de R${total:.2f}. (Modelo: R${modelo1:.2f} * Quantidade com desconto: {num1:.0f} + frete: R${frete1:.2f})')