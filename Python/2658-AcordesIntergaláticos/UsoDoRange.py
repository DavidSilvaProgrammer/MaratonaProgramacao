O range em Python pode receber até três parâmetros. Aqui está a sintaxe do range:

python

range(start, stop, step)

    start: O valor inicial da sequência (opcional). Se não for especificado, o padrão é 0.
    stop: O valor final da sequência (obrigatório). O range vai até stop - 1.
    step: O tamanho do passo entre os números (opcional). Se não for especificado, o padrão é 1.

Se apenas um argumento for passado, ele será tratado como stop, e os valores padrão de start e step serão utilizados.

Por exemplo:

    range(5) cria uma sequência de 0 a 4.
    range(1, 10) cria uma sequência de 1 a 9.
    range(1, 10, 2) cria uma sequência de 1 a 9, com passos de 2 em 2.

Você pode usar o range para gerar sequências de números em um loop, em uma compreensão de lista, 
ou em qualquer outro lugar onde uma sequência de números seja necessária.
