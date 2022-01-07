'''O mesmo prfessor do desafio anterior quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'''
import random
alunos = ["Maria",'Pedro','Gustavo','Rafaela']
random.shuffle(alunos)
print(' A ordem da apresentação do trabalho vai ser a seguinte:{}'.format(alunos))


