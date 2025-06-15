import os
from Carona import cadastradas_usuario, cadastrar, detalhes, listar, procurar, relatorio_totalizadores, remover
from Reserva import cancelar, grafico_reservas, reservar
from Usuario import bem_vindo, fazer_cadastro, fazer_login, logout

carona = []
cadastro = []
reservas = []

if os.path.exists('usuarios.txt'):
    with open('usuarios.txt', 'r', encoding = 'utf-8') as importar_usuarios:
        for i in importar_usuarios:
            dados_usuario = i.strip().split(',')
            if len(dados_usuario) == 3:
                usuario, email2, senha2 = dados_usuario
                cadastro.append({
                    "usuario": usuario,
                    "email": email2,
                    "senha": senha2
                })

if os.path.exists('caronas.txt'):
    with open('caronas.txt', 'r', encoding = 'utf-8') as importar_caronas:
        for i2 in importar_caronas:
            dados_carona = i2.strip().split(',')
            if len(dados_carona) == 7:
                usuario_log, local_origem, destino, data_carona, horario, vagas, valor = dados_carona
                carona.append({
                    "usuario": usuario_log,
                    "origem": local_origem,
                    "destino": destino,
                    "data": data_carona,
                    "hora": horario,
                    "vagas": int(vagas),
                    "valor": float(valor)
                })

if os.path.exists('reservas.txt'):
    with open('reservas.txt', 'r', encoding = 'utf-8') as importar_reservas:
        for i3 in importar_reservas:
            dados_reservas = i3.strip().split(',')
            if len(dados_reservas) == 7:
                usuario_log, local_origem, destino, data_carona, horario, valor, quantidade = dados_reservas
                reservas.append({
                    "usuario": usuario_log,
                    "origem": local_origem,
                    "destino": destino,
                    "data": data_carona,
                    "hora": horario,
                    "vagas_reservadas": int(float(dados_reservas[5])),
                    "valor": float(valor)
                })

while True:
    bem_vindo.cabecalho(None)
    print(
        '\n[1] Cadastro' \
        '\n[2] Login')
    opcao = input('\nOpção: ')

    if opcao == '1':
        bem_vindo.cabecalho(None)
        cadastro = fazer_cadastro.cadastrar(cadastro)
        continue
    
    elif opcao == '2':
        usuario_log = fazer_login.login(cadastro)
        bem_vindo.cabecalho(usuario_log)
        if usuario_log is None:
            continue

        while True:
            print(
            '\n[1] Cadastrar Carona' \
            '\n[2] Listar Caronas Disponiveis' \
            '\n[3] Procurar Caronas' \
            '\n[4] Reservar Carona' \
            '\n[5] Cancelar Reserva' \
            '\n[6] Remover Carona' \
            '\n[7] Detalhes Da Carona' \
            '\n[8] Caronas Cadastradas Pelo Usuario' \
            '\n[9] Vizualizar Grafico De Reservas' \
            '\n[10] Relatorio de Totalizadores'
            '\n[0] Logout')
            opcao = input('\nOpção: ')

            if opcao == '1':
                bem_vindo.cabecalho(usuario_log)
                carona = cadastrar.cadastrar_carona(usuario_log, carona)

            elif opcao == '2':
                bem_vindo.cabecalho(usuario_log) 
                listar.listar_caronas(carona)

            elif opcao == '3':
                bem_vindo.cabecalho(usuario_log)
                procurar.procurar_caronas(carona)
                
            elif opcao == '4':
                bem_vindo.cabecalho(usuario_log)
                reservas, carona = reservar.reservar_carona(cadastro, carona, reservas, usuario_log)

            elif opcao == '5':
                bem_vindo.cabecalho(usuario_log)
                reservas, carona = cancelar.cancelar_reserva(carona, reservas, usuario_log)

            elif opcao == '6':
                bem_vindo.cabecalho(usuario_log)
                carona = remover.remover_carona(carona, usuario_log)
                 
            elif(opcao == '7'): 
                bem_vindo.cabecalho(usuario_log)
                detalhes.detalhes_da_carona(cadastro, carona)

            elif(opcao == '8'):
                bem_vindo.cabecalho(usuario_log)
                cadastradas_usuario.caronas_cadastradas_pelo_usuario(carona, reservas, usuario_log)

            elif opcao == '9':
                bem_vindo.cabecalho(usuario_log)
                grafico_reservas.grafico(reservas)

            elif opcao == '10':
                bem_vindo.cabecalho(usuario_log)
                relatorio_totalizadores.relatorio(carona, reservas, usuario_log)

            elif opcao == '0':
                logout.deslogar()
                break
