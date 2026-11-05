import tkinter as tk

def somar():
    #.get() lê o conteúdo das caixas como texto
    n1 = float(entrada1.get())
    n2 = float(entrada2.get())
    resultado = n1 + n2
    
    # Altera o texto do Label para mostrar a soma na janela
    lbl_resultado.config(text=f"Resultado: {resultado}")

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("350x250")

# Cria o texto e a caixa de entrada
lbl_numero1 = tk.Label(janela, text="Primeiro Número:")
lbl_numero1.pack() # Posiciona o componente na janela

entrada1 = tk.Entry(janela)
entrada1.pack()

# Cria o texto e a caixa de entrada do segundo número
lbl_numero2 = tk.Label(janela, text="Segundo Número:")
lbl_numero2.pack()

entrada2 = tk.Entry(janela)
entrada2.pack()

# Cria o botão e associa o clique à função somar
botao_somar = tk.Button(
    janela, 
    text="Somar", 
    command=somar # Sem (): a função será chamada somente no clique
)
botao_somar.pack(pady=15)

# Cria o espaço onde o resultado será exibido
lbl_resultado = tk.Label(janela, text="Resultado: ")
lbl_resultado.pack()

# Mantém janela aberta e aguardando as ações do usuário
janela.mainloop()