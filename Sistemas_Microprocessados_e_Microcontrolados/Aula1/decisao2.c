#include <stdio.h>

int main(void) {
  float dinheiro = 40;
  float preco_cinema = 35;
  float preco_2_lanches = 20;

  if(dinheiro >= preco_cinema){
    printf("Hoje tem cinema!\n");
  } else if(dinheiro >= preco_2_lanches){
    printf("Hoje tem lanche!\n");
  } else {
    printf("Hoje tem FreeFire só mesmo!\n");
  }
  return 0;
}
