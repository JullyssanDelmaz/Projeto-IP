import json
import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Projeto Jullyssan Delmaz IP 2025.1")
janela.geometry("800x600")

# Frame de início
frame_inicio = tk.Frame(janela)
frame_inicio.pack(pady=20)

frame_professor = tk.Frame(janela)
frame_professor.pack(pady=20)
frame_professor.pack_forget()

frame_aluno = tk.Frame(janela)
frame_aluno.pack(pady=20)
frame_aluno.pack_forget()

frame_dados_professor = tk.Frame(janela)
frame_dados_professor.pack(pady=20)
frame_dados_professor.pack_forget()

frame_redigir_prova = tk.Frame(janela)
frame_redigir_prova.pack(pady=20)
frame_redigir_prova.pack_forget()

frame_questao_professor = tk.Frame(janela)
frame_questao_professor.pack(pady=20, fill="both", expand=True)
frame_questao_professor.pack_forget()

frame_questao_aluno = tk.Frame(janela)
frame_questao_aluno.pack(pady=20, fill="both", expand=True)
frame_questao_aluno.pack_forget()  # começa escondido

frame_resultado_final = tk.Frame(janela)
frame_resultado_final.pack(pady=20)
frame_resultado_final.pack_forget()

frame_correcao_login = tk.Frame(janela)
frame_correcao_login.pack(pady=20)
frame_correcao_login.pack_forget()

frame_correcao_provas = tk.Frame(janela)
frame_correcao_provas.pack(pady=20)
frame_correcao_provas.pack_forget()



# Tela inicial
botao_professor = tk.Button(frame_inicio, text="PROFESSOR", font=("Arial", 10), bg="red", fg="white")
botao_professor.pack(side="left", padx=10, pady=20)
botao_aluno = tk.Button(frame_inicio, text="ALUNO", font=("Arial", 10), bg="green", fg="white")
botao_aluno.pack(side="left", padx=10, pady=20)
botao_correcao = tk.Button(frame_inicio, text="CORREÇÃO", font=("arial", 10), bg="blue", fg="white")
botao_correcao.pack(side="left", padx=10, pady=20)
botao_voltar_inicio = tk.Button(janela, text="Tela Inicial", font=("Arial", 12), bg="black", fg="white", command=lambda: voltar_tela_inicial())
botao_voltar_inicio.pack_forget()


# Variáveis para provas e seleção
todas_as_provas = {}
prova_selecionada = tk.StringVar(value="Selecione uma prova")
dados_prova = {}
questoes_subjetivas = {}

tk.Label(frame_aluno, text="Selecione a Prova:", font=("Arial", 12), anchor="w").pack(fill="x", padx=20, pady=2)
menu_provas = tk.OptionMenu(frame_aluno, prova_selecionada, "")
menu_provas.config(width=30, font=("Arial", 12))
menu_provas.pack(fill="x", padx=20, pady=5)

# Função para atualizar o menu das provas na tela do aluno
def atualizar_menu_provas():
    global todas_as_provas

    try:
        with open("provas.json", "r", encoding="utf-8") as f:
            todas_as_provas = json.load(f)
    except FileNotFoundError:
        todas_as_provas = {}

    opcoes = list(todas_as_provas.keys())
    if not opcoes:
        opcoes = ["Nenhuma prova disponível"]
    prova_selecionada.set(opcoes[0])

    menu = menu_provas["menu"]
    menu.delete(0, "end")
    for opcao in opcoes:
        menu.add_command(label=opcao, command=tk._setit(prova_selecionada, opcao))
          



        
# MODOS
def modo_professor():
    frame_inicio.pack_forget()
    frame_professor.pack(pady=20)

def modo_aluno():
    frame_inicio.pack_forget()
    atualizar_menu_provas()
    frame_aluno.pack(pady=20)

def modo_correcao():
    frame_inicio.pack_forget()
    frame_correcao_login.pack(pady=20)

    
botao_professor.config(command=modo_professor)
botao_aluno.config(command=modo_aluno)
botao_correcao.config(command=modo_correcao)


# Cabeçalho com os dados do professor
tk.Label(frame_professor, text="Nome Completo:", font=("Arial", 12)).pack(anchor="w", pady=5, padx=10)
entrada_nome_professor = tk.Entry(frame_professor, font=("Arial", 12), width=40)
entrada_nome_professor.pack(pady=5, padx=10)

tk.Label(frame_professor, text="Matrícula:", font=("Arial", 12)).pack(anchor="w", pady=5, padx=10)
entrada_matricula = tk.Entry(frame_professor, font=("Arial", 12), width=40)
entrada_matricula.pack(pady=5, padx=10)

tk.Label(frame_professor, text="Disciplina:", font=("Arial", 12)).pack(anchor="w", pady=5, padx=10)
entrada_disciplina = tk.Entry(frame_professor, font=("Arial", 12), width=40)
entrada_disciplina.pack(pady=5, padx=10)

tk.Label(frame_professor, text="Senha", font=("Arial", 12)).pack(anchor="w", pady=5, padx=10)
entrada_senha_professor = tk.Entry(frame_professor, font=("Arial", 12), width=40, show="*")
entrada_senha_professor.pack(pady=5, padx=10)

botao_voltar_inicio = tk.Button(frame_professor, text="Tela Inicial", font=("Arial", 12), bg="black", fg="white", command=lambda:voltar_tela_inicial())
botao_voltar_inicio.pack(pady=10)

botao_seguinte = tk.Button(frame_professor, text="Iniciar Prova", font=("Arial", 12), bg="Red", fg="white", command=lambda:dados_professor())
botao_seguinte.pack(pady=10)

# Cabeçalho Professor
info_professor={}

def dados_professor():
    nome_professor= entrada_nome_professor.get().strip()
    matricula= entrada_matricula.get().strip()
    disciplina= entrada_disciplina.get().strip()
    senha_professor=entrada_senha_professor.get().strip()
    

    if not nome_professor or not matricula or not senha_professor or not disciplina :
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return
    
    # Salva as informações do professor
    info_professor['nome'] = nome_professor
    info_professor['matricula'] = matricula 
    info_professor['disciplina'] = disciplina
    info_professor['senha'] = senha_professor


    try:
        with open("cadastro_professores.json", "r", encoding="utf-8") as f:
            professores = json.load(f)
    except FileNotFoundError:
        professores=[]

    professores.append(info_professor.copy())

    with open("cadastro_professores.json", "w", encoding="utf-8") as f:
        json.dump(professores, f, ensure_ascii=False, indent=4)
        
    frame_professor.pack_forget()
    frame_questao_professor.pack(pady=20)


#Cabeçalho correção-login
tk.Label(frame_correcao_login, text="Nome Completo:", font=("Arial", 12)).pack(anchor="w", pady=5, padx=10)
entrada_nome_professor_login = tk.Entry(frame_correcao_login, font=("Arial", 12), width=40)
entrada_nome_professor_login.pack(pady=5, padx=10)

tk.Label(frame_correcao_login, text="Matrícula:", font=("Arial", 12)).pack(anchor="w", pady=5, padx=10)
entrada_matricula_login = tk.Entry(frame_correcao_login, font=("Arial", 12), width=40)
entrada_matricula_login.pack(pady=5, padx=10)

tk.Label(frame_correcao_login, text="Senha", font=("Arial", 12)).pack(anchor="w", pady=5, padx=10)
entrada_senha_professor_login = tk.Entry(frame_correcao_login, font=("Arial", 12), width=40, show="*")
entrada_senha_professor_login.pack(pady=5, padx=10)

botao_iniciar_correcao = tk.Button(frame_correcao_login,text="ENTRAR", font=("Arial", 12),bg="green", fg="white",command=lambda: dados_professor_login())
botao_iniciar_correcao.pack(pady=15)

botao_voltar_inicio = tk.Button(frame_correcao_login, text="Tela Inicial", font=("Arial", 12), bg="black", fg="white", command=lambda: voltar_tela_inicial())
botao_voltar_inicio.pack(pady=15)

def dados_professor_login():
    
    nome_professor_login= entrada_nome_professor_login.get().strip()
    matricula_login = entrada_matricula_login.get().strip()
    senha_professor_login=entrada_senha_professor_login.get().strip()
    

    if not nome_professor_login or not matricula_login or not senha_professor_login :
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return
           
    try:
        with open("cadastro_professores.json", "r", encoding="utf-8") as f:
            professores_cadastrados = json.load(f)
    except FileNotFoundError:
        messagebox.showwarning("Aviso", "Nenhum professor cadastrado!")
        return
    for prof in professores_cadastrados:
        if (prof['nome'] == nome_professor_login and
            prof['matricula'] == matricula_login and
            prof['senha'] == senha_professor_login):            
            global info_professor
            info_professor = prof

            frame_correcao_login.pack_forget()
            frame_correcao_provas.pack(pady=20)
            
            return
    messagebox.showerror("Erro", "Dados incorretos ou professor não cadastrado.")
               
    

# Redigir Prova

tipo_questao_var = tk.StringVar(value="Objetiva")
todas_questoes=[ ]
alternativas_vars = {}

label_questao_professor = tk.Label(frame_questao_professor, text="Título da Prova:", font=("Arial", 12), justify="left")
label_questao_professor.pack(anchor="w")
entrada_titulo_p = tk.Entry(frame_questao_professor, font=("Arial", 12))
entrada_titulo_p.pack(pady=10)

tk.Label(frame_questao_professor, text="Enunciado da Questão:", font=("Arial", 12)).pack(anchor="w")
entrada_enunciado = tk.Text(frame_questao_professor, height=4, width=80, font=("Arial", 12))
entrada_enunciado.pack(pady=5)

tk.Label(frame_questao_professor, text="Tipo da Questão:", font=("Arial", 12)).pack(anchor="w")
frame_tipo = tk.Frame(frame_questao_professor)
frame_tipo.pack()
tk.Radiobutton(frame_tipo, text="Objetiva", variable=tipo_questao_var, value="Objetiva", command=lambda: alterna_tipo("Objetiva")).pack(side="left", padx=10)
tk.Radiobutton(frame_tipo, text="Subjetiva", variable=tipo_questao_var, value="Subjetiva", command=lambda: alterna_tipo("Subjetiva")).pack(side="left", padx=10)

frame_alternativas = tk.Frame(frame_questao_professor)
frame_alternativas.pack(pady=5)

for letra in ["A", "B", "C", "D", "E"]:
    tk.Label(frame_alternativas, text=f"Alternativa {letra}:", font=("Arial", 12)).pack(anchor="w")
    entrada = tk.Entry(frame_alternativas, font=("Arial", 12), width=80)
    entrada.pack()
    alternativas_vars[letra] = entrada

tk.Label(frame_alternativas, text="Gabarito (Letra):", font=("Arial", 12)).pack(anchor="w", pady=(10, 0))
entrada_gabarito = tk.Entry(frame_alternativas, font=("Arial", 12), width=5)
entrada_gabarito.pack()

def alterna_tipo(tipo):
    if tipo == "Objetiva":
        frame_alternativas.pack(pady=5)
    else:
        frame_alternativas.pack_forget()

def salvar_questao():
    enunciado = entrada_enunciado.get("1.0", "end").strip()
    tipo = tipo_questao_var.get()

    if not enunciado:
        messagebox.showwarning("Aviso", "Digite o enunciado da questão.")
        return

    questao = {"tipo": tipo, "questao": enunciado}

    if tipo == "Objetiva":
        alternativas = {letra: entrada.get().strip() for letra, entrada in alternativas_vars.items()}
        gabarito = entrada_gabarito.get().strip().upper()

        if not all(alternativas.values()) or gabarito not in alternativas:
            messagebox.showwarning("Aviso", "Preencha todas as alternativas e defina um gabarito válido.")
            return

        questao["alternativas"] = alternativas
        questao["gabarito"] = gabarito

    todas_questoes.append(questao)
    entrada_enunciado.delete("1.0", "end")
    for entrada in alternativas_vars.values():
        entrada.delete(0, "end")
    entrada_gabarito.delete(0, "end")
    messagebox.showinfo("Sucesso", "Questão salva!")

def finalizar_prova():
    titulo = entrada_titulo_p.get().strip()
    if not titulo:
        messagebox.showwarning("Aviso", "Digite o título da prova.")
        return
    
    titulo_completo = f"{info_professor['nome']} - {titulo}"
    dados_prova["Título"] = titulo_completo

    if not todas_questoes:
        messagebox.showwarning("Aviso", "Adicione pelo menos uma questão.")
        return

    dados_prova["Título"] = titulo
    dados_prova["professor"] = info_professor
    dados_prova["questoes"] = todas_questoes

    try:
        with open("provas.json", "r", encoding="utf-8") as f:
            todas_as_provas = json.load(f)
    except FileNotFoundError:
        todas_as_provas = {}

    chave = f"{info_professor['nome']} - {titulo}"
    todas_as_provas[chave] = dados_prova

    with open("provas.json", "w", encoding="utf-8") as f:
        json.dump(todas_as_provas, f, ensure_ascii=False, indent=4)

    messagebox.showinfo("Sucesso", "Prova salva com sucesso!")
    frame_questao_professor.pack_forget()
    frame_inicio.pack(pady=20)


frame_botoes = tk.Frame(frame_questao_professor)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Salvar Questão", command=salvar_questao, bg="green", fg="white", font=("Arial", 12)).pack(side="left", padx=10)
tk.Button(frame_botoes, text="Finalizar Prova", command=finalizar_prova, bg="red", fg="white", font=("Arial", 12)).pack(side="left", padx=10)
tk.Button(frame_botoes, text="TELA INICIAL", command=lambda:voltar_tela_inicial(), bg="black", fg="white", font=("Arial", 12)).pack(side="left", padx=10)
 

alterna_tipo(tipo_questao_var.get())

###################### MODO ALUNO #####################
# Variáveis para aluno
numero_questao = 0
respostas_aluno = []
info_aluno = {}
questoes_subjetivas={}



# Cabeçalho com os dados do aluno
tk.Label(frame_aluno, text="Nome Completo:", font=("Arial", 12), anchor="w").pack(fill="x", padx=20, pady=2)
entrada_nome = tk.Entry(frame_aluno, font=("Arial", 12))
entrada_nome.pack(fill="x", padx=20, pady=2)

tk.Label(frame_aluno, text="Série:", font=("Arial", 12), anchor="w").pack(fill="x", padx=20, pady=2)
entrada_serie = tk.Entry(frame_aluno, font=("Arial", 12))
entrada_serie.pack(fill="x", padx=20, pady=2)

tk.Label(frame_aluno, text="Turma:", font=("Arial", 12), anchor="w").pack(fill="x", padx=20, pady=2)
entrada_turma = tk.Entry(frame_aluno, font=("Arial", 12))
entrada_turma.pack(fill="x", padx=20, pady=2)





# O menu será criado na função atualizar_menu_provas()

botao_iniciar = tk.Button(frame_aluno,text="Iniciar Prova", font=("Arial", 12), bg="green", fg="white",command=lambda: iniciar_prova())
botao_iniciar.pack(pady=50)

botao_voltar_inicio = tk.Button(frame_aluno,text="Tela Inicial",font=("Arial", 12),bg="black",fg="white",command=lambda: voltar_tela_inicial())
botao_voltar_inicio.pack(pady=20)

# Questões para o aluno
label_questao = tk.Label(frame_questao_aluno, text="", font=("Arial", 14), wraplength=700, justify="left")
label_questao.pack(anchor="w")

frame_alternativas = tk.Frame(frame_questao_aluno)
frame_alternativas.pack(anchor="w", pady=10)

resposta_var = tk.StringVar()

label_resultado = tk.Label(frame_resultado_final, text="", font=("Arial", 14), fg="black")
label_resultado.pack(pady=10)

botao_proxima = tk.Button(janela, text="Próxima", font=("Arial", 12), bg="black", fg="white", command=lambda: proxima_questao())
botao_proxima.pack_forget()

botao_finalizar = tk.Button(janela, text="FINALIZAR PROVA", font=("Arial", 12), bg="green", fg="white", command=lambda: mostrar_resultado_final())
botao_finalizar.pack_forget()


def iniciar_prova():
    nome = entrada_nome.get().strip()
    serie = entrada_serie.get().strip()
    turma = entrada_turma.get().strip()
    prova_escolhida = prova_selecionada.get()

    if not nome or not serie or not turma:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return
    if prova_escolhida in ["Selecione uma prova", "Nenhuma prova disponível"]:
        messagebox.showwarning("Aviso", "Por favor, selecione uma prova válida!")
        return
       
    # Salva as infos do aluno
    info_aluno['nome'] = nome
    info_aluno['serie'] = serie
    info_aluno['turma'] = turma

    global dados_prova, numero_questao, respostas_aluno
    dados_prova = todas_as_provas[prova_escolhida]
    numero_questao = 0
    respostas_aluno = []
    
    frame_aluno.pack_forget()
    frame_questao_aluno.pack(pady=20, fill="both", expand=True)
    botao_proxima.pack(pady=10)

    mostrar_questao()

def mostrar_questao():
    global numero_questao
    resposta_var.set("")

    if numero_questao in questoes_subjetivas:
        campo_texto = questoes_subjetivas[numero_questao]
        texto_salvo = campo_texto.get("1.0", "end").strip()
        if len(respostas_aluno) > numero_questao:
            respostas_aluno[numero_questao] = texto_salvo
        else:
            respostas_aluno.append(texto_salvo)

    for widget in frame_alternativas.winfo_children():
        widget.destroy()

    
    if numero_questao < len(dados_prova["questoes"]):
        questao = dados_prova["questoes"][numero_questao]
        label_questao.config(text=f"Questão {numero_questao+1}: {questao['questao']}")

        if questao["tipo"]=="Objetiva":
            for letra, texto in questao["alternativas"].items():
                rb = tk.Radiobutton(frame_alternativas, text=f"{letra}) {texto}", variable=resposta_var, value=letra, font=("Arial", 12), anchor="w", justify="left")
                rb.pack(fill="x", padx=20, pady=2)
        elif questao["tipo"] == "Subjetiva":
            resposta_subjetiva = tk.Text(frame_alternativas, height=5, width=80, font=("Arial", 12))
            resposta_subjetiva.pack(padx=10, pady=10)
            questoes_subjetivas[numero_questao] = resposta_subjetiva
    else:
        label_questao.config(text="")

    botao_proxima.pack_forget()
    botao_finalizar.pack_forget()

    if numero_questao==len(dados_prova["questoes"])-1:
        botao_finalizar.pack(pady=20)
    else:
        botao_proxima.pack(pady=20)

def proxima_questao():
    global numero_questao
    questao= dados_prova["questoes"][numero_questao]
    
    if questao["tipo"] == "Objetiva":
        resposta = resposta_var.get()
        if resposta == "":
            messagebox.showwarning("Aviso", "Por favor, selecione uma alternativa antes de continuar.")
            return
    else:
        campo_texto = questoes_subjetivas.get(numero_questao)
        resposta = campo_texto.get("1.0", "end").strip()

        if resposta == "":
            messagebox.showwarning("Aviso", "Por favor, escreva uma resposta antes de continuar.")
            return
    
    respostas_aluno.append(resposta)
    numero_questao += 1
    
    if numero_questao < len(dados_prova["questoes"])-1:
        mostrar_questao()
    elif numero_questao == len(dados_prova["questoes"])-1:
        mostrar_questao()
    else:
        pass



def tela_inicial():
    
    frame_questao_aluno.pack_forget()
    label_resultado.config(text="")
    botao_proxima.pack_forget()
    botao_voltar_inicio.pack_forget()
    frame_inicio.pack(pady=20)


    
botao_voltar_inicio = tk.Button(frame_resultado_final,text="Tela Inicial",font=("Arial", 12),bg="black",fg="white",command=lambda: voltar_tela_inicial())
botao_voltar_inicio.pack_forget()


def mostrar_resultado_final():
    global numero_questao
    questao = dados_prova["questoes"][numero_questao]
    if questao["tipo"] == "Objetiva":
        resposta = resposta_var.get()
    else:
        campo_texto = questoes_subjetivas.get(numero_questao)
        resposta = campo_texto.get("1.0", "end").strip()

    if len(respostas_aluno) > numero_questao:
        respostas_aluno[numero_questao] = resposta
    else:
        respostas_aluno.append(resposta)
        
    frame_questao_aluno.pack_forget()
    botao_proxima.pack_forget()
    botao_finalizar.pack_forget()
    
    
    todas_objetivas = all(q.get("tipo") == "Objetiva" for q in dados_prova["questoes"])

    resultado_texto = f"Aluno: {info_aluno['nome']}\nSérie: {info_aluno['serie']}\nTurma: {info_aluno['turma']}\n\n"

    if todas_objetivas:
        acertos = 0
        erros = []

        for i, resposta in enumerate(respostas_aluno):
            gabarito = dados_prova["questoes"][i].get("gabarito", "")
            if resposta.upper() == gabarito.upper():
                acertos += 1
            else:
                erros.append(i + 1)

        nota = (acertos / len(dados_prova["questoes"])) * 10 if dados_prova["questoes"] else 0

        resultado_texto += f"Prova finalizada!\nVocê acertou {acertos} questões.\n"
        if erros:
            resultado_texto += f"Você errou as questões: {erros}\n"
        else:
            resultado_texto += "Você não errou nenhuma questão.\n"
        resultado_texto += f"Sua nota final é {nota:.1f}."
    else:
        resultado_texto += "Prova finalizada!\nA correção será realizada manualmente pelo professor,\npois a prova contém questões subjetivas."
    salvar_respostas()

    
    messagebox.showinfo("Resultado", resultado_texto)
        
    label_resultado.config(text=resultado_texto)
    botao_voltar_inicio.pack(pady=20)
    frame_resultado_final.pack(pady=20)

def salvar_respostas():
    titulo_completo = dados_prova.get("Título", "Prova sem título")
    nome_arquivo = f"respostas_{titulo_completo.replace(' ', '_')}.json"
    respostas_salvas = {}
    for i, questao in enumerate(dados_prova["questoes"]):
        numero = i+1
        if i < len(respostas_aluno):
            respostas_salvas[numero] = respostas_aluno[i]
        else:
            respostas_salvas[numero] = ""
                
    resposta_final = {
        "aluno": info_aluno,
        "prova": dados_prova["Título"],
        "respostas": respostas_salvas,
    }

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            todas_respostas = json.load(f)
    except FileNotFoundError:
        todas_respostas = []

    todas_respostas.append(resposta_final)

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(todas_respostas, f, ensure_ascii=False, indent=4)


    print(f"Respostas salvas em {nome_arquivo}")

     

def voltar_tela_inicial():
    botao_voltar_inicio.pack_forget()
    frame_questao_aluno.pack_forget()
    frame_aluno.pack_forget()
    
    frame_professor.pack_forget()
    frame_questao_professor.pack_forget()
    frame_dados_professor.pack_forget()
    frame_redigir_prova.pack_forget()

    frame_correcao_login.pack_forget()
      
    botao_proxima.pack_forget()
    botao_voltar_inicio.pack_forget()

    
    label_resultado.config(text="")
    resposta_var.set("")
    respostas_aluno.clear()
    questoes_subjetivas.clear()

    
    frame_inicio.pack(pady=20)
    

   

janela.mainloop()
