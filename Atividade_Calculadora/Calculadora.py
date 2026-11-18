import tkinter as tk

# Variáveis globais - Pra armazenar o primeiro número e a operação selecionada
num1 = 0
operacaoSelecionada = ""

# Funções
def digitar(numero):
    try:
        float(visor.get())
    except ValueError:
    #if visor.get() == "+" or visor.get() == "-" or visor.get() == "×" or visor.get() == "÷": #deve haver uma forma de melhorar isso LOL
        visor.delete(0, tk.END)
    visor.insert(tk.END, numero)

def limpar():
    visor.delete(0, tk.END)

def apagar():
    visor.delete(len(visor.get())-1, tk.END)
    
def ponto():
    if "." not in visor.get():
        visor.insert(tk.END, ".")

def operacao(operador):
    global num1, operacaoSelecionada
    operacaoSelecionada = operador
    try:
        num1 = float(visor.get())
    except ValueError:
        num1 = 0
    # Caso o visor não seja float, apaga o visor, e insere o operador
    try:
        visor.get() == isinstance(float)
    except TypeError:
        visor.delete(0, tk.END)
        visor.insert(tk.END, operador)
        
def calcular():
    global num1, operacaoSelecionada
    try:
        num2 = float(visor.get())
    except ValueError:
        num2 = 0
    resultado = 0
    match operacaoSelecionada:
        case "+":
            resultado = num1 + num2
        case "-":
            resultado = num1 - num2
        case "×":
            resultado = num1 * num2
        case "÷":
            if num2 != 0:
                resultado = num1 / num2
            else:
                visor.delete(0, tk.END)
                visor.insert(tk.END, "Erro: Divisão por zero")
                return
    resultado_formatado = f"{resultado}".rstrip("0").rstrip(".") # .rstrip("0").rstrip(".") remove o zero e o ponto decimal caso estejam no final
    visor.delete(0, tk.END)
    visor.insert(tk.END, resultado_formatado)

janela = tk.Tk()
janela.title("Calculadora")

# Visor
visor = tk.Entry(janela, width=32, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Botões dos Números
botao_0 = tk.Button(
    janela,
    text="0", width=16,
    command=lambda: digitar("0")
)
botao_0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

botao_1 = tk.Button(
    janela, 
    text="1", width=6, 
    command=lambda: digitar("1")
)
botao_1.grid(row=4, column=0, padx=5, pady=5)

botao_2 = tk.Button(
    janela, 
    text="2", width=6, 
    command=lambda: digitar("2")
)
botao_2.grid(row=4, column=1, padx=5, pady=5)

botao_3 = tk.Button(
    janela, 
    text="3", width=6, 
    command=lambda: digitar("3")
)
botao_3.grid(row=4, column=2, padx=5, pady=5)

botao_4 = tk.Button(
    janela, 
    text="4", width=6, 
    command=lambda: digitar("4")
)
botao_4.grid(row=3, column=0, padx=5, pady=5)

botao_5 = tk.Button(
    janela, 
    text="5", width=6, 
    command=lambda: digitar("5")
)
botao_5.grid(row=3, column=1, padx=5, pady=5)

botao_6 = tk.Button(
    janela, 
    text="6", width=6, 
    command=lambda: digitar("6")
)
botao_6.grid(row=3, column=2, padx=5, pady=5)

botao_7 = tk.Button(
    janela, 
    text="7", width=6, 
    command=lambda: digitar("7")
)
botao_7.grid(row=2, column=0, padx=5, pady=5)

botao_8 = tk.Button(
    janela, 
    text="8", width=6, 
    command=lambda: digitar("8")
)
botao_8.grid(row=2, column=1, padx=5, pady=5)
    
botao_9 = tk.Button(
    janela, 
    text="9", width=6, 
    command=lambda: digitar("9")
)
botao_9.grid(row=2, column=2, padx=5, pady=5)

# Botões de funções
botao_soma = tk.Button(
    janela, 
    text="+", width=6, 
    command=lambda: operacao("+")
)
botao_soma.grid(row=3, column=3, padx=5, pady=5)

botao_subtracao = tk.Button(
    janela, 
    text="-", width=6, 
    command=lambda: operacao("-")
)
botao_subtracao.grid(row=2, column=3, padx=5, pady=5)

botao_multiplicacao = tk.Button(
    janela,
    text="×", width=6,
    command=lambda: operacao("×")
)
botao_multiplicacao.grid(row=1, column=3, padx=5, pady=5)

botao_divisao = tk.Button(
    janela,
    text="÷", width=6,
    command=lambda: operacao("÷")
)
botao_divisao.grid(row=1, column=2, padx=5, pady=5)

botao_igual = tk.Button(
    janela,
    text="=", width=6, height=4,
    command=lambda: calcular()
)
botao_igual.grid(row=4, rowspan=2, column=3, padx=5, pady=5)

botao_c = tk.Button(
    janela, 
    text="C", 
    width=6, 
    command=limpar
)
botao_c.grid(row=1, column=0, padx=5, pady=5)

botao_apagar = tk.Button(
    janela, 
    text="⌫", width=6, 
    command=lambda: apagar()
)
botao_apagar.grid(row=1, column=1, padx=5, pady=5)

botao_ponto = tk.Button(
    janela,
    text=".", width=6,
    command=lambda: ponto()
)
botao_ponto.grid(row=5, column=2, padx=5, pady=5)

janela.mainloop()