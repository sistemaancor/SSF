import time
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
def calcular_primos(cantidad):
    primos = []
    numero = 2
    while len(primos) < cantidad:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos
def test_rendimiento():
    cantidad_numeros_primos = 10000
    inicio_tiempo = time.time()
    # Realizar el cálculo de números primos
    primos_calculados = calcular_primos(cantidad_numeros_primos)
    fin_tiempo = time.time()
    tiempo_transcurrido = fin_tiempo - inicio_tiempo
    print(f"Se calcularon {cantidad_numeros_primos} números primos en {tiempo_transcurrido:.4f} segundos.")
    # Puntuación de rendimiento
    puntuacion_rendimiento = 1 / tiempo_transcurrido
    print(f"Puntuación de rendimiento: {puntuacion_rendimiento:.2f}")
if __name__ == "__main__":
    test_rendimiento()
