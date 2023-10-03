# Solicita a distância em Km
distancia_km = float(input("Digite a distância percorrida (em Km): "))

# Solicita o tempo em minutos
tempo_minutos = float(input("Digite o tempo necessário (em minutos): "))

# Calcula a velocidade média em Km/h
velocidade_kmh = distancia_km / (tempo_minutos / 60)

# Calcula a velocidade média em m/s
# 1 Km = 1000 m, 1 hora = 3600 segundos
velocidade_ms = (distancia_km * 1000) / (tempo_minutos * 60)

# Exibe os resultados
print(f"Velocidade média em Km/h: {velocidade_kmh} Km/h")
print(f"Velocidade média em m/s: {velocidade_ms} m/s")