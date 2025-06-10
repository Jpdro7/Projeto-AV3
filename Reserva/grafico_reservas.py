import matplotlib.pyplot as grafico_reservas

def grafico(reservas):        
    if len(reservas) == 0:
        print("\nNenhum passageiro encontrado !")
        return

    print('\nInforme as datas inicial e final para filtrar.')
    filtrar_periodo1 = input('Data inicial: ')
    filtrar_periodo2 = input('Data final: ')

    verificacao1 = filtrar_periodo1[6:10] + filtrar_periodo1[3:5] + filtrar_periodo1[0:2]
    verificacao2 = filtrar_periodo2[6:10] + filtrar_periodo2[3:5] + filtrar_periodo2[0:2]

    total_vagas_por_usuario = {}

    for r in reservas:
        data_reservada = r["data"]
        reorganizar = data_reservada[6:10] + data_reservada[3:5] + data_reservada[0:2]

        if verificacao1 <= reorganizar <= verificacao2:
            usuario = r["usuario"]
            vagas = int(float(r["vagas_reservadas"]))
            if usuario in total_vagas_por_usuario:
                total_vagas_por_usuario[usuario] += vagas
            else:
                total_vagas_por_usuario[usuario] = vagas

    if not total_vagas_por_usuario:
        print('\nNenhuma reserva encontrada nesse período.')
        return

    nomes = list(total_vagas_por_usuario.keys())
    total_vagas = list(total_vagas_por_usuario.values())

    grafico_reservas.bar(nomes, total_vagas, color='blue')
    grafico_reservas.xlabel('Usuário(s)')
    grafico_reservas.ylabel('Vagas Reservadas')
    grafico_reservas.title('Gráfico de Vagas Reservadas por Usuário')
    grafico_reservas.yticks(range(0, max(total_vagas) + 1))
    grafico_reservas.xticks(rotation = 40)
    grafico_reservas.tight_layout()
    grafico_reservas.show()