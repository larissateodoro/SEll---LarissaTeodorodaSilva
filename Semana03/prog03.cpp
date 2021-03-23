#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int i, *a, *b, *c, *p, *fr, *to, *sp, n, n1, n2;
    ofstream out("Resposta.txt");
    n = atoi(argv[1]);
    n1 = n + 1;
    n2 = n + 2;
    a = (int *)malloc((n + 3) * sizeof(int));
    b = (int *)malloc((n + 3) * sizeof(int));
    c = (int *)malloc((n + 3) * sizeof(int));
     // cria os vetores a, b e c
    a[0] = 1;
    b[0] = c[0] = n1;
    a[n1] = b[n1] = c[n1] = n1;
    a[n2] = 1;
    b[n2] = 2;
    c[n2] = 3;
    for (i = 1; i < n1; i++)
    { // coloca os discos no vetor a
        a[i] = i;
        b[i] = c[i] = 0;
    }
    fr = a; // Vetor a é o poste de origem
    if (n & 1)
    {
        to = c;
        sp = b;
    } // verifica se n é par
    else
    {
        to = b;
        sp = c;
    }
    while (c[0] > 1)
    {
     i = fr[fr[0]++];
        cout << "Move o disco " << i  << " de " << fr[n2] << " para " << to[n2] << endl;
        out << "Retira o disco " << i << " da torre " << fr[n2] << " Coloca na torre "<< to [n2]<<endl;
        p = sp;
        if ((to[--to[0]] = i) & 1)
        { // testa se o disco a ser retirado é par
            sp = to;
            if (fr[fr[0]] > p[p[0]])
            {
                to = fr;
                fr = p;
            } // testa o movimento que vai fazer
            else
                to = p; 
        }
        else
        {
            sp = fr;
            fr = p;
        }
    }
    out.close();
return 0;
}