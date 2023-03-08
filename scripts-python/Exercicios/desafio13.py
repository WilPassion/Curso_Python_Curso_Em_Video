sal = float(input('Digite o seu salário: R$'))

desc = sal - (sal * 5 / 100)

print('Seu salário com desconto é R${:.2f}'.format(desc))
