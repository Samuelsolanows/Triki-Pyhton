import tkinter as tk
from tkinter import messagebox



def matrizvector(t, turno, casilla):
    match casilla:
        case 1:
            i, j = 0, 0
        case 2:
            i, j = 0, 1
        case 3:
            i, j = 0, 2
        case 4:
            i, j = 1, 0
        case 5:
            i, j = 1, 1
        case 6:
            i, j = 1, 2
        case 7:
            i, j = 2, 0
        case 8:
            i, j = 2, 1
        case 9:
            i, j = 2, 2
        case _:
            return
    
    t[i][j] = 1 if turno == "X" else -1


def asignarturno(ficha):
    if ficha == "X" or ficha == "x":
        fa = "O"
    else:
        if ficha == "O" or ficha == "o":
            fa = "X"
    return fa


def sumacolummas(t):
    gc = 0
    sc = [0 for _ in range(3)]
    for i in range(1, 4):
        sc[i-1] = t[i-1][0] + t[i-1][1] + t[i-1][2]
        if sc[i-1] == 3 or sc[i-1] == -3:
            gc = sc[i-1]
    return gc


def sumafilas(t):
    gf = 0
    sf = [0 for _ in range(3)]
    for i in range(1, 4):
        sf[i-1] = t[0][i-1] + t[1][i-1] + t[2][i-1]
        if sf[i-1] == 3 or sf[i-1] == -3:
            gf = sf[i-1]
    return gf


def sumadiagonales(t):
    gd = 0
    sd = [0.0 for _ in range(2)]
    sd[0] = t[0][0] + t[1][1] + t[2][2]
    sd[1] = t[2][0] + t[1][1] + t[0][2]
    for i in range(1, 3):
        if sd[i-1] == 3 or sd[i-1] == -3:
            gd = sd[i-1]
    return gd


def verificarganador(t):
    g = 0
    if sumacolummas(t) == 3 or sumafilas(t) == 3 or sumadiagonales(t) == 3:
        g = 3
    if sumacolummas(t) == -3 or sumafilas(t) == -3 or sumadiagonales(t) == -3:
        g = -3
    return g



# Variables globales
turno = "X"
nj = 1
t = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(0)
    t.append(fila)

p = []
for i in range(9):
    p.append("-")

ganador = 0

ventana = tk.Tk()
ventana.title("Triki")
ventana.config(bg="#121212")
ventana.iconbitmap("img/triki.ico")

# Crear frame para organizar la matriz
frame = tk.Frame(ventana)
frame.pack(padx=20, pady=20, fill="both", expand=True)
frame.config(bg="#1F1F1F")
for i in range(3):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)


def jugar(fila, columna):
    global turno, nj, ganador, color_texto
    
    # Calcular la casilla (1-9)
    casilla = fila * 3 + columna + 1
    
    # Verificar si la casilla está disponible
    if p[casilla - 1] != "-":
        return
    

    # CAmbiar el texto del boton dependiendo el turno
    if turno == "X":
        color_texto = "#FF1744"  
    else:
        color_texto = "#2979FF" 
        
    botones[fila][columna].config(text=turno,font=("Arial", 20, "bold"),fg=color_texto, disabledforeground=color_texto)
    botones[fila][columna].config(state="disabled")
    
    # Actualizar la matriz y el vector
    p[casilla - 1] = turno
    matrizvector(t, turno, casilla)
    if nj > 4:
        ganador = verificarganador(t)
        if ganador == 3:
            messagebox.showinfo("¡Ganador!", "¡Ganador: X!")
            return
        elif ganador == -3:
            messagebox.showinfo("¡Ganador!", "¡Ganador: O!")
            return
    
    nj += 1
    
    if nj > 9:
        messagebox.showinfo("Empate", "¡El juego ha terminado en empate!")
        reiniciar_juego()
        return
    

    turno = asignarturno(turno)


def reiniciar_juego():
    global turno, nj, t, p, ganador
    turno = "X"
    nj = 1
    ganador = 0
    t = [] # Tablero
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(0)
        t.append(fila)
    p = [] # Vector
    for i in range(9):
        p.append("-")
    
    for fila in range(3):
        for columna in range(3):
            botones[fila][columna].config(text="", state="normal")



botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(frame,
                          command=lambda f=fila, c=columna: jugar(f, c),
                          text="", width=10, height=3,
                          font=("Arial", 20, "bold"),
                          bg="#2D2D2D", activebackground="#424242")
        boton.grid(row=fila, column=columna, padx=5, pady=5)
        fila_botones.append(boton)
    botones.append(fila_botones)

# Botón para reiniciar el juego
boton_reiniciar = tk.Button(ventana, text="Reiniciar Juego", 
                            command=reiniciar_juego, 
                            font=("Arial", 12, "bold"),
                            bg="#00C853", fg="white", 
                            padx=20, pady=10)
boton_reiniciar.pack(pady=10)

ventana.mainloop()