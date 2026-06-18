# Lista de usuários: [Nome, E-mail, Ano de Nascimento]
inscricoes = [
    ["Mateus", "mateus@email.com", 2005],
    ["Ana", "ana_valida@gmail.com", 1998],
    ["Lucas", "lucas_sem_arroba.com", 2000],  # Sem @
    ["Beatriz", "bia@outlook.com", 2012],  # Menor de idade
]

ec = []

for usuario in inscricoes:
    nome = usuario[0]
    email = usuario[1]
    ano_nascimento = usuario[2]

    idade = 2026 - ano_nascimento


    if "@" in email and idade >= 18:
        ec.append(email)


print("E-mails que vão receber a campanha:")
print(ec)