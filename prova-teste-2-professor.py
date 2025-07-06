import json

dados_prova = { }
todas_questoes=[ ]
alternativas = { }


titulo_p = input("Escreva o Título da Prova: ")
dados_prova["Título"] = titulo_p
print(dados_prova)
quantidade_questoes = int(input("Escreva quantas questões você deseja fazer: "))



for i in range(quantidade_questoes):
    tipo = input("A questão é 'Objetiva' ou 'Subjetiva'? ")
    questao = input(f"Escreva a {i+1}º questão: ")
    dic_questao = {"tipo": tipo,
                   "questao": questao,
                }
    
    if tipo=="Objetiva":
        a = input("Alternativa A:")
        b = input("Alternativa B:")
        c = input("Alternativa C:")
        d = input("Alternativa D:")
        e = input("Alternativa E:")

        alternativas = {"A": a,
                        "B": b,
                        "C": c,
                        "D": d,
                        "E": e
                        }
        
        gabarito= input("Escreva o gabarito da questão: ")
        dic_questao["gabarito"] = gabarito
        dic_questao["alternativas"] = alternativas
        
    todas_questoes.append(dic_questao)
    
dados_prova["questoes"] = todas_questoes

with open('prova 2.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados_prova, arquivo, ensure_ascii=False, indent=4)


