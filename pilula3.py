def converter_nota_para_conceito(nota: float):
    if nota < 3:
        return 'F'
    if nota < 5:
        return 'D'
    if nota < 7:
        return 'C'
    if nota < 9:
        return 'B'
    return 'A'