palavra = input("Digite uma palavra a ser cifrada: ")
cifrada = palavra.lower().replace("a","i").replace("e","o").replace("i","u")
print(f"{cifrada}")