'''Escreva um progrma que pergunte a quanitdade de Km percorridos por um carro alugado
 e a quantidade de dias pelos quais ele foi alugado.
Calcule  o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado'''

dia = int(input('Quantos dias passou com o carro ?'))
km = float(input('Quantos Km rodados ?'))
cusd = dia*60
cuskm = km*0.15
res = cusd + cuskm
print('Com {} dias e {}Km percorridos vc vai precisar pagar {}'.format(dia, km, res))