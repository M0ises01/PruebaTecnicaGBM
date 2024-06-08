def procesar_campeonatos(data):
    resultados = []
    index = 0
    output = []
    data = data.strip().split("\n")

    while True:
        G, P = map(int, data[index].split())
        if G == 0 and P == 0:
            break
        index += 1

        resultados = []
        for _ in range(G):
            resultados.append(list(map(int, data[index].split())))
            index += 1

        S = int(data[index])
        index += 1

        sistemas_puntuacion = []
        for _ in range(S):
            sistema = list(map(int, data[index].split()))
            sistemas_puntuacion.append(sistema)
            index += 1

        for sistema in sistemas_puntuacion:
            K = sistema[0]
            puntos = sistema[1:]

            # Inicializar el puntaje de cada piloto en cero
            puntajes = [0] * P

            for resultado in resultados:
                for i in range(P):
                    posicion = resultado[i] - 1  # La posición en la carrera
                    if posicion < K:
                        puntajes[i] += puntos[posicion]

            # Determinar el/los campeones
            max_puntos = max(puntajes)
            campeones = [i + 1 for i in range(P) if puntajes[i] == max_puntos]
            
            # Almacenar resultados
            output.append(" ".join(map(str, campeones)))
    
    output = "\n".join(output)
    return output
