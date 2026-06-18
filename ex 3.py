print("*======================================================*")
print("          Verificador de Validade - Supermercado        ")
print("*======================================================*")

nome_produto = input("Nome do produto: ")
dpven = int(input(f"Quantos dias faltam para {nome_produto} vencer? "))


if dpven < 0:
    status = "Vencido"
elif dpven <= 3:
    status = "Critico"
elif dpven <= 10:
    status = "Alerta"
else:
    status = "Normal"


match status:
    case "Vencido":
        destino = "DESCARTAR IMEDIATAMENTE"
        acao = "Retirar da área de circulação e registrar perda."

    case "Critico":
        destino = "PROMOÇÃO RELÂMPAGO"
        acao = "Colocar etiqueta de 50% de desconto e expor na ilha central."

    case "Alerta":
        destino = "PRATELEIRA COMUM"
        acao = "Aplicar a regra PVPS (Primeiro que Vence, Primeiro que Sai) na frente."

    case "Normal":
        destino = "PRATELEIRA COMUM / ESTOQUE"
        acao = "Produto seguro. Pode ser armazenado ou colocado ao fundo da prateleira."

    case _:
        destino = "Erro de análise"
        acao = "Verificar dados manualmente."

print("\n*------------------------------------------------------*")
print(f" PRODUTO: {nome_produto}")
print(f" DESTINO: {destino}")
print(f" AÇÃO: {acao}")
print("*------------------------------------------------------*")