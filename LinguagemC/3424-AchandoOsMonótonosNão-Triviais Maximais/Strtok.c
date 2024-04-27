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


    */
