from ply import lex
import tkinter as tk

tokens = (
    'FOR',
    'DO',
    'WHILE',
    'IF',
    'ELSE',
)

t_FOR = r'\bfor\b'
t_DO = r'\bdo\b'
t_WHILE = r'\bwhile\b'
t_IF = r'\bif\b'
t_ELSE = r'\belse\b'


lexer = lex.lex()

def analizar(entrada):
    identificador = []
    lexer.input(entrada)
    matches = []

    while True:
        tok = None
        try:
            tok = lexer.token()
            matches.append(tok.value)
        except Exception as e:
            pass

        if not tok: break
        
    for match in matches:
        identificador.append((match, f"<Reservada {match}>"))
        entrada = entrada.replace(match, "", 1)

    if len(entrada) > 0:
        identificador.append((entrada, "<No definido>"))
    return identificador

def analizar_codigo():
    codigo = entrada_texto.get("1.0", tk.END)
    entrada = codigo.split("\n")
    token_totales = []
    for i, linea in enumerate(entrada):
        tokens_linea = analizar(linea)
        for token, tipo in tokens_linea:
            token_totales.append((i+1, token, tipo))

    resultado_texto.delete("1.0", tk.END)
    for numero_linea, token, tipo in token_totales:
        resultado_texto.insert(tk.END, f"Linea {numero_linea}\n{tipo}  Simbolo {token}\n")

    numero_reservadas = len([token for _, _, tipo in token_totales if tipo.startswith("<Reservada")])
    resultado_texto.insert(tk.END, f"\nPalabra reservada: {numero_reservadas}\n")

ventana = tk.Tk()
ventana.geometry("500x580")
ventana.title("Analizador Léxico")
ventana.config(bg="#12657f")

entrada_texto = tk.Text(ventana, font=("Arial", 12), bg="white", fg="black", height=10, width=40)
entrada_texto.place(x=60, y=40)

boton_analizar = tk.Button(ventana, text="Analizar", font=("Arial", 12), bg="#121b29", fg="white", command=analizar_codigo)
boton_analizar.place(x=60, y=240)

resultado_texto = tk.Text(ventana, font=("Arial", 12), bg="white", fg="black", height=10, width=40)
resultado_texto.place(x=60, y=300)

ventana.mainloop()
