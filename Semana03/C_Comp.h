#ifndef C_Comp_H
#define C_Comp_H

#include <cmath>
#include <iostream>
using namespace std;

class C_Comp
{
    
    public:

    double mod, fase;
    double real, img;
    
    C_Comp(double real, double img);
    C_Comp Soma(double real, double img);
    

    C_Comp Subtracao(double real, double img);
    C_Comp Multipicacao(double real, double img);
    
    C_Comp Divisao(double mod, double fase);
    void Retangular_Polar();
    void Polar_Retangular();
    
    double *Polar_Retangular(double mod, double fas);
    
    void Print();
};

#endif
