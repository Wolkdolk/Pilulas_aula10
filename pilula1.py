def acao_semaforo(cor: str):
    if cor == 'vermelho':
        return 'Pare'
    elif cor == 'amarelo':
        return 'Atenção'
    elif cor == 'verde':
        return 'Siga'
    
    return 'Cor inválida'