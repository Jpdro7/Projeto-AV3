def cadastrar_carona(usuario_log, carona):
    condicao_data = 0
    
    local_origem = input('\nOrigem: ').title()
    destino = input('Destino: ').title()
    data_carona = input('Data: ')

    while len(data_carona) != 10 or data_carona[2] != '/' or data_carona[5] != '/':
        print('\nData invalida !')
        print('Digite novamente.')
        data_carona = input('\nData: ')

    if int(data_carona[3:5]) in [1, 3, 5, 7, 8, 10, 12]:
        condicao_data = 31

    elif int(data_carona[3:5]) in [4, 6, 9, 11]:
        condicao_data = 30

    elif int(data_carona[3:5]) == 2:
        condicao_data = 28

    if int(data_carona[0:2]) > condicao_data or int(data_carona[3:5]) > 12 or int(data_carona[6:10]) < 2025 or int(data_carona[6:10]) > 2025:
        while True:
            print('\nData invalida !')
            print('Digite novamente.')
            data_carona = input('\nData: ')

            if int(data_carona[0:2]) <= condicao_data and int(data_carona[3:5]) <= 12 and int(data_carona[6:10]) == 2025:
                break
            if int(data_carona[0:2]) > condicao_data and int(data_carona[3:5]) > 12 and int(data_carona[6:10]) < 2025 and int(data_carona[6:10]) > 2025:
                continue

    horario = input('Hora: ') 

    while len(horario) != 5 or horario[2] != ':':
        print('\nHora invalida !')
        print('Digite novamente.')
        horario = input('Hora: ')

    vagas = int(input('Vaga(s) disponivel: '))
    valor = float(input('Valor por vaga: '))

    carona2 = {
        "usuario": usuario_log,
        "origem": local_origem,
        "destino": destino,
        "data": data_carona,
        "hora": horario,
        "vagas": vagas,
        "valor": valor
        }
    carona.append(carona2)
    print('\nCarona cadastrada com sucesso.')

    with open('caronas.txt', 'w', encoding = 'utf-8') as importar_caronas:
        for c in carona:
            dados_carona = (f'{c["usuario"]},{c["origem"]},{c["destino"]},{c["data"]},{c["hora"]},{c["vagas"]},{c["valor"]}\n')
            importar_caronas.write(dados_carona)
    
    return carona