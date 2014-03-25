class NumeroFeliz(object):
    """Para saber se um número é feliz, você deve obter o quadrado de cada dígito deste número,
     em seguida você faz a soma desses resultados.
     A seguir o mesmo procedimento deve ser feito com o valor resultante desta soma.
     Se ao repetir o procedimento diversas vezes obtivermos o valor 1, o número inicial é considerado feliz.

    Tomamos o 7, que é um número feliz:
    7² = 49
    4² + 9² = 97
    9² + 7² = 130
    1² + 3² + 0² = 10
    1² + 0² = 1 """

    def retorna(self, numero):
        feliz = 0
        for alg in numero:
            feliz += int(alg) **2

        if feliz == 1:
            return "numero feliz"
        elif feliz < 10:
            return "numero infeliz: " + str(feliz)
        else:
            obj = NumeroFeliz()
            return obj.retorna(str(feliz))
