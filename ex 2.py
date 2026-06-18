vDaVia = 100
vDaVia2 = 45
vDaVia3 = 50

print("================================")
print("  Em que via estava o carro?")
print("1 - Rua São alberto")
print("2 - Rua BR118")
print("3 - Rua Engenheiro Matheus")
print("================================")

via = input()

print("================================")
print("  Dgite a velocidade do carro")
print("================================")

speed = float(input())

match via:
    case "1":
        if speed <= vDaVia:
            infracao = "Sem infração"
        elif speed <= 110:
            infracao = "Infração leve"
        elif speed <= 120:
            infracao = "Infração media"
        else:
            infracao = "Infração grave"
        print(infracao)
    case "2":
        if speed <= vDaVia2:
            infracao = "Sem infração"
        elif speed <= 50:
            infracao = "Infração leve"
        elif speed <= 55:
            infracao = "Infração media"
        else:
            infracao = "Infração grave"
        print(infracao)
    case "3":
        if speed <= vDaVia3:
            infracao = "Sem infração"
        elif speed <= 55:
            infracao = "Infração leve"
        elif speed <= 60:
            infracao = "Infração media"
        else:
            infracao = "Infração grave"
        print(infracao)