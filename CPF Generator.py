senha_registrada = ''
email_registrado = ''


while True:
    pedido_email = input ('Digite seu email: ')
    print()
    if '.com' not in pedido_email or '@' not in pedido_email:
        print('Email inválido! ')
        
    else:
        print('Email registrado! ')
        email_registrado = pedido_email  
        break    

while True:
    pedido = input ('Digite sua senha nova: ')
    print()
    
    if len(pedido) < 7:
        print('Senha muito curta, insiria no minímo 7 caractéres!')
        continue
  
    pedido_2 = input ('Cofirme sua senha: ')
    if pedido != pedido_2:
        print('Senhas não são iguais, tente novamente! ')

    elif pedido == pedido_2:
        senha_registrada = pedido
        break

i = 3
while i != 0:

    email = input('Digite seu email para entrar: ')
    if email != email_registrado:
        print('Email não existe! ')
        continue
    else:
        print()
    while True:
        senha = input('Digite sua senha: ')
        if senha != senha_registrada:
            i -= 1
            print(f'Senha incorreta! Tentativas restantes: {i}')
            print()
            if i == 0:
                print('Vocẽ digitou a senha incorreta muitas vezes! ')
                break
        else:
            print('Você entrou na sua conta! ')
            break
    import random
    def gerador_cpf():
        nove_digitos = ''
        for i in range(9):
            nove_digitos += str(random.randint(0, 9))

        contagem = 10

        resultado_digito_1 = 0
        for nums in nove_digitos[0:9]:
            resultado_digito_1 += int(nums) * contagem
            contagem -= 1
        digito_1 = (resultado_digito_1 * 10) % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        dez_digitos = nove_digitos + str(digito_1)

        contagem_2 = 11
        resultado_digito_2 = 0
        for nums_2 in dez_digitos:
            resultado_digito_2 += int(nums_2) * contagem_2
            contagem_2 -= 1
        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0
        onze_digitos = dez_digitos + str(digito_2)    
        return (f'{onze_digitos[0:3]}.{onze_digitos[3:6]}.{onze_digitos[6:9]}-{onze_digitos[9:11]}')

    if email == email_registrado and senha == senha_registrada:
        pedido = input("Insira a quantidade de CPF's que deseja gerar: ")
        print()

        i = 1
        for _ in range(int(pedido)):
            print(f'CPF nº{i}: {gerador_cpf()}') 
            print()
            i += 1
        
    print('Obrigado por usar! ')
    break
