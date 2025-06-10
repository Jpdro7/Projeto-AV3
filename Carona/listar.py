def listar_caronas(carona):
    if not carona:
        print('\nRegistro de carona não encontrado.')
        return
    contador = 1
    for c in carona:
        print('-' * 50)
        print(f'\nCarona nº {contador}\n')
        print(f"Usuario: {c['usuario']}")
        print(f"Origem: {c['origem']}")
        print(f"Destino: {c['destino']}")
        print(f"Data: {c['data']}")
        print(f"Hora: {c['hora']}")
        print(f"Vagas: {c['vagas']}")
        print(f"Valor: {c['valor']:.2f} R$")
        contador += 1
        print('-' * 50)