# ===============================================================
# COMO ESTE PROGRAMA FUNCIONA — explicado na ordem em que executa
# ===============================================================
# Este arquivo é comentado "Ato" por "Ato", seguindo a ORDEM DE
# EXECUÇÃO real do programa (não apenas a ordem das linhas no
# arquivo — aqui elas coincidem, pois o programa é sequencial,
# sem funções). O Python lê e executa este script de cima para
# baixo, uma instrução de cada vez.
#
# Resumo da peça inteira:
#   Ato 0 -> Exibe o cabeçalho da campanha
#   Ato 1 -> Pergunta o tipo de imóvel
#   Ato 2 -> Pergunta o consumo mensal de água
#   Ato 3 -> Classifica o consumo com base nas regras de negócio
#   Ato 4 -> Exibe o resultado final ao morador
# ===============================================================

# ---------------------------------------------------------------
# Ato 0: Exibição do cabeçalho
# ---------------------------------------------------------------
# print() mostra um texto na tela. Aqui é só a "moldura" visual
# do programa, para o morador saber que está usando o sistema
# da campanha de conscientização.
print("=======================================================")
print("   💧 CAMPANHA DE CONSCIENTIZAÇÃO - CONSUMO DE ÁGUA 💧")
print("=======================================================")

# ---------------------------------------------------------------
# Ato 1: Solicitação do tipo de imóvel
# ---------------------------------------------------------------
# input() pausa o programa e espera o usuário digitar algo no
# teclado. O que for digitado chega sempre como texto (string).
# .lower() converte tudo para minúsculas, para que "Casa",
# "CASA" ou "casa" sejam tratados da mesma forma mais adiante.
tipo_imovel = input("🏠 Informe o tipo de imóvel (comercial, casa ou apartamento): ")
tipo_imovel = tipo_imovel.lower()

# ---------------------------------------------------------------
# Ato 2: Solicitação do consumo mensal de água
# ---------------------------------------------------------------
# float() converte o texto digitado em um número decimal, para
# que seja possível fazer comparações (<, <=, etc.) mais adiante.
consumo_mensal = float(input("🚰 Informe o consumo mensal de água (em m³): "))

# ---------------------------------------------------------------
# Ato 3: Classificação do consumo (regras de negócio)
# ---------------------------------------------------------------
# A estrutura if/elif/else testa as condições NA ORDEM em que
# aparecem e executa apenas o primeiro bloco verdadeiro. Por isso
# a ordem das condições importa:
#
#   1º) Se o imóvel é comercial, a regra comercial já se aplica,
#       independente do consumo.
#   2º) Se for apartamento com consumo abaixo de 10 m³, é o caso
#       de consumo econômico.
#   3º) Se for apartamento (com qualquer consumo que não caiu na
#       regra anterior) OU casa com consumo até 25 m³, é consumo
#       moderado.
#   4º) Qualquer outro caso restante (ex: casa acima de 25 m³) é
#       tratado como consumo excessivo.
if tipo_imovel == "comercial":
    mensagem = "🏢 Tarifa comercial aplicada – consulte o plano corporativo."
elif tipo_imovel == "apartamento" and consumo_mensal < 10:
    mensagem = "🌱 Consumo econômico – excelente controle de água!"
elif tipo_imovel == "apartamento" or (tipo_imovel == "casa" and consumo_mensal <= 25):
    mensagem = "💧 Consumo moderado – dentro do padrão residencial."
else:
    mensagem = "🚨 Consumo excessivo – adote medidas de economia e verifique vazamentos."

# ---------------------------------------------------------------
# Ato 4: Exibição do resultado final
# ---------------------------------------------------------------
# Por fim, o programa mostra um resumo com os dados informados
# pelo usuário e a mensagem de classificação definida no Ato 3.
print("-------------------------------------------------------")
print("📋 Tipo de imóvel :", tipo_imovel.capitalize())
print("📊 Consumo mensal :", consumo_mensal, "m³")
print("📢 Resultado      :", mensagem)
print("-------------------------------------------------------")

# ===============================================================
# Para fixar:
#   - Por que .lower() é usado logo após o input() do tipo de
#     imóvel, e não depois?
#   - O que aconteceria se a condição do "apartamento" (Ato 3)
#     viesse DEPOIS da condição da "casa"? O resultado mudaria
#     para algum caso de teste?
#   - O que acontece se o usuário digitar um texto (ex: "dez")
#     no lugar de um número no Ato 2? (dica: tente executar e
#     observe a mensagem de erro do Python)
# ===============================================================
