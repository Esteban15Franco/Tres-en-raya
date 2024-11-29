tablero = [[' ' for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    print("\nel tablero")
    for fila in tablero:
        print("   |   ".join(fila))
        print("-" * 18)


def realizar_movimientos(simbolo):
    while True:
        try:
            fila = int(input(f"Seleccione la fila (0, 1, 2) para colocar {simbolo}: "))
            columna = int(input(f"Seleccione la columna (0, 1, 2) para  colocar {simbolo}: "))

            if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                print("Posicion fuera de rango. Intente nuevamente...")
            elif tablero[fila][columna] != ' ':
                print("La posicion esta ocupada. Intente nuevamente...")
            else:
                tablero[fila][columna] = simbolo
                break
        except ValueError:
            print("Por favor ingrese numeros enteros validos")


def validar_ganador():
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != " ":
            return fila[0]

    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
            return tablero[0][col]

    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return tablero[0][0]

    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return tablero[0][2]


    return None

def jugar():
    turno = "X"
    mov_realizado = 0

    while True:
        mostrar_tablero()
        realizar_movimientos(turno)

        ganador = validar_ganador()
        if ganador:
            mostrar_tablero()
            print(f"El ganador es el jugador {ganador}!!!")
            break

        mov_realizado += 1

        if mov_realizado == 9:
            print("Es un empate!!!")
            break

        turno = "O" if turno == "X" else "X"


if __name__ == '__main__':
    jugar()



