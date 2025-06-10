def relatorio(caronas, reservas, usuario_log):
    encontrou = False
    total_geral = 0.0

    for c in caronas:
        for r in reservas:
            if c["usuario"] == usuario_log:
                encontrou = True
                valor = float(c["valor"])
                passageiros = int(r["vagas_reservadas"])
                total = valor * passageiros
                total_geral += total

                print()
                print("-" * 50)
                print('Relatorio Totalizado'.center(50))
                print("-" * 50)
                print(f'Origem: {c["origem"]}')
                print(f'Destino: {c["destino"]}')
                print(f'Data: {c["data"]}')
                print(f'Hora: {c["hora"]}')
                print(f'Valor: {valor:.2f} R$')
                print(f'Passageiros: {passageiros}')
                print(f'Vagas restantes: {c["vagas"]}')
                print(f'Total: R$ {total:.2f}')
                print("-" * 50)

    if encontrou:
        print("=" * 50)
        print(f"Total geral: {total_geral:.2f} R$")
        print("=" * 50)

        salvar_relatorio = input('\nVocê deseja salvar o relatorio ? ')
        if salvar_relatorio == 's':
            with open('relatorio.txt', 'a', encoding = 'utf-8') as relatorio_salvo:
                dados_salvos = (f'{c["origem"]},{c["destino"]},{c["data"]},{c["hora"]},{valor:.2f},{passageiros}.{c["vagas"]},{total:.2f}\n')
                relatorio_salvo.write(dados_salvos)
        else:
            return
    else:
        print("\nRegistro de carona não encontrada.")