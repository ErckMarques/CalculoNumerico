def imprime(matriz):
    '''
    Método para imprimir uma matriz de forma convencional (ainda precisa de ajustes, mas no geral, funciona bem).

    Args: 
        matriz (list): matriz a ser exibida.
    
    Returns: 
        Uma matriz impressa de forma convencional.
    '''
    try:
        linhas = len(matriz); colunas = len(matriz[0])
    except:
        print(matriz)
    else:
        for i in range(linhas):
            print("|", end=" ")
            for j in range(colunas):
                print(f"{matriz[i][j]:^3}", end=" ")
            print("|")
        
        print('\n')