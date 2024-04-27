#include <stdio.h>
#include <string.h>

int main() {
    char str[30];
    char* token;
    int n,tam,cont=0;
    scanf("%d",&n);
    scanf("%s",str);
    token = strtok(str,"b");
    while(token!=NULL){
        tam= strlen(token);
        if(tam >1){
            cont+=tam;
        }
        token=strtok(NULL, "b");
    }
    printf("%d\n",cont);
    
    return 0;
}
