#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int copyPaste(char *oldArq,char *newArq){

	FILE *CtrlC,*CtrlV;
	CtrlC = fopen(oldArq , "r");
	CtrlV = fopen(newArq , "w"); 

	int ch;
  	 while ((ch = getc (CtrlC )) != EOF){
       putc (ch, CtrlV);
      	}
      	fclose(CtrlC);
      	fclose(CtrlV);
	}

int main(int argc, char const *argv[])
/*Precisa dar um nome para o arquivo que vai ser copiado.
Exemplo: 
prog02 /home/larissa/Documentos/Semana03/prog01.cpp /home/larissa/Documentos/novo.cpp
*/
{
    char *str, *str2;
    int tamanho = 0;
    str = malloc ((tamanho+1) * sizeof (char));
    str2 = malloc ((tamanho+1) * sizeof (char));
    
    
        tamanho = strlen(argv[1]);
        str = realloc (str, (tamanho+1) * sizeof (char));
        strcat(str, argv[1]);
    
      tamanho = strlen(argv[2]);
        str2 = realloc (str2, (tamanho+1) * sizeof (char));
        strcat(str2, argv[2]);

    printf("\npr: %s\n",str);
    printf("\npr: %s\n",str2);
    copyPaste(str, str2);
    free(str);
    free(str2);
    return 0;
}

