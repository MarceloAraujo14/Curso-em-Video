def notas(*num, sit=False):
    """
    >> Indica o total de notas inseridas, indica a maior e menor nota, a média e situação da turma.
    :param num: notas a serem inseridas (sem limite estabelecido)
    :param sit: (opcional) True para mostrar a situação da turma.  Default = False
    :return: sem retorno.
    """

    global turma, nota
    soma = 0
    nota = []
    turma = {}


    turma["total"] = len(num)

    for i in range(len(num)):
        if i == 0:
            nota.append(num[i])
            turma["maior"] = num[i]
            turma["menor"] = num[i]
            soma += num[i]
        else:
            nota.append(num[i])
            if turma["maior"] < num[i]:
                turma["maior"] = num[i]
            if turma["menor"] > num[i]:
                turma["menor"] = num[i]
            soma += num[i]


    turma["media"] = soma / len(num)

    if turma["media"] < 5:
        turma["situação"] = 'ruim'
    elif turma["media"] < 6:
        turma["situação"] = 'razoável'
    elif turma["media"] < 8:
        turma["situação"] = 'boa'
    elif turma["media"] > 10:
        turma["situação"] = 'muito boa'

    if sit == False:
        del turma["situação"]

    return turma

resp = notas(7, 5, 0, 2, 8, 8, 6, sit=True)
print(resp)