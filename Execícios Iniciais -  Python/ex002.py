
x = int(input("Digite um número para X: "))
y = int(input("Digite um valor para Y: "))
z = int(input("Digite um valor para Z: "))

if x > y and x > z:
    print('A variavel com o maior valor é X, ou seja {}'.format(x))

elif y > x and y > z:
    print('A variavel com o maior valor é Y, ou seja {}'.format(y))

else:
    print('A variavel com o maior valor é Z, ou seja'.fotmat (z))
print('Fim')