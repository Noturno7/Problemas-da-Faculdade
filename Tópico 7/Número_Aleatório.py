import tkinter as tk
from tkinter import messagebox
import random
import numpy as np

# Variáveis globais
tentativas = np.array([], dtype=int)  # Array para armazenar as tentativas do jogador

# Função para iniciar o jogo
def iniciar_jogo():
    global minimo, maximo, chances, num_aleatorio, tentativas
    try:
        minimo = int(entry_minimo.get())
        maximo = int(entry_maximo.get())
        chances = int(entry_chances.get())
        
        if minimo >= maximo:
            raise ValueError("O valor mínimo deve ser menor que o máximo.")
        
        num_aleatorio = random.randint(minimo, maximo)  # Gerando o número alvo
        tentativas = np.array([], dtype=int)  # Resetando as tentativas
        
        feedback_label.config(text=f"Tente adivinhar um número entre {minimo} e {maximo}")
        tentativa_button.config(state='normal')
        
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Função para verificar a tentativa do usuário
def verificar_proximidade(num_tentativa, num_aleatorio):
    distancia = abs(num_tentativa - num_aleatorio)  # Calcula a distância entre os números
    
    # Classificação de proximidade
    if distancia == 0:
        return "Parabéns! Você acertou o número!"
    elif distancia <= 5:
        return "Fervendo! Muito perto!"
    elif distancia <= 10:
        return "Quente! Está próximo."
    elif distancia <= 30:
        return "Morno. Está um pouco longe."
    else:
        return "Frio. Está longe do número."
def fazer_tentativa():
    global tentativas, chances, num_aleatorio
    try:
        num_tentativa = int(entry_tentativa.get())
        tentativas = np.append(tentativas, num_tentativa)  # Armazenando tentativa
        
        # Verifica se a tentativa excede o número de chances
        if len(tentativas) > chances:
            feedback_label.config(text=f"Suas chances acabaram! O número era {num_aleatorio}")
            tentativa_button.config(state='disabled')
            return
        
        # Verifica se acertou ou fornece proximidade
        proximidade_msg = verificar_proximidade(num_tentativa, num_aleatorio)
        feedback_label.config(text=proximidade_msg)
        
        # Atualiza o histórico
        atualizar_historico()
        
        # Bloqueia o botão se o jogador acertou
        if num_tentativa == num_aleatorio:
            tentativa_button.config(state='disabled')
        
    except ValueError:
        messagebox.showerror("Erro", "Digite um número inteiro válido!")


# Função para atualizar o histórico de tentativas
def atualizar_historico():
    tentativas_label.config(text=f"Suas tentativas: {tentativas}")
    if len(tentativas) > 0:
        media_tentativas = np.mean(tentativas)
        acima_do_alvo = np.sum(tentativas > num_aleatorio)
        abaixo_do_alvo = np.sum(tentativas < num_aleatorio)
        analise_label.config(text=f"Média: {media_tentativas:.2f}, Acima: {acima_do_alvo}, Abaixo: {abaixo_do_alvo}")
    else:
        analise_label.config(text="")
        
    

# Configurações principais da interface Tkinter
root = tk.Tk()
root.title("Jogo de Adivinhação com Análise Numérica")
root.geometry("500x400")
root.configure(bg="#006400")  # Cor de fundo

# Títulos e instruções
tk.Label(root, text="Bem-vindo ao Jogo de Adivinhação!", font=("Helvetica", 16, "bold"), bg="#32CD32").pack(pady=10)
tk.Label(root, text="Informe o intervalo e a quantidade de tentativas permitidas:", bg="#008000").pack()

# Labels e caixas de entrada para limite mínimo, máximo e chances
tk.Label(root, text="Valor Mínimo:", bg="#228B22").pack()
entry_minimo = tk.Entry(root)
entry_minimo.pack()

tk.Label(root, text="Valor Máximo:", bg="#228B22").pack()
entry_maximo = tk.Entry(root)
entry_maximo.pack()

tk.Label(root, text="Quantidade de Tentativas:", bg="#228B22").pack()
entry_chances = tk.Entry(root)
entry_chances.pack()

# Botão para iniciar o jogo
iniciar_button = tk.Button(root, text="Iniciar Jogo", command=iniciar_jogo, bg="#4CAF50", fg="white")
iniciar_button.pack(pady=10)

# Caixa de entrada e botão para fazer tentativas
tk.Label(root, text="Sua Tentativa:", bg="#228B22").pack()
entry_tentativa = tk.Entry(root)
entry_tentativa.pack()

tentativa_button = tk.Button(root, text="Fazer Tentativa", command=fazer_tentativa, state='disabled', bg="#FF5722", fg="white")
tentativa_button.pack(pady=10)

# Labels de feedback e análise
feedback_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#228B22", fg="#333")
feedback_label.pack(pady=5)

tentativas_label = tk.Label(root, text="Suas tentativas: ", bg="#228B22", fg="#333")
tentativas_label.pack()

analise_label = tk.Label(root, text="", bg="#228B22", fg="#333")
analise_label.pack(pady=5)

# Executa a interface
root.mainloop()
