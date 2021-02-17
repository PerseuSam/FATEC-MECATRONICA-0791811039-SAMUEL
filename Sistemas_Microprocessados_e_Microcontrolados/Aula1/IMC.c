#include <stdio.h>

int main(void){
    int altura;
    altura = 151;
    printf("O valor da minha altura é: %i cm\n", altura);
    //Variavel para armazenar um número real
    float peso;//Número real de 32 bits
    double imc;//Número real de 64 bits
    peso = 105.47;
    float altura_metros;
    //Para transformar em float
    altura_metros = altura/100.0;
    //ou altura_metros = (float)altura/100;
    imc = peso/(altura_metros * altura_metros);
    printf("Valor do IMC para altura %i cm e peso %f kg: %lf \n", altura, peso, imc);
    return 0;
}
