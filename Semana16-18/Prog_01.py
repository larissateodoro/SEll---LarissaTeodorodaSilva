print("\n Exercicio 1 - Letra a)")
F = 1 #F(k = 0) = 1
for j in range(1,21,1):
    print(F)
    F = F +2#F(k) = F(k-1)+2

print("\n Exercicio 1 - Letra b)")
F = 0 
for j in range(1,21,1):
    F = F +j #F(k) = F(k-1)+j
    print(F)

print("\n Exercicio 1 - Letra c)")
F = 0 
for j in range(1,21,1):
    F = j*j #F(k) = F(k-1)+j
    print(F)