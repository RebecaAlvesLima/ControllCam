import sqlite3
import tkinter as tk
from tkinter import ttk

# Função para conectar ao banco de dados e obter os dados
def obter_dados():
    conn = sqlite3.connect('placas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, placa, data_hora FROM placas')
    dados = cursor.fetchall()
    conn.close()
    return dados

# Função para atualizar a lista na interface gráfica
def atualizar_lista():
    dados = obter_dados()
    for row in tree.get_children():
        tree.delete(row)
    for row in dados:
        tree.insert("", "end", values=row)

# Criar a janela principal
root = tk.Tk()
root.title("Control CAM")

# Criar uma árvore para mostrar os dados
tree = ttk.Treeview(root, columns=("id", "Placa", "data_hora"), show="headings")
tree.heading("Placa", text="Placa")
tree.heading("id", text="Número")
tree.heading("data_hora", text="Data e Hora")
tree.pack(padx=20, pady=20)

# Botão para atualizar a lista
atualizar_button = tk.Button(root, text="Atualizar Lista", command=atualizar_lista)
atualizar_button.pack(pady=10)

# Chamar a função para exibir dados inicialmente
atualizar_lista()

# Iniciar o loop da aplicação
root.mainloop()