def tiempo_total_vueltas(n, x):
    tiempo_por_vuelta = 90  # Tiempo base por vuelta en segundos (1 minuto y 30 segundos)
    incremento_desgaste = 1.15  # Desgaste por cada vuelta en porcentaje
    incremento_tiempo = 0.2  # Incremento de tiempo por vuelta debido al desgaste en segundos
    desgaste_actual = 0  # Desgaste inicial
    tiempo_total = 0  # Tiempo total inicial
    vueltas_completadas = 0  # Contador de vueltas completadas
    penalizacion_parada = 25  # Penalización por parada en boxes en segundos
    paradas_boxes = 0  # Contador de paradas en boxes

    while vueltas_completadas < n:
        # Agregamos el tiempo de la vuelta actual
        tiempo_total += tiempo_por_vuelta
        desgaste_actual += incremento_desgaste
        vueltas_completadas += 1

        # Si el desgaste alcanza o supera el límite, hacemos una parada
        if desgaste_actual >= x:
            tiempo_total += penalizacion_parada  # Añadimos tiempo por la parada en boxes
            desgaste_actual = 0  # Reiniciar el desgaste a 0 tras la parada
            tiempo_por_vuelta = 90  # Reiniciar el tiempo de vuelta tras la parada
            paradas_boxes += 1  # Incrementamos el contador de paradas
        else:
            # Incrementamos el tiempo de la vuelta en 0.2 segundos
            tiempo_por_vuelta += incremento_tiempo

    # Convertimos el tiempo total a minutos
    tiempo_total_minutos = tiempo_total / 60

    # Imprimir resultados de manera bonita
    print(f"Resultados para {n} vueltas y límite de desgaste del {x}%:")
    print(f"- Tiempo total: {tiempo_total_minutos:.2f} minutos")
    print(f"- Paradas en boxes: {paradas_boxes}")
    
    return tiempo_total_minutos, paradas_boxes

# Llamamos a la función con 60 vueltas y un límite de desgaste del 40%
tiempo_total_vueltas(60, 40)

