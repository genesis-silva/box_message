
# Importa a biblioteca tkinter, que é usada para criar interfaces gráficas de usuário (GUIs).
import tkinter as tk
from tkinter import messagebox

# Função que será chamada quando o botão for clicado.
def mudar_mensagem():
    """
    Esta função altera o texto exibido na etiqueta e mostra uma mensagem de saudação.
    """
    # Altera o texto da etiqueta para uma nova mensagem.
    label_mensagem.config(text="Olá, mundo! Você clicou no botão!")

    messagebox.showinfo("Saudação", "Bem-vindo ao seu primeiro aplicativo GUI!")

janela = tk.Tk()
janela.title("Meu Primeiro Aplicativo Python") # Define o título da janela.
janela.geometry("400x200") # Define o tamanho inicial da janela (largura x altura).

# Cria uma etiqueta (Label) para exibir texto.
# O texto inicial é "Clique no botão abaixo!".
label_mensagem = tk.Label(janela, text="Clique no botão abaixo!", font=("Arial", 16))
# Posiciona a etiqueta na janela. 'pack()' organiza o widget automaticamente.
label_mensagem.pack(pady=20) # 'pady' adiciona um preenchimento vertical de 20 pixels.


botao_clique = tk.Button(janela, text="Clique Aqui!", command=mudar_mensagem, font=("Arial", 14), bg="lightblue", fg="darkblue", relief="raised")
# Posiciona o botão na janela.
botao_clique.pack(pady=10)

janela.mainloop()