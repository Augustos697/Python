'''Um professor quer sortear um dos seus quatro aluno para apagar o quadro.
 Fala um programa que ajude ele, lendo o nome deles e escrevendo onome do escolhido'''
import random
alunos = ["Maria","Pedro","Gustavo","Rafaela"]
print("Apague o quadro {}".format(random.choice(alunos)))