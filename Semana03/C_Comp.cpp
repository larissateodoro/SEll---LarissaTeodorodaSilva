#include "C_Comp.h"


    C_Comp :: C_Comp(double real, double img){
        this->real = real;
        this->img = img;
        Retangular_Polar();
    }
    C_Comp C_Comp:: Soma(double real, double img){
        double i= real + this->real;
        double j = img + this->img;
        C_Comp tf(i,j);
        return tf;
    }
    
    C_Comp C_Comp:: Subtracao(double real, double img){
        double i= -real + this->real;
        double j = -img + this->img;
        C_Comp tf(i,j);
        return tf;
    }
    
    C_Comp C_Comp:: Multipicacao(double real, double img){
        double i= (real * this->real) - (img * this->img);
        double j = (real * this->img)+ (img * this->real);
        C_Comp tf(i,j);
        return tf;
    }
    
    C_Comp C_Comp:: Divisao(double mod, double fase){
        double *conv;
        double m = this->mod/mod;
        double f = this->fase - fase;
        conv = Polar_Retangular(m,f);
        C_Comp tf(conv[0],conv[1]);
        return tf;
    }
    void C_Comp:: Retangular_Polar(){
        this->mod = hypot(this->real, this->img);
        if(this->real == 0.0 && this->img != 0.0)
             this->fase = M_PI/2;
        else if (this->real != 0.0 )
        this->fase = atan(this->img/this->real);
        
        if((this->img<=0.0 && this->real<=0.0)||(this->img>=0.0 && this->real<0.0)){
            if(this->img==0.0 && this->real==0.0)
            this->fase = 0.0;
            else
                this->fase = this->fase + M_PI;
        }
    }
    void C_Comp:: Polar_Retangular(){
        this->real =  this->mod * cos(this->fase);
        this->img =  this->mod * sin(this->fase);

    }

    double* C_Comp::Polar_Retangular(double mod, double fas){
        double tf[2];
        double *Ponteiro;
        Ponteiro = tf;
        //Usuário passa os parâmetros em graus 
        tf[0] =  mod * cos(fas *M_PI/180.0);
        tf[1] =  mod * sin(fas *M_PI/180.0);
        
        return Ponteiro;
    }
    
    void C_Comp:: Print(){
        cout <<"Retangular:"<<this->real<<" "<<this->img <<"j"<<endl;
        cout <<"Polar:"<<this->mod <<"<"<<this->fase <<"rad"<<endl;
    }