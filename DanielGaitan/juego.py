import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]

    print("=== Juego: Piedra, Papel o Tijera ===")
    print("Opciones: piedra, papel, tijera")
    
    jugador = input("Elige tu jugada: ").lower()
    if jugador not in opciones:
        print("⚠️ Opción no válida. Intenta de nuevo.")
        return

    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    if jugador == computadora:
        print("🤝 ¡Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("🎉 ¡Ganaste!")
    else:
        print("😢 Perdiste...")

if __name__ == "__main__":
    jugar()
