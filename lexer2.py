import re
import tkinter as tk

keywords = ["public", "static", "void", "main"]

delimiters = ["(", ")", "{", "}", ".", ";"]

types = ["int"]

def checkKeyword(token):
    for keyword in keywords:
        matches = re.findall(keyword, token)
        if (len(matches) > 0):
            return matches[0]
    return False

def checkNumeric(token):
    matches = re.findall(r"\d+", token)
    for match in matches:
        if (len(matches) > 0):
            return matches[0]
    return False

def checkType(token):
    for type in types:
        matches = re.findall(type, token)
        if (len(matches) > 0):
            return matches[0]
    return False

def checkDelimiters(token):
    for delimiter in delimiters:
        matches = re.findall("\\" + delimiter, token)
        if (len(matches) > 0):
            return matches[0]
    return False

def analizeToken(token, found = [], index = 0):
    prev = None
    if (index > 0): prev = found[index-1]

    
    result = checkKeyword(token)

    if (result): return (result, 'Reservado')

    result = checkDelimiters(token)

    if(result): return (result, 'Delimitador')

    result = checkNumeric(token)
    
    if (result): return (result, 'Númerico')

    result = checkType(token)
    
    if (result): return (result, 'Tipo')

    if (prev):
        if (prev[1] == 'Tipo'):
            return (token, 'Identificador')
        
        if (token == '=' and prev[1] == 'Identificador'):
                return (token, 'Asignación')

    return (token, False)

def analize(entrada):
    splitRegex = r"\w+|=";
    for delimiter in delimiters:
        splitRegex += "|\\" + delimiter
    
    tokens = re.findall(f"({splitRegex})", entrada.strip())
    allFounds = []

    for i,token in enumerate(tokens):
        last = None
        if (len(allFounds) > 0):
            last = allFounds[len(allFounds) - 1]
        
        founds = analizeToken(token,allFounds, i)
        allFounds.append(founds)

    for i,found in enumerate(allFounds):
        if (not found[1]):
            allFounds[i] = (found[0], f"<No identificado>")
        else:
            allFounds[i] = (found[0], f"<{found[1]}>")
    # end for
    
    return allFounds
    

def analizar_codigo():
    codigo = entrada_texto.get("1.0", tk.END)
    entrada = codigo.split("\n")
    token_totales = []
    for i, linea in enumerate(entrada):
        tokens_linea = analize(linea)
        for token, tipo in tokens_linea:
            token_totales.append((i+1, token, tipo))

    resultado_texto.delete("1.0", tk.END)
    for numero_linea, token, tipo in token_totales:
        resultado_texto.insert(tk.END, f"Linea {numero_linea}\n{tipo}  '{token}'\n")

    numero_reservadas = len([token for _, _, tipo in token_totales if tipo.startswith("<Reservada")])
    #resultado_texto.insert(tk.END, f"\nPalabra reservada: {numero_reservadas}\n")

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