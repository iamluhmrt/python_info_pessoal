ano_base = 2023
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_base - ano_nascimento
aniversario = input('Você fez aniversário esse ano?: ')
if aniversario == "no":
  idade -= 1
maior_de_idade = idade >= 18
altura_metros = float(input('Digite sua altura: '))
print('Nome: ', nome)
print('Sobrenome: ', sobrenome)
print('Idade: ', idade)
print('Ano de nascimento: ', ano_nascimento)
print('É maior de idade? ', maior_de_idade)
print('Altura em metros: ', altura_metros)
