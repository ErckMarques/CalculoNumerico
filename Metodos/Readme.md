## Métodos Numéricos
Nesta pasta estão os arquivos .py que implementam os principais métodos numéricos utilizados em programação.
A seguir uma breve descrição de cada método dos arquivos

#### Descrição:
Métodos para o calculo de zeros de funções (arquivo metodos_funcoes.py).

    - Método da Bissecção:  Divide o intervalo inicial ao
      meio e verifica em qual dos dois subintervalos ocorre
      a mudança de sinal da função. 
      Repete o processo até encontrar uma aproximação da raiz.
     
      $x_{n+1} = \frac{a + b}{2}$

    - Método das Cordas ou Falsa Posição: Utiliza uma reta 
      que passa pelos pontos inicial e final do intervalo
      e verifica em qual ponto esta reta cruza o eixo x. 
      Repete o processo até encontrar uma aproximação da raiz.
      
      x_{n+1} = x_n - \frac{f(x_n)(b - x_n)}{f(b) - f(x_n)}

    - Método de Newton-Raphson ou Das Tangentes: Utiliza a
      tangente à curva da função em um ponto estimado para 
      encontrar a interseção com o eixo x. 
      Repete o processo até encontrar uma aproximação da raiz.
    
      x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}

    - Método das Secantes: Utiliza uma secante que passa
      pelos pontos finais dos dois últimos subintervalos e
      verifica em qual ponto esta secante cruza o eixo x.
      Repete o processo até encontrar uma aproximação da raiz.

      x_{n+1} = x_n - \frac{f(x_n)(x_{n-1} - x_n)}{f(x_{n-1}) - f(x_n)}


Métodos para trabalhar com Matrizes e Sistemas Lineares:
    
    - Eliminação de Gauss ou Escalonamento:
     Utiliza operações elementares nas linhas de uma
     matriz para triangularizar o sistema e encontrar a solução. 

        \begin{bmatrix}
        a_{11} & a_{12} & ... & a_{1n} & b_1 \\
        a_{21} & a_{22} & ... & a_{2n} & b_2 \\
        ... & ... & ... & ... & ... \\
        a_{n1} & a_{n2} & ... & a_{nn} & b_n \\
        \end{bmatrix}

        - Pivoteamento: Realiza uma reorganização das
          linhas da matriz durante a eliminação de Gauss,
          de modo a garantir que não ocorram divisões por 
          zero nos cálculos. Este procedimento pode ser 
          realizado de forma parcial (troca de linhas)
          ou de forma total (troca de colunas).

         \begin{bmatrix}
         a_{11} & a_{12} & ... & a_{1n} & b_1 \\
         0 & a_{22}^{(2)} & ... & a_{2n}^{(2)} & b_2^{(2)} \\
         ... & ... & ... & ... & ... \\
         0 & a_{n2}^{(2)} & ... & a_{nn}^{(2)} & b_n^{(2)} \\
         \end{bmatrix}



Obs: Apesar de visto no curso, preferimos não implementar o Método Iterativo Linear (MIL) ou de Ponto Fixo (IPF), pois os métodos: Secante e Tangentes são aprimoramentos de convergência do mesmo, isto é, o MIL é um método lento para o cálculo de raízes. 

-----------------------------------------------------------
Sugestões, dicas e informações:

Desenvolvedor: Erik Marques | 
E-Mail: erik.marques@ufpe.br | 
Assunto: Calculo Numerico
