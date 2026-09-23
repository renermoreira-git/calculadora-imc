import tkinter as tk

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora IMC")
janela.geometry("400x400")

# Título
titulo = tk.Label(
    janela,
    text="CALCULADORA IMC",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=30)

# Peso
label_peso = tk.Label(
    janela,
    text="Peso (kg):",
    font=("Arial", 12)
)
label_peso.pack()

entrada_peso = tk.Entry(
    janela,
    font=("Arial", 12)
)
entrada_peso.pack(pady=5)

# Altura
label_altura = tk.Label(
    janela,
    text="Altura (m):",
    font=("Arial", 12)
)
label_altura.pack(pady=(15, 0))

entrada_altura = tk.Entry(
    janela,
    font=("Arial", 12)
)
entrada_altura.pack(pady=5)

# Resultado
label_imc = tk.Label(
    janela,
    text="IMC: --",
    font=("Arial", 12, "bold")
)
label_imc.pack(pady=5)

label_resultado = tk.Label(
    janela,
    text="Resultado: --",
    font=("Arial", 12, "bold")
)
label_resultado.pack(pady=5)



def calcular():

    altura = float(entrada_altura.get())
    peso = float(entrada_peso.get())

    imc = peso / (altura ** 2)

    label_imc.config(
        text= str(imc)
    )

    if imc < 18.5:
        resultado = "Abaixo do peso"
    elif imc < 25:
        resultado = "Peso Normal"
    elif imc < 30:
        resultado = "Sobrepeso"
    else:
        resultado = "Obesidade"

    label_resultado.config(
        text=str(resultado)
    )

# Botão
botao = tk.Button(
    janela,
    text="CALCULAR",
    font=("Arial", 12, "bold"),
    command=calcular
)
botao.pack(pady=25)

# Mantém a janela aberta
janela.mainloop()