def calcular_frete(peso_kg: float):
    if peso_kg <= 0:
        return 0
    elif peso_kg <= 1:
        return 5
    elif peso_kg <= 5:
        return 10
    
    return 18