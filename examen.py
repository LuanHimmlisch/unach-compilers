from ply import lex
import ply.yacc as yacc
import tkinter as tk
import re

totals = {
    'Palabras Reservadas': [],
    'IDS': [],
    'Operadores': [],
    'Simbolos': [],
}

reserved = {
   'int': 'TYPE_INT',
   'read': 'KEY_READ',
   'end': 'KEY_END',
   'programa': 'KEY_FUNCTION',
}

simbols = {
   '(': 'LPAREN',
   ')': 'RPAREN',
   '{': 'LBRACKET',
   '}': 'RBRACKET',
   ';': 'SEMICOLON',
   ':': 'DUAL',
   ',': 'COMMA'
}

operators = {
    '+': 'PLUS',
    '-': 'MINUS',
    '*': 'MULTIPLY',
}

t_EQUALS = r'=';

def t_RESERVED(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'


    t.type = reserved.get(t.value, 'ID')

    if t.type != 'ID':
        totals['Palabras Reservadas'].append(t.value)
    elif t.value not in totals['IDS']:
        totals['IDS'].append(t.value)

    return t

def t_SIMBOLS(t):
    r'\(|\)|\{|\}|\:|\;|\,'

    t.type = simbols.get(t.value)
    
    totals['Simbolos'].append(t.value)
    
    return t

def t_OPERATORS(t):
    r'(\+|-|\*)'

    totals['Operadores'].append(t.value)

    return t


t_NUMBER = '\d+';
t_STRING = '(\"[^\"]+\")|(\'[^\']+\')';

tokens = [
    'RESERVED',
    'SIMBOLS',
    'EQUALS',
    'ID',
    'NUMBER',
    'OPERATORS',
    'STRING',
] + list(reserved.values()) + list(simbols.values()) + list(operators.values())

lexer = lex.lex()

def p_variable(p):
    '''
    assignment :  ID EQUALS NUMBER
           |  ID EQUALS expression
    expression : expression OPERATORS expression
           | LPAREN expression RPAREN
           | NUMBER
           | ID
    '''
    # p[0] = p[3]


# parser = yacc.yacc()

def analizar(entrada):
    identificador = []
    matches = []

    while True:
        if (len(entrada.strip()) == 0): break;

        input = entrada.strip()

        lexer.input(input)
        
        tok = None

        try:
            tok = lexer.token()
            # tok = parser.parse(input, lexer=lexer)
        except Exception as e:
            pass

        if not tok: 
            identificador.append((entrada, "<No definido>"));
            break

        identificador.append((tok.value, f"<Reservada {tok.type}>"))
        entrada = entrada.replace(tok.value, "", 1)

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
    
    for key,value in totals.items():
        resultado_texto.insert(tk.END, f"\n{key}: {len(value)}")
    
    resultado_texto.insert(tk.END, f"\n\n Totales: {numero_reservadas}\n")
    # end for

ventana = tk.Tk()
ventana.geometry("670x580")
ventana.title("Analizador Léxico")
ventana.config(bg="#12657f")

entrada_texto = tk.Text(ventana, font=("Arial", 12), bg="white", fg="black", height=10, width=60)
entrada_texto.place(x=60, y=40)

boton_analizar = tk.Button(ventana, text="Analizar", font=("Arial", 12), bg="#121b29", fg="white", command=analizar_codigo)
boton_analizar.place(x=60, y=240)

resultado_texto = tk.Text(ventana, font=("Arial", 12), bg="white", fg="black", height=10, width=60)
resultado_texto.place(x=60, y=300)

ventana.mainloop()
