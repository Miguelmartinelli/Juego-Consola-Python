import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador


def main():
    nombre_jugador = input(
        "Holusssss bienvenido a Guerra de las Galaxias. Ingresa tu nombre: "
    )
    jugador = Jugador(nombre_jugador)

    enemigos = [
        Enemigo("Arsehole", 50, 10),
        Enemigo("Silvia Cipolla", 70, 15),
        Enemigo("Roxana Bueno", 30, 5),
    ]
    enemigos_derrotados = []

    print("a jugar, se te viene la noche fiscal")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue
        print(f" Te encuentras con {enemigo_actual.nombre} en tu camino")

        while enemigo_actual.salud > 0:
            accion = input("Que joraca hacemos? (atacar/ huir): ").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(f"atacaste a {enemigo_actual.nombre}  y le causaste {dano_jugador} de daño")
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(f"{enemigo_actual.nombre} te ataco y te causo {dano_enemigo} de dano")                
                    jugador.recibir_dano(dano_enemigo)
                    
            elif accion == "huir":
                print("Te cagaste en las patas y te fuiste, GIL!")
                break

        if jugador.salud <= 0:
            print("perdiste bro")
            break

        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        jugador.ganar_experiencia(20)

        continuar = input("queres seguir explorando? (si/no): ").lower()
        if continuar != "si":
            print("Gracias por haber jugado la Guerra de las Galaxias")
            break

    if not enemigos:
        print(f"ganaste {nombre_jugador} ")

if __name__ == "__main__":
    main()