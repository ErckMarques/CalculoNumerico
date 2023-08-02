from numpy import transpose

def valida_matriz_quadrada(matriz: list[list[float]]) -> bool:
    '''
    Método para verificação de uma matriz quadrada.

    Args:
        matriz (list): matriz a ser validada

    Returns: 
        bool: True se a matriz for quadrada, False se a matriz não for quadrada.
    '''

    linhas = len(matriz)
    colunas = [len(linha) for linha in matriz] # cada elemento de colunas recebe o numero de colunas de cada linha da matriz

    return all(coluna == linhas for coluna in colunas)

def matriz_simetrica(matriz):
    '''
    Método que verifica se uma matriz é simétrica ou não.
    Isto é: 
            A = AT, AT -> transposta de A.

    Args:
        matriz list[list[float]]: matriz a ser verificada.

    Returns:
        bool: True se é simétrica. False se não for simétrica.
    '''
    if not valida_matriz_quadrada(matriz):
        return False

    return all(matriz[i][j] == matriz[j][i] for i in range(len(matriz)) for j in range(len(matriz[0])))
