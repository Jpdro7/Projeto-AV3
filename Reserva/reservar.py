def reservar_carona(cadastro, carona, reservas, usuario_log):
    quantidade = 0
    
    reserva1 = input('\nEmail: ')
    while len(reserva1) < 1 or '@gmail.com' not in reserva1:
        print('\nEmail invalido !')
        print('Digite novamente.')
        reserva1 = input('\nEmail: ')

    reserva2 = input('Data: ')
    while len(reserva2) < 10 or '/' not in reserva2[2] or '/' not in reserva2[5]:
        print('\nData invalida !')
        print('Digite novamente.')
        reserva2 = input('\nData: ')

    reserva_verify = False
    for c in cadastro:
        if reserva1 in c["email"]:
            for c in carona:
                if reserva2 in c["data"]:
                    if c["vagas"] > 0:
                        reserva_verify = True
                        print('\nVaga disponivel.')
                        reserva3 = input('Reservar ? ').lower()
                        if reserva3 == 's':
                            quantidade = int(input('Quantas Vagas ? '))
                            if quantidade > c["vagas"]:
                                print('\nQuantidade de vagas não disponiveis.')
                            else:
                                c["vagas"] -= quantidade
                                
                                with open('caronas.txt', 'w', encoding = 'utf-8') as importar_caronas:
                                    for c in carona:
                                        dados_carona = (f'{c["usuario"]},{c["origem"]},{c["destino"]},{c["data"]},{c["hora"]},{c["vagas"]},{c["valor"]}\n')
                                        importar_caronas.write(dados_carona)      
                                
                                reserva = {
                                    "usuario": usuario_log,
                                    "origem": c["origem"],
                                    "destino": c["destino"],
                                    "data": c["data"],
                                    "hora": c["hora"],
                                    "vagas_reservadas": quantidade,
                                    "valor": c["valor"]
                                    }
                                reservas.append(reserva)

                                with open('reservas.txt', 'w', encoding = 'utf-8') as importar_reservas:
                                    for r in reservas:
                                        dados_reserva = (f'{r["usuario"]},{r["origem"]},{r["destino"]},{r["data"]},{r["hora"]},{r["vagas_reservadas"]},{r["valor"]}\n')
                                        importar_reservas.write(dados_reserva)

                                reserva_verify = True
                                print('\nVaga reservada.')
                        break

    if not reserva_verify:
        print('\nCarona não encontrada.')
    return reservas, carona