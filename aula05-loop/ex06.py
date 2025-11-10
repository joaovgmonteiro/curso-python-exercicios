''' 
Faça uma tabuada de multiplicar com um número escolhido pelo usuário;
1 x 0 = 
1 x 1 = 
1 x 2 =
...
'''
multi = 0
num = int(input("Digite o número que deseja ver a tabuada: "))
print(f"\n========== TABUADA DO {num} ==========")
for i in range(0,11):
    multi = i * num
    print(f"{num} * {i} = {multi}")
    
