
x = int(input("Digite um número para X: "))
y = int(input("Digite um valor para Y: "))
z = int(input("Digite um valor para Z: "))

divix = x % 2
diviy = y % 2
diviz = z % 2

if divix == 0:
    print(' o valor da variavel X {} é par'.format(x))
if diviy == 0:
    print('{} é par'.format(y))
if diviz == 0:
    print('{} é par'.format(z))