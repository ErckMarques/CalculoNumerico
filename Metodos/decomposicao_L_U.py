from eliminacao_gauss import eliminacao_gauss
from numpy import eye, subtract, zeros

def _triangular_superior(U: list[list[float]], b: list[float]) -> list[float]:
   '''
    U: matriz triangular superior
    b: termos independentes do sistema triangular superior

    retorna a solução do sistema
    '''
   tamanho = len(U)

   x = zeros(tamanho)
   x[tamanho-1] = b[tamanho-1] / U[tamanho-1][tamanho-1] # ultimo x[j]

   #range(inicio,parada,passo)
   for k in range(tamanho-2,-1,-1):
      for t in range(k,tamanho):
         b[k] = b[k] - (U[k][t] * x[t])

      x[k] = b[k] / U[k][k]

   return x

def _triangular_inferior(L: list[list[float]], b: list[float]) -> list[float]:
   '''
   A: matriz triangular inferior
   b: termos independentes do sistema triangular inferior

   retorna a solução do sistema
   '''
   tamanho = len(L)

   x = zeros(tamanho)
   x[0] = b[0] # primeiro x[j]

   for k in range(1,tamanho-1):
      for t in range(0,k-1):
         b[k] = b[k] - (L[k][t] * x[t])

   x = b

   return x

def decomposicao_LU(matriz: list[list[float]], matriz_independente: list[float]) -> list[float]:
    '''
    Aplica o método da decomposição LU a uma matriz quadrada fornecida.

    Args:
        matriz(list): matriz quadrada que se deseja decompor, também chamda de matriz dos coeficientes do sistema.
        matriz_independente(list): matriz dos termos independentes (soluções do sistema)

    Returns:
        list: solução do sistema.
    '''
    solucao: list[float]

    # obtendo as matrizes U (escalonada) e a matriz m, dos fatores do escalonamento.
    matrizes = eliminacao_gauss(matriz) 
    
    #separando as matrizes U e m
    matriz_U = matrizes[0] 
    fatores = matrizes[1]  
    
    # criando uma matriz identidade com mesmas dimensões de U
    matriz_L = eye(len(matriz_U)) 
    
    # completando com os fatores do escalonamento
    matriz_L = subtract(matriz_L,fatores) 
   
    # Ly = b
    y = _triangular_inferior(matriz_L,matriz_independente)
    # Ux = y
    solucao = _triangular_superior(matriz_U,y)
    
    return solucao