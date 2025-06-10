def caronas_cadastradas_pelo_usuario(caronas, reservas, usuario_logado):
    caronas_usuario = False
    for c in caronas:
        if c["usuario"] == usuario_logado:
            caronas_usuario = True
            passageiros = 0
            for r in reservas:
                if r["data"] == c["data"] and r["origem"] == c["origem"] and r["destino"] == c["destino"]:
                    passageiros += int(r["vagas_reservadas"])     
            vagas_restantes = c["vagas"]
     
            print('=' * 50)
            print(f'Origem: {c["origem"]}')
            print(f'Destino: {c["destino"]}')
            print(f'Data: {c["data"]}')
            print(f'Hora: {c["hora"]}')
            print(f'Valor: {c["valor"]:.2f} R$')
            print(f'Passageiros: {passageiros}')
            print(f'Vagas Restantes: {vagas_restantes}')
            print('=' * 50)
    
    if not caronas_usuario:
        print('\nCarona não encontrada.')