def cadastrar(cadastro):
    usuario = input('\nNome de usuario: ')
    email1 = input('\nEmail: ')
    email2 = input('Confirmar Email: ')

    while email2 != email1:
        print("\nEmail's diferente !")
        print("Verifique os email's e tente novamente.")
        email1 = input('\nEmail: ')
        email2 = input('Confirmar Email: ')

    while len(email1) < 1 or "@gmail.com" not in email1:
        print('\nEmail invalido !')
        print('Digite o email com nome de dominio do gmail.')
        email1 = input('\nEmail: ')
        email2 = input('Confirmar Email: ')

    for c in cadastro:
        while c["email"] == email1:
            print('\nEsse email já esta cadastrado, cadastre outro !')
            email1 = input('\nEmail: ')
            email2 = input('Confirmar Email: ')
    
    print('\nCadastre sua senha, ela deve conter sete ou mais caracteres.')
    senha1 = input('Senha: ')
    senha2 = input('Confirmar Senha: ')

    while senha2 != senha1 or len(senha1) < 7:
        print('\nAs senhas não conferem ou tem menos de sete caracteres !')
        print('Verifique as senhas e tente novamente.')
        senha1 = input('\nSenha: ')
        senha2 = input('Confirmar Senha: ')

    print('\nEmail e Senha cadastrados com sucesso.')
    print('Cadastro concluido.')

    cadastro2 = {
        "usuario": usuario,
        "email": email2,
        "senha": senha2
    }
    cadastro.append(cadastro2)

    with open('usuarios.txt', 'a', encoding = 'utf-8') as dados:
        dados.write(f'{usuario},{email2},{senha2}\n')
        
    return cadastro