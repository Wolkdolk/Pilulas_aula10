from pilula2 import calcular_frete

def test_fretes():
    assert calcular_frete(1.0) == 5.0
    assert calcular_frete(1.01)  == 10.0
    assert calcular_frete(5.01) == 18
    assert calcular_frete(0) == 0
    assert calcular_frete(-10) == 0