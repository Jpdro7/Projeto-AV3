def detalhes_da_carona(cadastro, carona):
    verify1 = False
    email_motorista = input('\nEmail: ')
    data_carona2 = input('Data: ')
    print()
    for c in cadastro:
        if email_motorista in c["email"]:
            for c2 in carona:
                if data_carona2 in c2["data"]:
                    print("=" * 50)
                    print(f'\nOrigem: {c2["origem"]}')
                    print(f'Destino: {c2["destino"]}')
                    print(f'Data: {c2["data"]}')
                    print(f'Hora: {c2["hora"]}')
                    print(f'Vagas Restantes: {c2["vagas"]}')
                    print(f'Valor: {c2["valor"]:.2f} R$')
                    print("=" * 50)
                    verify1 = True
                                     
    if not verify1:
        print('Informações não encontradas.')