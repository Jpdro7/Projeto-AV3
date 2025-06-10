def cancelar_reserva(carona, reservas, usuario_log):
    reserva_verify2 = False
    reserva_cancelamento2 = input('Data: ')

    while len(reserva_cancelamento2) < 10 or '/' not in reserva_cancelamento2[2] or '/' not in reserva_cancelamento2[5]:
        print('\nData invalida !')
        print('Digite novamente.')
        reserva_cancelamento2 = input('\nData: ')

    for c in carona:
        if reserva_cancelamento2 in c["data"]:
            for r in reservas:
                if r["data"] == c["data"]:
                    reserva_verify2 = True
                    print('\nReserva encontrada.')
                    cancelar = input('Cancelar ? ')
                    if cancelar == 's':
                        c["vagas"] += int(r["vagas_reservadas"])
                        print('\nReversa cancelada.')
                        r["vagas"] = 0
                        reservas.remove(r)
                    break
            break
                        
    if not reserva_verify2:
        print('\nReserva não encontrada.')
    return reservas, carona