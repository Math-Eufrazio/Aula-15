precos = ["23.44", "-343.44", "-3333.33", "50.00", "43.44"]
pbarato = []
pcaro = []
neg = []

print(f"Lista original: {precos}")

for produto_str in precos:
    preco = float(produto_str)
    if preco < 0:
        neg.append(preco)
    else:
        if preco < 50:
            pbarato.append(preco)
        else:
            pcaro.append(preco)

print(f"Negativos (erros): {neg}")
print(f"Preços Baratos (abaixo de 50): {pbarato}")
print(f"Preços Caros (50 ou mais): {pcaro}")