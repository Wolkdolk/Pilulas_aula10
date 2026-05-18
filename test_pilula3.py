from pilula3 import converter_nota_para_conceito

def test_conversao_notas():
    assert converter_nota_para_conceito(2.9) == 'F'
    assert converter_nota_para_conceito(3.0) == 'D'
    assert converter_nota_para_conceito(4.9) == 'D'
    assert converter_nota_para_conceito(5.0) == 'C'
    assert converter_nota_para_conceito(6.9) == 'C'
    assert converter_nota_para_conceito(7.0) == 'B'
    assert converter_nota_para_conceito(8.9) == 'B'
    assert converter_nota_para_conceito(9.0) == 'A'
    