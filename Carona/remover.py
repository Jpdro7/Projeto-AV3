def remover_carona(carona, usuario_log):
    remover_verify = False
    remover_carona = input('\nData: ')

    while len(remover_carona) < 10 or '/' not in remover_carona[2] or '/' not in remover_carona[5]:
        print('\nData invalida !')
        print('Digite novamente.')
        remover_carona = input('\nData: ')
        
    for c in carona:
        if remover_carona in c["data"] and c["usuario"] == usuario_log:
            remover_verify = True
            carona.remove(c)
            print('\nCarona removida.')
            break

    if not remover_verify:
        print('\nCarona não encontrada.')
    return carona