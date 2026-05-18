def aplicar_cupom(codigo_cupom: str, valor_compra: float) -> float:
    cupom_formatado = codigo_cupom.upper()

    regras_cupons = {
        "CUPOM10": (0.10, 0.0),
        "CUPOM25": (0.25, 100.0),
        "DESCONTOVIP": (0.35, 500.0)
    }

    if cupom_formatado not in regras_cupons:
        return 0.0

    percentual, valor_minimo = regras_cupons[cupom_formatado]

    if valor_compra > valor_minimo:
        return percentual
    
    return 0.0