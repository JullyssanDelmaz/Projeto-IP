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

frame_questao = tk.Frame(janela)
frame_questao.pack(pady=20, fill="both", expand=True)
frame_questao.pack_forget()  # começa escondido


# Tela inicial
botao_professor = tk.Button(frame_inicio, text="PROFESSOR", font=("Arial", 10), bg="red", fg="white")
botao_professor.grid(row=0, column=0, padx=5)
botao_aluno = tk.Button(frame_inicio, text="ALUNO", font=("Arial", 10), bg="green", fg="white")
botao_aluno.grid(row=0, column=3, padx=20)

# Variáveis para provas e seleção
todas_as_provas = {}
prova_selecionada = tk.StringVar(value="Selecione uma prova")
dados_prova = {}

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

    # Remove o menu anterior
    for widget in frame_aluno.grid_slaves(row=3, column=1):
        widget.destroy()

    # Cria novo menu com as opções atualizadas
    novo_menu = tk.OptionMenu(frame_aluno, prova_selecionada, *opcoes)
    novo_menu.config(width=30, font=("Arial", 12))
    novo_menu.grid(row=3, column=1)

# MODOS
def modo_professor():
    frame_inicio.pack_forget()
    frame_professor.pack(pady=20)

def modo_aluno():
    frame_inicio.pack_forget()
    atualizar_menu_provas()
    frame_aluno.pack(pady=20)

botao_professor.config(command=modo_professor)
botao_aluno.config(command=modo_aluno)


# Cabeçalho com os dados do professor
tk.Label(frame_professor, text="Nome Completo:", font=("Arial", 12)).grid(row=0, column=0, sticky="e", pady=5)
entrada_nome_professor= tk.Entry(frame_professor, font=("Arial",12))
entrada_nome_professor.grid(row=0, column=1)

tk.Label(frame_professor, text="Matrícula:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", pady=5)
entrada_matricula= tk.Entry(frame_professor, font=("Arial", 12))
entrada_matricula.grid(row=1, column=1)

tk.Label(frame_professor, text="Disciplina:", font=("Arial", 12)).grid(row=2, column=0, sticky="e", pady=5)
entrada_disciplina= tk.Entry(frame_professor, font=("Arial", 12))
entrada_disciplina.grid(row=2, column=1)

tk.Label(frame_professor, text="Série", font=("Arial", 12)).grid(row=3, column=0, sticky="e", pady=5)
entrada_serie_professor= tk.Entry(frame_professor, font=("Arial", 12))
entrada_serie_professor.grid(row=3, column=1)

botao_seguinte = tk.Button(frame_professor, text="Iniciar Prova", font=("Arial", 12), bg="Red", fg="white", command=lambda: dados_professor())
botao_seguinte.grid(row=4, column=0, columnspan=2, pady=15)

# Cabeçalho Professor
info_professor={}

def dados_professor():
    nome_professor= entrada_nome_professor.get().strip()
    matricula= entrada_matricula.get().strip()
    disciplina= entrada_disciplina.get().strip()
    serie_professor= entrada_serie_professor.get().strip()

    if not nome_professor or not matricula or not disciplina or not serie_professor:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return
    
    # Salva as informações do professor
    info_professor['nome'] = nome_professor
    info_professor['matricula'] = matricula 
    info_professor['disciplina'] = disciplina
    info_professor['serie'] = serie_professor
    frame_professor.pack_forget()
    frame_questao_professor.pack(pady=20)

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

alterna_tipo(tipo_questao_var.get())

# Variáveis para aluno
numero_questao = 0
respostas_aluno = []
info_aluno = {}

# Cabeçalho com os dados do aluno
tk.Label(frame_aluno, text="Nome Completo:", font=("Arial", 12)).grid(row=0, column=0, sticky="e")
entrada_nome = tk.Entry(frame_aluno, font=("Arial", 12))
entrada_nome.grid(row=0, column=1)

tk.Label(frame_aluno, text="Série:", font=("Arial", 12)).grid(row=1, column=0, sticky="e")
entrada_serie = tk.Entry(frame_aluno, font=("Arial", 12))
entrada_serie.grid(row=1, column=1)

tk.Label(frame_aluno, text="Turma:", font=("Arial", 12)).grid(row=2, column=0, sticky="e")
entrada_turma = tk.Entry(frame_aluno, font=("Arial", 12))
entrada_turma.grid(row=2, column=1)

tk.Label(frame_aluno, text="Selecione a Prova:", font=("Arial", 12)).grid(row=3, column=0, sticky="e")

# O menu será criado na função atualizar_menu_provas()

botao_iniciar = tk.Button(frame_aluno, text="Iniciar Prova", font=("Arial", 12), bg="green", fg="white", command=lambda: iniciar_prova())
botao_iniciar.grid(row=4, column=0, columnspan=2, pady=15)

# Questões para o aluno
label_questao = tk.Label(frame_questao, text="", font=("Arial", 14), wraplength=700, justify="left")
label_questao.pack(anchor="w")

frame_alternativas = tk.Frame(frame_questao)
frame_alternativas.pack(anchor="w", pady=10)

resposta_var = tk.StringVar()

label_resultado = tk.Label(janela, text="", font=("Arial", 14), fg="black")
label_resultado.pack(pady=10)

botao_proxima = tk.Button(janela, text="Próxima", font=("Arial", 12), bg="black", fg="white", command=lambda: proxima_questao())
botao_proxima.pack_forget()

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
    frame_questao.pack(pady=20, fill="both", expand=True)
    botao_proxima.pack(pady=10)

    mostrar_questao()

def mostrar_questao():
    resposta_var.set("")

    for widget in frame_alternativas.winfo_children():
        widget.destroy()

    global numero_questao
    if numero_questao < len(dados_prova["questoes"]):
        questao = dados_prova["questoes"][numero_questao]
        label_questao.config(text=f"Questão {numero_questao+1}: {questao['questao']}")

        if "alternativas" in questao:
            for letra, texto in questao["alternativas"].items():
                rb = tk.Radiobutton(frame_alternativas, text=f"{letra}) {texto}", variable=resposta_var, value=letra, font=("Arial", 12), anchor="w", justify="left")
                rb.pack(fill="x", padx=20, pady=2)
    else:
        mostrar_resultado_final()

def proxima_questao():
    resposta = resposta_var.get()
    if resposta == "":
        messagebox.showwarning("Aviso", "Por favor, selecione uma alternativa antes de continuar.")
        return
    
    respostas_aluno.append(resposta)

    global numero_questao
    numero_questao += 1
    if numero_questao < len(dados_prova["questoes"]):
        mostrar_questao()
    else:
        mostrar_resultado_final()

def mostrar_resultado_final():
    frame_questao.pack_forget()
    botao_proxima.pack_forget()

    acertos = 0
    erros = []

    for i, resposta in enumerate(respostas_aluno):
        gabarito = dados_prova["questoes"][i].get("gabarito", "")
        if resposta.upper() == gabarito.upper():
            acertos += 1
        else:
            erros.append(i+1)

    nota = (acertos / len(dados_prova["questoes"])) * 10 if dados_prova["questoes"] else 0

    resultado_texto = f"Aluno: {info_aluno['nome']}\nSérie: {info_aluno['serie']}\nTurma: {info_aluno['turma']}\n\n"
    resultado_texto += f"Prova finalizada!\nVocê acertou {acertos} questões.\n"
    if erros:
        resultado_texto += f"Você errou as questões: {erros}\n"
    else:
        resultado_texto += "Você não errou nenhuma questão.\n"
    resultado_texto += f"Sua nota final é {nota:.1f}."

    label_resultado.config(text=resultado_texto)

janela.mainloop()
