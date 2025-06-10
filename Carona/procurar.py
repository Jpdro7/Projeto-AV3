def procurar_caronas(carona):
    filtrar_origem = input('\nOrigem: ').title()
    filtrar_destino = input('Destino: ').title()
    filtrar_carona = False
    for c in carona:
        if 'origem' in c and 'destino' in c:
            if filtrar_origem in c['origem'] and filtrar_destino in c['destino']:
                print('-' * 50)
                print(f"Usuario: {c['usuario']}")
                print(f"Origem: {c['origem']}")
                print(f"Destino: {c['destino']}")
                print(f"Data: {c['data']}")
                print(f"Hora: {c['hora']}")
                print(f"Vagas: {c['vagas']}")
                print(f"Valor: {c['valor']:.2f} R$")
                filtrar_carona = True
                print('-' * 50)
                
    if not filtrar_carona:
        print('\nNenhuma carona encontrada.')