def calcular_bonus(salario_base: float, avaliacao: str) -> float:

    if salario_base < 0:
        return 0.0


    bonus = {
        "Excelente": 0.20,  # 20%
        "Bom": 0.10,        # 10%
        "Regular": 0.02,    # 2%
        "Ruim": 0.00        # 0%
    }

    # Busca o percentual. Se a string for inválida, o .get() assume 0.00 por padrão
    percentual = bonus.get(avaliacao, 0.00)

    return salario_base * percentual