'''
Match case 
'''

fruta = input("escolha a fruta: ").lower()

match fruta:
    case "maça":
        print("É uma maça.")
    case "banana":
        print("É uma banana.")
    case _:
        print("escolha errada - é outra fruta")


