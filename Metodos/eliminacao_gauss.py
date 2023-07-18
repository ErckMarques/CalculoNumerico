
def eliminacao_gauss(matriz_coeficientes, matriz_independente, parcial=True):
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

    def _pivotacao(matriz, matriz_indep, parcial=True):
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

    n = len(matriz_coeficientes)
    a = matriz_coeficientes[:]                    # Cria uma cópia da matriz de coeficientes
    b = matriz_independente[:]                    # Cria uma cópia da matriz de termos independentes

    for k in range(n):
        if a[k][k] == 0:
            a, b = _pivotacao(a, b, parcial)
            if a[k][k] == 0:
                raise ValueError("A matriz é singular!")

        for i in range(k + 1, n):
            fator = a[i][k] / a[k][k]
            a[i][k] = 0
            for j in range(k + 1, n):
                a[i][j] -= fator * a[k][j]
            b[i] -= fator * b[k]

    return a, b

# método para imprimir uma matriz bonitinha
def imprime(matriz):
    linhas, colunas = len(matriz), len(matriz[0])
    # condição para 1 linha e 1 coluna
    for i in range(linhas):
        print("|", end=" ")
        for j in range(colunas):
            print(f"{matriz[i][j]:^3}", end=" ")
        print("|")
    return ""