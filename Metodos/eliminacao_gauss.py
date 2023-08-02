from copy import deepcopy
from numpy import zeros, shape
from condicoes import valida_matriz_quadrada

def eliminacao_gauss(matriz_coeficientes: list[list[float]], matriz_independente: list[float] = [0.0], parcial: bool=True):
    """ 
    Executa o Método da Eliminação de Gauss (com pivotamento parcial ou total) num sistema de equações lineares.

    Args:
        matriz_coeficientes (list[list[float]]): Matriz dos coeficientes (A).
        matriz_independente (list[float]): Matriz dos termos independentes (b).
        parcial (bool): Indicador do tipo de pivotamento desejado. Por padrão, é utilizado o método parcial.

    Returns:
        resposta: uma lista contendo as listas abaixo:
            list[list[float]]: Matriz dos coeficientes escalonada.
            list[list[float]]: Matriz dos termos independentes modificados segundo as operações do escalonamento.
            np.array: Matriz dos fatores utilizados no escalonamento. Útil ao método LU.
    -----------
    Exemplo:
        
        matriz_coeficientes = [[1,-2,4],[4,0,6],[8,6,8]]
        termos_independentes = [4,1,5]
        
        matrizes_respostas = eliminacao_gaus(matriz_coeficientes, termos_independentes)
        
        A = np.array(matrizes_respostas[0])     # matriz A escalonada.
        b = np.array(matrizes_respostas[1][0])  # matriz b dos termos independentes após escalonamento.
        m = np.array(matrizes_respostas[2])     # matriz dos fatores utilizados no processo de escalonamento.
        
        Saída:
        
        A = array([[  1.   -2.    4. ]
                   [  0.    8.  -10. ]
                   [  0.    0.    3.5]]
        
        b = array([4., -15, 14.25])

        fatores = array([[ 0.,  0.,  0.],
                         [-1.,  0.,  0.],
                         [-1., -8.,  0.]])
    -----------
    """

    def _pivotacao(matriz: list[list[float]], matriz_indep: list[float] = [0.0], parcial: bool=True):
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

    if matriz_independente == [0.0]:
        matriz_independente = zeros(len(matriz_coeficientes))

    n = len(matriz_coeficientes)
    a = deepcopy(matriz_coeficientes)       # Cria uma cópia segura da matriz de coeficientes
    b = deepcopy(matriz_independente)       # Cria uma cópia segura da matriz de termos independentes
    m = zeros(shape(matriz_coeficientes))     # Cria uma matriz identidade a partir da matriz de coeficientes. Objeto Numpy.
    respostas = []

    if valida_matriz_quadrada(matriz_coeficientes):
        for k in range(n):
            if a[k][k] == 0:
                a, b = _pivotacao(a, b, parcial)
                if a[k][k] == 0:
                    raise ValueError("A matriz é singular! A matriz fornecida tem muitos elementos proximos de zero.") 

            for i in range(k + 1, n):
                fator = a[i][k] / a[k][k]
                m[i][k] -= fator                            # preenchendo a lista com os fatores de eliminação                
                b[i] -= fator * b[k]                        # alteração no vetor independente
                for j in range(k + 1, n):                                  
                    a[i][j] -= fator * a[k][j]              # alteração na linha 
                    a[i][k] = 0
    else: 
        raise ValueError("A matriz não eh quadrada! Forneça uma matriz quadrada.")

    # converter em objetos numpy depois

    if all(elemento == 0.0 for elemento in b):
        respostas.append(a)
        respostas.append(m)
    else: 
        respostas.append(a)
        respostas.append([b])
        respostas.append(m)

    return respostas

def eliminacao_gauss_jordan(matriz_coeficientes: list[list[float]], matriz_independente: list[float] = [0.0], parcial: bool=True):
    '''
    Método que implementa a Eliminação de Gauss-Jordan ou escalonamento completo.
    
    Args:
        matriz_coeficientes (list[list[float]]): Matriz dos coeficientes (A).
        matriz_independente (list[float]): Matriz dos termos independentes (b).
        parcial (bool): Indicador do tipo de pivotamento desejado. Por padrão, é utilizado o método parcial.

    Returns:
        resposta: uma lista contendo as listas abaixo:
            list[list[float]]: Matriz dos coeficientes escalonada.
            list[list[float]]: Matriz dos termos independentes modificados segundo as operações do escalonamento.
            np.array: Matriz dos fatores utilizados no escalonamento. Útil ao método LU.
    -----------
    '''