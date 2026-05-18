from pilula1 import acao_semaforo

def test_cores():
    assert acao_semaforo('vermelho') == 'Pare'
    assert acao_semaforo('amarelo') == 'Atenção'
    assert acao_semaforo('verde') == 'Siga'
    assert acao_semaforo('roxo') == 'Cor inválida'