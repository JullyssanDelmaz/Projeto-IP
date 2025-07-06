import json
with open('prova 2.json', 'r', encoding='utf-8') as arquivo:
    dados_prova = json.load(arquivo)

acertos = 0
nome_aluno = input("Escreva seu nome e sobrenome: ")
serie_aluno = int(input("Escreva sua série: "))
turma_aluno = input("Escreva sua turma: ")
respostas = []
erros = []

for i, q in enumerate(dados_prova["questoes"]):
    print(f"Questão {i+1}: {q['questao']}")
    if "alternativas" in q:
        for letra, texto in q["alternativas"].items():
            print(f"{letra}) {texto}")

    gabarito_aluno = input("Sua Resposta: ")
    respostas.append({
        "questao": q["questao"],
        "gabarito_aluno": gabarito_aluno
        })
    if gabarito_aluno.upper() == q["gabarito"].upper():
        acertos+=1
    else:
        erros.append(i+1)
        
        
        
print(f"Você acertou {acertos} questões.")
if erros:
    print(f"Você errou as seguintes questões: {erros}")
else:
    print("Você não errou nenhuma questão.")

nota = (acertos/ len(dados_prova["questoes"]))*10
print(f"Sua nota final é {nota: .1f}.")
