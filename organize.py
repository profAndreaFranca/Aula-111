import os
import shutil

#1 - crie uma variável que receba o caminho de uma pasta e exiba no terminal se ela existe ou não
pasta = input("caminho da pasta")

if os.path.exists(pasta):
    print("a pasta existe")

else:
    print("a pasta não existe")

#2 - crie uma variável que receba um arquivo, depois separe o caminho da extensão e exiba-os no terminal
arquivo = input ("caminho da pasta")

path = os.path.splitext(arquivo)
print(path)


#3 - Verifique a pasta teste existe, caso contrário, crie a pasta
file  = input("caminho da pasta")
file2 = file+"\teste"

if os.path.exists(file2):
    print("A pasta existe")

else:
    os.mkdir(file2)
    


#4 - exiba no terminal e diretório de trabalho atual

print(os.getcwd())

