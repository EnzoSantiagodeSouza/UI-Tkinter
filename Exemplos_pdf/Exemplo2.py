import tkinter as tk

def digitar(numero):
    visor.insert(tk.END, numero)
    
def limpar():
    visor.delete(0, tk.END)

janela = tk.Tk()
janela.title("Primeiros botões")

visor = tk.Entry(janela, width=24, justify="right")
visor.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

botao_7 = tk.Button(
    janela, 
    text="7", width=6, 
    command=lambda: digitar("7")
)
botao_7.grid(row=0, column=0, padx=5, pady=5)

botao_8 = tk.Button(
    janela, 
    text="8", width=6, 
    command=lambda: digitar("8")
)
botao_8.grid(row=0, column=1, padx=5, pady=5)

botao_c = tk.Button(janela, text="C", width=6, command=limpar)
botao_c.grid(row=0, column=2, padx=5, pady=5)

janela.mainloop()