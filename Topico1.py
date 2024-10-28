import dis
import tkinter as tk
from tkinter import messagebox, font
"""
Verificando condição digitada pelo usuário
Observe o uso do "input"
Aqui estamos utilizando o placeholder %s e %d como marcadores de posição
Observe que  utilizamos após a frase a ser impressa, %(VARIAVEIS) para dizer ao python quais variáveis serão impressas nos marcadores.
Observe também que utilimos a função "f" antes da frase. Podemos imprimir variáveis e manipular variáveis no print, utilizando colchetes "{VARIAVEL}"
"""

## Backend do programa.
def verificar_aprovacao():
    # Obtendo os valores dos campos
    disciplina = entrada_disciplina.get()
    nota_final = entrada_nota.get()
    universidade = entrada_universidade.get()

    try:
        # Convertendo a nota para inteiro e validando se está no intervalo adequado
        nota_final = int(nota_final)
        if nota_final < 0 or nota_final > 100:
            messagebox.showerror("Erro", "A nota deve estar entre 0 e 100.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para a nota.")
        return

    # Verificando a condição de aprovação
    if disciplina == 'Programação de Computadores' and nota_final >= 70:
        messagebox.showinfo("Resultado", f"Você foi aprovado na {disciplina}, na {universidade}, com média final {nota_final}, meus parabens!!")
    elif disciplina == 'Psicologia Organizacional' and nota_final >= 70:
      messagebox.showinfo("Resultado", f"Você foi aprovado na {disciplina}, na {universidade}, com média final de {nota_final}, meus parabens!!")
    elif(disciplina != 'Programação de computadores' or 'Psicologia Organizacional'):
        messagebox.showinfo("Resultado", "Apenas disciplinas do segundo módulo do primeiro semestre podem ser verificadas!!")  
        
## Interface do programa.  
janela = tk.Tk()
janela.title("Verificador de Aprovação")
janela.geometry("600x500")

## Design
janela.configure(bg="#f0f8ff")
# Fontes
titulo_fonte = font.Font(family="Helvetica", size=18, weight="bold")
label_fonte = font.Font(family="Arial", size=12)


# Borda
frame_inputs = tk.Frame(janela, bg="#e6f2ff", bd=2, relief="groove", padx=10, pady=10)
frame_inputs.pack(pady=10)




# Criando e posicionando os elementos da interface
tk.Label(frame_inputs, text="Disciplina:", font=label_fonte, bg="#e6f2ff").grid(row=0, column=0, sticky="w", pady=5)
entrada_disciplina = tk.Entry(frame_inputs, width=35)
entrada_disciplina.grid(row=0, column=1, padx=10)

tk.Label(frame_inputs, text="Nota Final (entre 0 e 100):", font=label_fonte, bg="#e6f2ff").grid(row=1, column=0, sticky="w", pady=5)
entrada_nota = tk.Entry(frame_inputs, width=10)
entrada_nota.grid(row=1, column=1, padx=10)


tk.Label(frame_inputs, text="Universidade:", font=label_fonte, bg="#e6f2ff").grid(row=2, column=0, sticky="w", pady=5)
entrada_universidade = tk.Entry(frame_inputs, width=35)
entrada_universidade.grid(row=2, column=1, padx=10)

# Botão para verificar a aprovação
botao_verificar = tk.Button(janela, text="Verificar Aprovação", command=verificar_aprovacao,
                            font=label_fonte, bg="#0066cc", fg="white", width=20, height=2, relief="raised")
botao_verificar.pack(pady=20)

# Rodapé
rodape_label = tk.Label(janela, text="Desenvolvido por Gabriel", font=("Arial", 10), fg="#666666", bg="#f0f8ff")
rodape_label.pack(side="bottom", pady=10)

# Iniciando o loop principal da interface
janela.mainloop()
