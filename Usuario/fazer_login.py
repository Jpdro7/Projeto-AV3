def login(cadastro):
    login_email = input('\nEmail: ')
    login_senha = input('Senha: ')
    for c in cadastro:
        if login_email == c["email"] and login_senha == c["senha"]: 
            usuario_log = c["usuario"]
            return usuario_log
    print('\nDados não encontradas !')
    return None
