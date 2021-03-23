#include <iostream>
#include "C_Comp.h"
using namespace std;


int main(){
    C_Comp A(2.0,1.0);
    C_Comp B(1.0,3.0);
    
    C_Comp E = A.Soma(1.0,5.0);
    E.Print();
    C_Comp F = A.Subtracao(1.0,5.0);
    F.Print();
    C_Comp G = B.Multipicacao(1.0,5.0);
    G.Print();
    C_Comp H = B.Divisao(1.0,5.0);
    H.Print();

    
    
    return 0;
}