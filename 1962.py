ano_atual = 2015
vezes = int(input())

while vezes > 0:
    ano_passou = int(input())

    ano_ocorreu = max(ano_atual,ano_passou) - min(ano_atual,ano_passou)

    if ano_passou > ano_atual:
        print((ano_ocorreu+1),"A.C.")

    if ano_passou < ano_atual:
        print(ano_ocorreu,"D.C.")

    if ano_passou == ano_atual:
        print("1 A.C.")

    vezes = vezes - 1
