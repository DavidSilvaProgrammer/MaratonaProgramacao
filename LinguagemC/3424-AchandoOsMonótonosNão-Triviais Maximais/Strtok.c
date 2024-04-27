#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "Hello, world! This is a test.";
    char delimiters[] = " ,.!"; // Delimitadores: espaço, vírgula, ponto e exclamação
    char *token = strtok(str, delimiters);

    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, delimiters);
    }

    return 0;
}


/*

A função strtok utiliza um ponteiro por algumas razões:

    Manutenção do estado interno:
        A função strtok precisa manter um estado interno para rastrear a posição atual dentro da 
        string que está sendo tokenizada.
        Um ponteiro é usado para armazenar essa posição, permitindo que strtok saiba onde continuar 
        sua busca pelo próximo token na próxima chamada.

    Iteração através da string:
        Como a função strtok é chamada várias vezes para obter os tokens subsequentes da string, um ponteiro é usado 
        para percorrer a string a cada chamada.
        O ponteiro é atualizado a cada chamada para apontar para a próxima posição na string após o token 
        encontrado anteriormente.

    Modificação da string original:
        strtok modifica a string original, substituindo os delimitadores encontrados pelo caractere nulo \0.
        Usar um ponteiro permite que strtok atualize diretamente a string original enquanto itera por ela.

Em resumo, o uso de ponteiros na função strtok é essencial para manter o estado interno da função, 
iterar através da string e modificar a string original conforme necessário para dividir a string em tokens.

***************************



A função strtok em C recebe dois parâmetros:

    String a ser tokenizada: Este é um ponteiro para uma string que será dividida em tokens. 
    A primeira vez que strtok é chamado, esta string é fornecida como o primeiro argumento. 
    Nas chamadas subsequentes, este argumento deve ser NULL, indicando que a função deve 
    continuar a tokenização da mesma string a partir de onde parou.

    String de delimitadores: Este é um ponteiro para uma string contendo os caracteres que serão 
    usados como delimitadores para dividir a string em tokens. Cada caractere na string de
    delimitadores será considerado um delimitador. Quando strtok encontra um desses delimitadores 
    na string a ser tokenizada, ele divide a string e retorna o token. Se vários delimitadores 
    aparecerem consecutivamente, eles serão tratados como um único delimitador.


Por exemplo, se quisermos dividir a string "Hello, world! This is a test." com os delimitadores " ,.!", 
chamamos strtok da seguinte forma:

char str[] = "Hello, world! This is a test.";
char delimiters[] = " ,.!";
char *token = strtok(str, delimiters);

A função strtok em C recebe dois parâmetros:

    String a ser tokenizada: Este é um ponteiro para uma string que será dividida em tokens. A primeira vez que strtok é chamado, esta string é fornecida como o primeiro argumento. Nas chamadas subsequentes, este argumento deve ser NULL, indicando que a função deve continuar a tokenização da mesma string a partir de onde parou.

    String de delimitadores: Este é um ponteiro para uma string contendo os caracteres que serão usados como delimitadores para dividir a string em tokens. Cada caractere na string de delimitadores será considerado um delimitador. Quando strtok encontra um desses delimitadores na string a ser tokenizada, ele divide a string e retorna o token. Se vários delimitadores aparecerem consecutivamente, eles serão tratados como um único delimitador.

Por exemplo, se quisermos dividir a string "Hello, world! This is a test." com os delimitadores " ,.!", chamamos strtok da seguinte forma:

c

char str[] = "Hello, world! This is a test.";
char delimiters[] = " ,.!";
char *token = strtok(str, delimiters);

Neste exemplo, a string "Hello, world! This is a test." será dividida 
em tokens com base nos delimitadores fornecidos.

 */
