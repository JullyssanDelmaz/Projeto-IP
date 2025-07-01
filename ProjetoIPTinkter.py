import json
import tkinter as tk

with open('prova 2.json', 'r', encoding='utf-8') as arquivo:
    dados_prova= json.load(arquivo)

def mostrar_questao():
    numero_questao = 1
    texto_questao = dados_prova["questoes"][numero_questao - 1]["questao"]
    label_questao.config(text=f"Questão {numero_questao}: {texto_questao}")
    

janela = tk.Tk()
janela.title("Projeto Jullyssan Delmaz IP 2025.1")
janela.geometry("1920x1080")

rotulo = tk.Label(janela, text="Prova de Matemática 2º Trimestre", font=("Arial", 16))
rotulo.pack(pady=10)

botao= tk.Button(janela, text="Iniciar Prova", command=mostrar_questao)
botao.pack()

label_questao= tk.Label(janela, text="")
label_questao.pack(pady=10)

janela.mainloop()
