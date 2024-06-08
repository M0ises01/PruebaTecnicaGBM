def calcular_saltos(x):
    jumps = 0
    # Inicializamos la suma acumulada en 0
    cumulative_sum = 0
    
    # Mientras la suma acumulada sea menor que x
    while cumulative_sum < x:
        # Incrementamos el número de saltos en 1
        jumps += 1
        # Sumamos el próximo número entero positivo a la suma acumulada
        cumulative_sum += jumps
    
    # Si la suma acumulada es mayor que x y es impar,
    # necesitaremos un salto adicional para llegar a x
    if (cumulative_sum - x) % 2 != 0:
        jumps += 1
    
    return jumps
