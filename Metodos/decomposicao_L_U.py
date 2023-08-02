from eliminacao_gauss import eliminacao_gauss
from numpy import eye, subtract, zeros
from typing import List

def _triangular_superior(U: List[List[float]], b: List[float]) -> List[float]:
    '''
    Função que resolve o sistema Ux = y.

    Args:
        U: Matriz triangular superior.
        b: Termos independentes do sistema triangular superior.

    Returns:
        solucao: Vetor solução do sistema.
    '''
    tamanho = len(U)
    solucao = zeros(tamanho)
    solucao[tamanho-1] = b[tamanho-1] / U[tamanho-1][tamanho-1] # Último solucao[j]

    for k in range(tamanho-2, -1, -1):
        for t in range(k, tamanho):
            b[k] = b[k] - (U[k][t] * solucao[t])

        solucao[k] = b[k] / U[k][k]

    return solucao

def _triangular_inferior(L: List[List[float]], b: List[float]) -> List[float]:
    '''
    Função que resolve o sistema Ly = b.

    Args:
        L: Matriz triangular inferior.
        b: Termos independentes do sistema triangular inferior.

    Returns:
        solucao: Vetor solução do sistema.
    '''
    tamanho = len(L)
    solucao = zeros(tamanho)
    solucao[0] = b[0] # Primeiro solucao[j]

    for k in range(1, tamanho-1):
        for t in range(0, k-1):
            b[k] = b[k] - (L[k][t] * solucao[t])

    solucao = b

    return solucao

def decomposicao_LU(matriz: List[List[float]], matriz_independente: List[float]) -> List[float]:
    '''
    Aplica o método da decomposição LU a uma matriz quadrada fornecida.

    Args:
        matriz (list[list[float]]): 
            Matriz quadrada que se deseja decompor, também chamada de matriz dos coeficientes do sistema.
            
        matriz_independente (list[float]): Matriz dos termos independentes (soluções do sistema).

    Returns:
        solucao (list[float]): Vetor solução do sistema.
    '''
    matrizes = eliminacao_gauss(matriz)     # Obtendo as matrizes U (escalonada) e a matriz m, dos fatores do escalonamento.
    matriz_U = matrizes[0] 
    fatores = matrizes[1] 

    matriz_L = eye(len(matriz_U))           # Criando uma matriz identidade com as mesmas dimensões de U
    matriz_L = subtract(matriz_L, fatores)  # Completando com os fatores do escalonamento

    y = _triangular_inferior(matriz_L, matriz_independente) # Ly = b
    solucao = _triangular_superior(matriz_U, y) # Ux = y

    return solucao