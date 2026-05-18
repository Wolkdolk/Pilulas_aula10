from pilula4 import calcular_bonus

def test_calculo_bonus():
    assert calcular_bonus(1000,'Bom') == 100
    assert calcular_bonus(1000,'Excelente') == 200
    assert calcular_bonus(1000,'Regular') == 20
    assert calcular_bonus(1000,'Ruim') == 0
    assert calcular_bonus(1000,'Mais ou menos') == 0
