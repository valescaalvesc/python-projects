#Guess the number
from random import randint

print('Olá!')
nome = input('Qual seu nome: \n')
print('Espero que goste do jogo' +nome)
input(nome+ ', você terá 3 tentativas para acertar o número sorteado. Boa sorte!')
print ('O número já foi sorteado!')

i = 1
while i <= 3:
    num = input(('Digite um núnero de 0 a 9:'))
    i += 1
    sort = (randint(0,9))
else:
    print('O número sorteado foi:')
    print(randint(0,9))

if num == sort:
    print('Você acertou!')
    
elif (num != sort):
    print('Tente novamente em outra rodada!')

    

