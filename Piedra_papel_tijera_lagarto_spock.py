import random

'''
Este ejercicio simula el juego de 'Piedra', 'Papel', 'Tijera', 'Lagarto', y 'Spock'. Del juego del mismo nombre visto en la Serie 'The Big Bang Theory'.
'''


# Esta funcion devuelve el movimiento seleccionado por el usuario
def selectMovimiento() -> str:
    while True:  # Un ciclo que se repetira hasta que se ingrese un numero valido
        try:
            index = int(input("Seleccione su movimiento: "))
            if index >= 1 and index <= 5:
                return index
            elif index < 1:
                print("¡¡EL MOVIMIENTO SELECCIONADO DEBE SER MAYOR A 0!!")
            else:
                print("¡¡EL MOVIMIENTO SELECCIONADO DEBE SER ENTRE 1 Y 5!!")
        except Exception as exception:
            print("¡¡ERROR: DEBE INGRESAR UN NUMERO ENTERO!!")


# Diccionario con la lista de movimiento y contra que movimiento es efectivo.
TablaMovimientos = {"Piedra": ["Tijera", "Lagarto"], "Papel": ["Piedra", "Spock"], "Tijera": [
    "Papel", "Lagarto"], "Lagarto": ["Papel", "Spock"], "Spock": ["Piedra", "Tijera"]}

# Muestra la lista de movimiento
print("Movimientos disponibles:")
for index, item in enumerate(TablaMovimientos):
    print(f"— {index + 1}. {item}")

# Pide al usuario seleccionar un movimiento
movimiento_Jugador = list(TablaMovimientos)[selectMovimiento() - 1]
# El oponente selecciona un movimiento randon
movimiento_CPU = list(TablaMovimientos)[random.randrange(0, 5)]

# Muestra el resultado
print(f"\nTu elegiste: —{movimiento_Jugador}—.\n" +
      f"El oponente eligió: —{movimiento_CPU}—.\n\n" +
      "Resultado:")

if movimiento_Jugador == movimiento_CPU:
    print("——Empate——.")
elif movimiento_CPU in TablaMovimientos[movimiento_Jugador]:
    print(f"——Ganaste——")
else:
    print(f"——Perdiste——")