import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Triki")
root.geometry("750x650")
root.resizable(False, False)

turno = "X"

lbl_turno = tk.Label(root, text=f"Turno: {turno}", font=("Arial", 20))
lbl_turno.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

BTN_SIZE = 100
buttons = []

def verificar_ganador():
    # Convertimos los textos en matriz
    matriz = [[buttons[i][j]["text"] for j in range(3)] for i in range(3)]

    # Líneas ganadoras
    lineas = [
        # Filas
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # Columnas
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # Diagonales
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]

    for linea in lineas:
        a, b, c = linea
        v1 = matriz[a[0]][a[1]]
        v2 = matriz[b[0]][b[1]]
        v3 = matriz[c[0]][c[1]]

        if v1 != "" and v1 == v2 == v3:
            resaltar(linea)
            return v1  # devuelve X u O ganador

    # Empate
    if all(matriz[i][j] != "" for i in range(3) for j in range(3)):
        return "Empate"

    return None


def resaltar(linea):
    # Resaltar solo la línea ganadora
    for (i, j) in linea:
        buttons[i][j].config(bg="lightgreen")

    # Deshabilitar los demás botones
    for fila in buttons:
        for btn in fila:
            btn.config(state="disabled")


def on_click(i, j):
    global turno

    btn = buttons[i][j]
    if btn["text"] != "":
        return

    # Poner X u O
    btn.config(text=turno, state="disabled")

    # Verificar si alguien ganó
    ganador = verificar_ganador()
    if ganador == "X" or ganador == "O":
        lbl_turno.config(text=f"Ganó {ganador}!")
        return
    elif ganador == "Empate":
        lbl_turno.config(text="Empate!")
        return

    # Cambiar turno
    turno = "O" if turno == "X" else "X"
    lbl_turno.config(text=f"Turno: {turno}")


# Crear la matriz de botones
for i in range(3):
    fila = []
    for j in range(3):
        btn = tk.Button(
            frame,
            text="",
            width=4,
            height=2,
            font=("Arial", 32),
            bg="white",
            command=lambda i=i, j=j: on_click(i, j)
        )
        btn.grid(row=i, column=j, padx=5, pady=5)
        fila.append(btn)
    buttons.append(fila)


def reiniciar():
    global turno
    turno = "X"
    lbl_turno.config(text=f"Turno: {turno}")

    for fila in buttons:
        for btn in fila:
            btn.config(text="", state="normal", bg="white")


btn_reiniciar = tk.Button(root, text="Reiniciar", font=("Arial", 16), command=reiniciar)
btn_reiniciar.pack(pady=30)

root.mainloop()
