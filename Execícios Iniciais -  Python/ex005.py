nome = input("Informe o Nome do aluno: ")
print("Òtimo, qual a série de {}".format(nome))
serie = input("Série: ")

n1 = float(input("qual a nota da 1ª avaliação:"))
n2 = float(input("qual a nota da 2ª avaliação:"))
n3 = float(input("qual a nota da 3ª avaliação:"))

media = (n1 + n2 + n3) / 3
print("O aluno {}, da {}, obteve a média {} no I Trimestre.".format(nome, serie, media))