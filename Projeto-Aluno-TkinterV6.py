import json
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import os, re, shutil, unicodedata



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

# Função para atualizar o menu das provas na tela do ALUNO
def atualizar_menu_provas():
    arquivos = [f for f in os.listdir() if f.endswith(".json") and "-" in f and not f.startswith("respostas_")]

    if not arquivos:
        arquivos = ["Nenhuma prova disponível"]

    prova_selecionada.set(arquivos[0])

    menu = menu_provas["menu"]
    menu.delete(0, "end")
    for arquivo in arquivos:
        menu.add_command(label=arquivo, command=tk._setit(prova_selecionada, arquivo))
          

# Função para atualizar o menu das provas na tela de CORREÇÃO

def atualizar_menu_provas_professor():
    provas_professor = []
    for arquivo in os.listdir():
        if arquivo.endswith(".json") and "-" in arquivo and not arquivo.startswith("respostas_"):
            try:
                with open(arquivo, "r", encoding="utf-8") as f:
                    prova = json.load(f)
                    if prova.get("professor", {}).get("matricula") == info_professor["matricula"]:
                        provas_professor.append(arquivo)
            except:
                continue

    if not provas_professor:
        provas_professor = ["Nenhuma prova disponível"]

    global lista_provas_professor, botao_corrigir
    
    for widget in frame_correcao_provas.winfo_children():
        widget.destroy()

    label = tk.Label(frame_correcao_provas, text="Selecione a prova para corrigir:", font=("Arial", 12))
    label.pack(pady=10)

    lista_provas_professor = ttk.Combobox(frame_correcao_provas, values=provas_professor, state="readonly", width=50)
    lista_provas_professor.pack(pady=5)
    lista_provas_professor.set(provas_professor[0])

    botao_corrigir = tk.Button(frame_correcao_provas, text="Iniciar Correção", bg="green", fg="white", command=lambda: iniciar_correcao_prova())
    botao_corrigir.pack(pady=10)

    botao_voltar_inicio = tk.Button(frame_correcao_provas, text="Tela Inicial", bg="black", fg="white", command=lambda: voltar_tela_inicial())
    botao_voltar_inicio.pack(pady=10)
        
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


########### MODO PROFESSOR ##################

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
    
    novo_professor = {
        'nome': nome_professor,
        'matricula': matricula,
        'disciplina': disciplina,
        'senha': senha_professor
    }

    try:
        with open("cadastro_professores.json", "r", encoding="utf-8") as f:
            professores = json.load(f)
    except FileNotFoundError:
        professores=[]

    for prof in professores:
        if prof["nome"] == nome_professor and prof["matricula"] == matricula:
            info_professor.clear()
            info_professor.update(prof)
            break
    else:
        professores.append(novo_professor)
        info_professor.clear()
        info_professor.update(novo_professor)


    with open("cadastro_professores.json", "w", encoding="utf-8") as f:
        json.dump(professores, f, ensure_ascii=False, indent=4)
        
    frame_professor.pack_forget()
    frame_questao_professor.pack(pady=20)

######## MODO CORREÇÃO #############
    
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

            atualizar_menu_provas_professor()
            return
        
    messagebox.showerror("Erro", "Dados incorretos ou professor não cadastrado.")
               
    
############### MODO PROFESSOR ###############
    
# REDIGINDO AS PROVAS

imagem_questao_diretorio = None

def selecionar_imagem():
    global imagem_questao_diretorio, imagem_preview_tk
    caminho = filedialog.askopenfilename(
        filetypes=[("Imagens", "*.png *.jpg *.jpeg *gif *bmp ")]
        )
    if caminho:
        imagem_questao_diretorio = caminho
        nome_arquivo = caminho.split('/')[-1]
        label_imagem_selecionada.config(text=f"Imagem selecionada: {nome_arquivo}")
        imagem = Image.open(caminho)
        imagem.thumbnail((300, 200))  
        imagem_preview_tk = ImageTk.PhotoImage(imagem)
        label_imagem_preview.config(image=imagem_preview_tk)
    else:
        imagem_questao_diretorio = None
        label_imagem_selecionada.config(text="Nenhuma imagem selecionada.")
        label_imagem_preview.config(image="")
        
        
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

botao_imagem = tk.Button(frame_questao_professor, text="Selecionar Imagem da Questão", command=selecionar_imagem)
botao_imagem.pack(pady=5)

label_imagem_selecionada = tk.Label(frame_questao_professor, text="Nenhuma imagem selecionada.", font=("Arial", 10))
label_imagem_selecionada.pack()

label_imagem_preview = tk.Label(frame_questao_professor)
label_imagem_preview.pack(pady=5)
                         
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
    global imagem_questao_diretorio
    
    enunciado = entrada_enunciado.get("1.0", "end").strip()
    tipo = tipo_questao_var.get()

    if not enunciado:
        messagebox.showwarning("Aviso", "Digite o enunciado da questão.")
        return

    questao = {"tipo": tipo, "questao": enunciado}

    if imagem_questao_diretorio:
        pasta_destino = "imagens_provas"
        os.makedirs(pasta_destino, exist_ok=True)
        nome_arquivo = os.path.basename(imagem_questao_diretorio)
        destino = os.path.join(pasta_destino, nome_arquivo)
        shutil.copy(imagem_questao_diretorio, destino)
        questao["imagem"] = destino
                

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
    imagem_questao_diretorio = None
    label_imagem_selecionada.config(text="Nenhuma imagem selecionada.")
    label_imagem_preview.config(image="")
    label_imagem_preview.image = None 
    
    messagebox.showinfo("Sucesso", "Questão salva!")

def finalizar_prova():
    titulo = entrada_titulo_p.get().strip()
    if not titulo:
        messagebox.showwarning("Aviso", "Digite o título da prova.")
        return

    # Monta o nome do arquivo
    nome_arquivo = f"{info_professor['nome']} - {titulo}.json"

    dados_prova["Título"] = titulo
    dados_prova["professor"] = info_professor
    dados_prova["questoes"] = todas_questoes

    # Salva em arquivo separado
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(dados_prova, f, ensure_ascii=False, indent=4)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar a prova: {e}")
        return

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
    prova_arquivo = prova_selecionada.get()

    if not nome or not serie or not turma:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return
    if prova_arquivo in ["Selecione uma prova", "Nenhuma prova disponível"]:
        messagebox.showwarning("Aviso", "Por favor, selecione uma prova válida!")
        return
       
    # Salva as infos do aluno
    info_aluno['nome'] = nome
    info_aluno['serie'] = serie
    info_aluno['turma'] = turma

    global dados_prova, numero_questao, respostas_aluno
    try:
        with open(prova_arquivo, "r", encoding="utf-8") as f:
            dados_prova = json.load(f)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar a prova: {e}")
        return

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
        if "imagem" in questao:
            try:
                imagem = Image.open(questao["imagem"])
                imagem.thumbnail((400,400))
                imagem_tk = ImageTk.PhotoImage(imagem)
                label_imagem = tk.Label(frame_alternativas, image=imagem_tk)
                label_imagem.image = imagem_tk
                label_imagem.pack(pady=10)
            except Exception as e:
                messagebox.showwarning("Erro", "Não foi possível carregar a imagem da questão.")

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
    def normalizar_nome(texto):
        texto = unicodedata.normalize("NFKD", texto)
        texto = texto.encode("ASCII", "ignore").decode("ASCII")
        texto = re.sub(r"[^\w\s-]", "", texto)
        texto = texto.strip().replace(" ", "_")
        return texto

    titulo_completo = dados_prova.get("Título", "Prova sem título")
    nome_base = normalizar_nome(titulo_completo)
    nome_arquivo = f"respostas_{nome_base}.json"
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


############### MODO CORREÇÃO ####################

notas_do_aluno =[]

def salvando_notas_iniciais():
     global notas_do_aluno, dados_prova
     quantidade_questoes = len(dados_prova.get("questoes", []))
     notas_do_aluno = [0.0] * quantidade_questoes

def salvar_nota_atual(entrada_nota, numero_questao_corrigir):
    global notas_do_aluno
    try:
        nota = float(entrada_nota.get())
    except ValueError:
        nota = None
    if nota is not None and nota >= 0:
        if 0 <= numero_questao_corrigir < len(notas_do_aluno):
            notas_do_aluno[numero_questao_corrigir] = nota
        


  
def iniciar_correcao_prova():
    
    global respostas_aluno_corrigir, aluno_index, numero_questao_corrigir
    
    aluno_index = 0
    numero_questao_corrigir = 0
    prova_arquivo = lista_provas_professor.get()
    
    if prova_arquivo in ["Nenhuma prova disponível", ""]:
        messagebox.showwarning("Aviso", "Selecione uma prova válida para corrigir.")
        return
    corrigir_provas(prova_arquivo)

    
def corrigir_provas(prova_arquivo):
    def normalizar_nome(texto):
        texto = unicodedata.normalize("NFKD", texto)
        texto = texto.encode("ASCII", "ignore").decode("ASCII") 
        texto = re.sub(r"[^\w\s-]", "", texto)  
        texto = texto.strip().replace(" ", "_")
        return texto

    global notas_do_aluno, dados_prova, respostas_aluno_corrigir, numero_questao_corrigir, nome_aluno_corrigir

    try:
        with open(prova_arquivo, "r", encoding="utf-8") as f:
            dados_prova = json.load(f)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar a prova: {e}")
        return

    
    quantidade_questoes = len(dados_prova.get("questoes", []))
    if quantidade_questoes == 0:
        messagebox.showwarning("Aviso", "Esta prova não tem questões para corrigir.")
        return

    notas_do_aluno = [0.0] * quantidade_questoes
    

    
    try:
        titulo_original = dados_prova.get("Título", "")
        titulo_normalizado = normalizar_nome(titulo_original)
        arquivo_respostas = f"respostas_{titulo_normalizado}.json"

        with open(arquivo_respostas, "r", encoding="utf-8") as f:
            respostas_aluno_corrigir = json.load(f)
        
    except FileNotFoundError:
        messagebox.showwarning("Aviso", "Nenhum aluno respondeu essa prova ainda.")
        return
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar as respostas: {e}")
        return

    numero_questao_corrigir = 0
    aluno_index = 0
    aluno = respostas_aluno_corrigir[aluno_index]
    nome_aluno_corrigir = aluno["aluno"]["nome"]
    mostrar_questao_correcao(aluno_index)


    
def mostrar_questao_correcao(aluno_index):
    
    global numero_questao_corrigir, dados_prova, respostas_aluno_corrigir, nome_aluno_corrigir, entrada_nota
    
    titulo_prova = dados_prova.get("Título")
    for widget in frame_correcao_provas.winfo_children():
        widget.destroy()
    
    aluno = respostas_aluno_corrigir[aluno_index]
    nome_aluno_corrigir = aluno["aluno"]["nome"]
    
    questoes = dados_prova.get("questoes", [])
    numero_questao_corrigir = min(numero_questao_corrigir, len(questoes) - 1)
    
    if numero_questao_corrigir < 0 or numero_questao_corrigir >= len(questoes):
        messagebox.showinfo("Info", "Fim das questões desta prova.")
        return
    
    questao = questoes[numero_questao_corrigir]
    resposta_aluno = aluno["respostas"].get(str(numero_questao_corrigir + 1), "")
    
    titulo = tk.Label(frame_correcao_provas, 
                      text=f"Corrigindo prova de: {nome_aluno_corrigir}\nQuestão {numero_questao_corrigir + 1}",
                      font=("Arial", 14, "bold"))
    titulo.pack(pady=10)
    
    enunciado = tk.Label(frame_correcao_provas, text=questao["questao"], font=("Arial", 12), wraplength=700, justify="left")
    enunciado.pack(pady=5)
    
    if "imagem" in questao:
        try:
            imagem = Image.open(questao["imagem"])
            imagem.thumbnail((400, 400))
            imagem_tk = ImageTk.PhotoImage(imagem)
            label_img = tk.Label(frame_correcao_provas, image=imagem_tk)
            label_img.image = imagem_tk
            label_img.pack(pady=5)
        except Exception:
            pass

    if questao["tipo"] == "Objetiva":
        alternativas = questao.get("alternativas", {})
        texto_alternativas = "\n".join(f"{letra}) {texto}" for letra, texto in alternativas.items())
        
        label_alternativas = tk.Label(frame_correcao_provas, text=texto_alternativas, font=("Arial", 12), justify="left")
        label_alternativas.pack(pady=5)

        gabarito = questao.get("gabarito", "")
        texto_resposta = f"Resposta do aluno: {resposta_aluno}\nGabarito: {gabarito}"
        resposta_label = tk.Label(frame_correcao_provas, text=texto_resposta, font=("Arial", 12))
        resposta_label.pack(pady=5)

        
        nota_auto = 10.0/len(questoes) if resposta_aluno == gabarito else 0.0

        if 0 <= numero_questao_corrigir < len(notas_do_aluno):
            if notas_do_aluno[numero_questao_corrigir] == 0:
                notas_do_aluno[numero_questao_corrigir] = nota_auto
        
        
        label_nota = tk.Label(frame_correcao_provas, text="Nota (ajustável):", font=("Arial", 12, "bold"))
        label_nota.pack(pady=(10, 0))
        
        entrada_nota = tk.Entry(frame_correcao_provas, font=("Arial", 12), width=10)
        entrada_nota.pack(pady=5)
        entrada_nota.delete(0, tk.END)
        if 0 <= numero_questao_corrigir < len(notas_do_aluno):
            entrada_nota.insert(0, str(notas_do_aluno[numero_questao_corrigir]))
        else:
            entrada_nota.insert(0, "0")
        
    else:
        resposta_texto = tk.Text(frame_correcao_provas, height=8, width=80, font=("Arial", 12))
        resposta_texto.insert("1.0", resposta_aluno)
        resposta_texto.config(state="disabled") 
        resposta_texto.pack(pady=5)

        label_nota_manual = tk.Label(frame_correcao_provas, text="Digite a nota para esta questão:", font=("Arial", 12))
        label_nota_manual.pack(pady=(10, 0))
        entrada_nota = tk.Entry(frame_correcao_provas, font=("Arial", 12), width=10)
        entrada_nota.pack(pady=5)
        entrada_nota.delete(0, tk.END)
        if 0 <= numero_questao_corrigir < len(notas_do_aluno):
            entrada_nota.insert(0, str(notas_do_aluno[numero_questao_corrigir]))
        else:
            entrada_nota.insert(0, "0")

        

    frame_botoes = tk.Frame(frame_correcao_provas)
    frame_botoes.pack(pady=15)

    def ir_proxima_questao():
        global numero_questao_corrigir
        salvar_nota_atual(entrada_nota, numero_questao_corrigir)
        
        if 0 <= numero_questao_corrigir < len(notas_do_aluno):
            salvar_nota_atual(entrada_nota, numero_questao_corrigir)
        else:
            print("Tentativa de salvar nota com índice inválido:")
        if numero_questao_corrigir < len(questoes) - 1:
            numero_questao_corrigir += 1
            mostrar_questao_correcao(aluno_index)
        else:
            messagebox.showinfo("Info", "Última questão.")

    def ir_questao_anterior():
        global numero_questao_corrigir
        salvar_nota_atual(entrada_nota, numero_questao_corrigir)
        if numero_questao_corrigir > 0:
            numero_questao_corrigir -= 1
            mostrar_questao_correcao(aluno_index)
        else:
            messagebox.showinfo("Info", "Primeira questão.")

    def ir_proximo_aluno():
        global numero_questao_corrigir, aluno_index
        salvar_nota_atual(entrada_nota, numero_questao_corrigir)           
        nota_final = sum(notas_do_aluno)
        salvar_nota_final(aluno_index, nota_final, titulo_prova)
        
        if aluno_index + 1 < len(respostas_aluno_corrigir):
            aluno_index+=1
            numero_questao_corrigir = 0
            salvando_notas_iniciais()
            mostrar_questao_correcao(aluno_index)
        else:
            messagebox.showinfo("Info", "Último aluno corrigido.")
            frame_correcao_provas.pack_forget()
            frame_correcao_provas.pack(pady=20)
            
    tk.Button(frame_botoes, text="Anterior", command=ir_questao_anterior).pack(side="left", padx=5)
    
    if numero_questao_corrigir < len(questoes) - 1:
        tk.Button(frame_botoes, text="Próxima", command=ir_proxima_questao).pack(side="left", padx=5)
        
    if numero_questao_corrigir == len(questoes) - 1:
        tk.Button(frame_botoes, text="Próximo Aluno", command=ir_proximo_aluno).pack(side="left", padx=5)
        
    tk.Button(frame_botoes, text="Voltar ao Menu", bg="yellow", fg="black", command=lambda: voltar_ao_menu()).pack(side="left", padx=5)



def salvar_nota_final (aluno_index, nota_final, titulo_prova):
    
    titulo_prova = dados_prova.get("Título", None)
    if titulo_prova is None:
        titulo_prova = "Sem_titulo"
    
    def normalizar_nome(texto):
        texto = unicodedata.normalize("NFKD", texto)
        texto = texto.encode("ASCII", "ignore").decode("ASCII") 
        texto = re.sub(r"[^\w\s-]", "", texto)  
        texto = texto.strip().replace(" ", "_")
        return texto
    
    titulo_base = normalizar_nome(titulo_prova)
    nome_arquivo = f"notas_{titulo_base}.json"
    nome_aluno = respostas_aluno_corrigir[aluno_index]["aluno"]["nome"]
                                                       
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
    else:
        dados = {}

    
    dados[nome_aluno] = {
        "nota_final": nota_final
    }

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    print(f"Nota do aluno {nome_aluno} salva no arquivo {nome_arquivo}.")




    
def voltar_ao_menu():
    for widget in frame_correcao_provas.winfo_children():
        widget.destroy()
    atualizar_menu_provas_professor()
    
def voltar_tela_inicial():
    botao_voltar_inicio.pack_forget()
    frame_questao_aluno.pack_forget()
    frame_aluno.pack_forget()
    
    frame_professor.pack_forget()
    frame_questao_professor.pack_forget()
    frame_dados_professor.pack_forget()
    frame_redigir_prova.pack_forget()

    frame_correcao_login.pack_forget()
    frame_correcao_provas.pack_forget()
      
    botao_proxima.pack_forget()
    botao_voltar_inicio.pack_forget()

    
    label_resultado.config(text="")
    resposta_var.set("")
    respostas_aluno.clear()
    questoes_subjetivas.clear()

    
    frame_inicio.pack(pady=20)


janela.mainloop()
