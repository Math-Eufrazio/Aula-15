cPro = [67 ,67767 ,768944, 222345, 11123]
eCad = []

for codigo in cPro:
    tamanho = len(str(codigo))
    if tamanho < 5:
        eCad.append(codigo)
    print(f"{eCad}")