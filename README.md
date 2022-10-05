# Equipe

Gustavo Bosco e Igor Tomasi.

Itens:

Saco de dormir 

Peso := 15 |
Pontos := 15

Corda

Peso := 3 |
Pontos := 10

Canivete

Peso := 2 |
Pontos := 10

Tocha

Peso := 5 |
Pontos := 5

Garrafa

Peso := 9 |
Pontos := 8

Comida

Peso := 20 |
Pontos := 17

Dica 1: Você basicamente precisará alterar a função cal_pop_fitness - aqui você deverá calcular a soma dos pontos de cada cromossomo. E eliminar as pontuações cujos pesos sejam MAIORES que 30kg (para isso, você pode fazer com que a pontuação seja um número negativo bem pequeno, como -9999999, nesses casos).

Dica 2: Lembre-se que você vai ter que gerar um conjunto populacional em que os valores dos genes são 0 ou 1 (item ausente ou presente na mochila). Para isso você também precisa alterar a forma de gerar a população inicial, no main.py (dica, veja o método randint da biblioteca numpy).

Dica 3: Você também precisará alterar a função mutation. A diferença aqui é que você não deve somar um valor aleatório. Simplesmente faça abs(valor_atual - 1), na hora de calcular a variação.

Dica 4: Experimente aumentar o número de gerações e mexer no número de soluções por população (por exemplo 100 gerações, 10 soluções por população). Veja quantas gerações você precisa para obter o valor máximo de pontos.
