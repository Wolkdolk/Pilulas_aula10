from pilula5 import aplicar_cupom

def test_cupom():
    assert aplicar_cupom("CUPOM10", 50.0) == 0.10
    assert aplicar_cupom("cupom10", 200.0) == 0.10  # Testando minúsculo
    assert aplicar_cupom("CUPOM25", 150.0) == 0.25
    assert aplicar_cupom("CUPOM25", 80.0) == 0.0
    assert aplicar_cupom("CUPOM25", 100.0) == 0.0
    assert aplicar_cupom("DESCONTOVIP", 600.0) == 0.35
    assert aplicar_cupom("descontovip", 450.0) == 0.0
    assert aplicar_cupom("DESCONTOVIP", 500.0) == 0.0
    assert aplicar_cupom("CUPOM_FALSO", 1000.0) == 0.0