print("*==================================================================================================*")
print("            Bem vindo ao sistema de triagem do Hospital Matheus Eufrazio")
print("Digite os dados do paciente que está atendendo abaixo para analisarmos e darmos um pré diagnostico ")
print("*===================================================================================================*")

nome = input("Nome do Paciente: ")
temperatura = float(input("Temperatura do paciente: "))
idade = float(input("Idade do Paciente: "))
bpm = int(input("Batimento do paciente: "))
danoVisivel = input("Possui machucado visivel Sim ou Não: ").strip().capitalize()

pdp = 0


if idade >= 65:
    clas = "Idoso"
elif idade >= 18:
    clas = "Adulto"
elif idade >= 12:
    clas = "Adolescente"
elif idade >= 2:
    clas = "Criança"
else:
    clas = "Bebe"


match clas:
    case "Adulto" | "Idoso" | "Adolescente":
        if temperatura >= 37.8:
            pdp += 2
            febre = "Com febre"
        elif temperatura <= 35.5:
            febre = "Temperatura muito baixa"
            pdp += 3
        else:
            febre = "Temperatura corporal normal"

        if bpm <= 50:
            batimentos = "Batimentos baixos"
            pdp += 2
        elif bpm >= 120:
            batimentos = "Batimentos altos"
            pdp += 2
        else:
            batimentos = "Batimentos normais"

    case "Criança" | "Bebe":

        if temperatura >= 37.8:
            pdp += 3
            febre = "Com febre"
        elif temperatura <= 35.5:
            febre = "Temperatura muito baixa"
            pdp += 3
        else:
            febre = "Temperatura corporal normal"


        if bpm <= 60:
            batimentos = "Batimentos baixos"
            pdp += 2
        elif bpm >= 140:
            batimentos = "Batimentos altos"
            pdp += 2
        else:
            batimentos = "Batimentos normais"

    case _:
        batimentos = "Não classificado"
        febre = "Não classificado"


if danoVisivel == "Sim":
    dmg = "Dano visivel"
    pdp += 5
else:
    dmg = "Nenhum Dano visivel"



print("\n*======================================*")
print(f"Paciente: {nome} ({clas})")
print(f"Status: {febre} | {batimentos} | {dmg}")
print(f"Pontuação de Risco (PDP): {pdp}/5")
print("*======================================*")