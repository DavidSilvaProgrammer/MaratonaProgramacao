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
