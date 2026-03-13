"""
Sistema simples de pedidos para uma lanchonete.

Funcionalidades:
- Permite escolher o tipo de refeição disponível no cardápio
- Permite selecionar o tamanho do prato
- Calcula o valor de cada pedido
- Permite adicionar múltiplos pedidos
- Exibe o valor total da compra

Projeto desenvolvido como exercício de lógica de programação em Python.
"""

#Apresentação da empresa
print('Seja bem-vindo(a) a Lanchonete Prato Feito!\n')
print('-----------------------------------------------------------')
print('                  -> Pratos do dia <-                      ')
print('                                                           ')
print('       Bife Acebolado (BA)     Filé de Frango (FF)         ')
print('       Pequeno (1) -- R$16     Pequeno (1) -- R$15         ')
print('       Médio   (2) -- R$18     Médio   (2) -- R$17         ')
print('       Grande  (3) -- R$22     Grande  (3) -- R$21         ')
print('-----------------------------------------------------------')

valorTotal = 0 #valor inicial necessário para o acumulador


#Escolha do tipo e o tamanho do prato
while True:
  print('')
  sabor = input('Qual refeição deseja? (Digite BA ou FF) ').upper() #upper deixa todas as letras em maiúsculo
  if sabor != 'BA' and sabor !='FF':
    print('Escolha inválida. Tente novamente!')
    continue

  tamanho = int(input('Qual tamanho do prato? '))
  if tamanho != 1 and tamanho != 2 and tamanho != 3:
    print('Tamanho inválido. Tente novamente!')
    continue

  if sabor == 'BA':
    sabor1 = 'Bife Acebolado'
  else:
    sabor1 = 'Filé de Frango'

  if tamanho == 1:
    tamanho1 = 'Pequeno'
  elif tamanho == 2:
    tamanho1 = 'Médio'
  else:
    tamanho1 = 'Grande'


  if sabor == 'BA':
    if tamanho == 1:
      valor = 16
    elif tamanho == 2:
      valor = 18
    else:
      valor = 22
  else: #Aqui é para FF
    if tamanho == 1:
      valor = 15
    elif tamanho == 2:
      valor = 17
    else:
      valor = 21

  print(f'Você pediu um {sabor1} no tamanho {tamanho1} que custa R${valor:.2f}.\n')

  valorTotal += valor #acumulador

#pergunta ao usuário se ele deseja mais alguma coisa
  pergunta = input('Deseja pedir mais alguma coisa (S/N)? ')
  if pergunta == 'S':
    continue
  else:
    break

print(f'O valor total do seu pedido será de R${valorTotal:.2f}.\n')
print('Aproveite sua refeição!')