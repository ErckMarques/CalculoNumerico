from copy import deepcopy
from numpy import zeros, shape


def _valida_matriz_quadrada(matriz: list[list[float]]):
    '''
    Método para verificação de uma matriz quadrada

    Args:
        matriz (list): matriz a ser validada

    Returns: 
        bool: True se a matriz for quadrada, False se a matriz não for quadrada.
    '''
    linhas = len(matriz)
    try:
        for i in range(linhas):
            colunas = len(matriz[i])
            if colunas == linhas:       # verifica se para cada linha o número de colunas é igual ao número de linhas
                continue                # para cada verificação válida, apenas continua. Na iminência de uma invalidação encerra o processo
            else: return False          # se acorrer alguma invalidação, a matriz não é quadrada. Retorna False.
    except:
        return False
    
    return True

def eliminacao_gauss(matriz_coeficientes: list[list[float]], matriz_independente: list[float] = [0.0], parcial: bool=True):
    """
    Implementação do método da Eliminação de Gauss com pivotamento parcial ou total.

    Args:
        matriz_coeficientes (list): Matriz dos coeficientes (A).
        matriz_independente (list): Matriz dos termos independentes (b).
        parcial (bool): Indicador do tipo de pivotamento desejado. Por padrão, é utilizado o método parcial.

    Returns:
        list: Matriz dos coeficientes escalonada.
        list: Matriz dos termos independentes escalonada.
    """

    def _pivotacao(matriz: list[list[float]], matriz_indep: list[float], parcial=True):
        """
        Função para realizar a pivotação parcial ou total de uma matriz.

        Args:
            matriz (list): Matriz dos coeficientes (A).
            matriz_indep (list): Matriz dos termos independentes (b).
            parcial (bool): Indicador do tipo de pivotamento desejado.

        Returns:
            list: Matriz dos coeficientes após a pivotação.
            list: Matriz dos termos independentes após a pivotação.
        """

        if parcial:
            max_index = max(range(k, n), key=lambda i: abs(matriz[i][k]))  # encontra o índice do maior valor absoluto da coluna
            if max_index != k:
                matriz[k], matriz[max_index] = matriz[max_index], matriz[k] # realiza as trocas em A
                matriz_indep[k], matriz_indep[max_index] = matriz_indep[max_index], matriz_indep[k] # Realiza as trocas em b
        else:
            max_row_index = max(range(k, n), key=lambda i: abs(matriz[i][k])) # busca o indice do menor elemento em módulo da linha
            max_col_index = max(range(k, n), key=lambda i: abs(matriz[k][i])) # busca o indice do maior elemento em módulo da coluna

            if max_row_index != k: # troca as linhas
                matriz[k], matriz[max_row_index] = matriz[max_row_index], matriz[k]
                matriz_indep[k], matriz_indep[max_row_index] = matriz_indep[max_row_index], matriz_indep[k]

            if max_col_index != k: # troca as colunas
                for i in range(n):
                    matriz[i][k], matriz[i][max_col_index] = matriz[i][max_col_index], matriz[i][k]

        return matriz, matriz_indep

    if matriz_independente == 0.0:
            b = zeros(shape(matriz_coeficientes))

    n = len(matriz_coeficientes)
    a = deepcopy(matriz_coeficientes)       # Cria uma cópia segura da matriz de coeficientes
    b = deepcopy(matriz_independente)       # Cria uma cópia segura da matriz de termos independentes

    if _valida_matriz_quadrada(matriz_coeficientes):
        for k in range(n):
            if a[k][k] == 0:
                a, b = _pivotacao(a, b, parcial)
                if a[k][k] == 0:
                    raise ValueError("A matriz é singular! A matriz fornecida tem muitos elementos proximos de zero.") 

            for i in range(k + 1, n):
                fator = a[i][k] / a[k][k]
                a[i][k] = 0
                for j in range(k + 1, n):
                    a[i][j] -= fator * a[k][j]
                b[i] -= fator * b[k]
    else: 
        raise ValueError("A matriz não eh quadrada! Forneça uma matriz quadrada.")

    if all(elemento == 0.0 for elemento in b):
        return a
    else: 
        return a, b

