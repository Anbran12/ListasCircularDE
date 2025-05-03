class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None

class JuegoUNO:
    def __init__(self):
        self.inicio = None
        self.direccion_normal = True  # True = sentido horario, False = antihorario
        self.jugador_actual = None

    def agregar_jugador(self, nombre):
        nuevo = Jugador(nombre)
        if self.inicio is None:
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
            self.inicio = nuevo
        else:
            ultimo = self.inicio.anterior
            nuevo.siguiente = self.inicio
            nuevo.anterior = ultimo
            ultimo.siguiente = nuevo
            self.inicio.anterior = nuevo
        self.jugador_actual = self.inicio

    def mostrar_jugadores(self):
        print("Jugadores en la mesa:")
        if self.inicio is None:
            return
        actual = self.inicio
        while True:
            print(f"- {actual.nombre}")
            actual = actual.siguiente
            if actual == self.inicio:
                break

    def siguiente_turno(self):
        if self.direccion_normal:
            self.jugador_actual = self.jugador_actual.siguiente
        else:
            self.jugador_actual = self.jugador_actual.anterior
        print(f"Turno de: {self.jugador_actual.nombre}")

    def jugar_reverse(self):
        self.direccion_normal = not self.direccion_normal
        direccion = "sentido horario" if self.direccion_normal else "sentido antihorario"
        print(f"¡Carta Reverse jugada! Ahora el turno va en {direccion}.")

    def simular_juego(self, pasos, reverse_en=None):
        print(f"Comenzando con: {self.jugador_actual.nombre}")
        for i in range(1, pasos + 1):
            if reverse_en and i in reverse_en:
                self.jugar_reverse()
            self.siguiente_turno()


# Agregar jugadores
juego = JuegoUNO()
jugadores = ["Player 1", "Player 2", "Player 3", "Player 4"]
for nombre in jugadores:
    juego.agregar_jugador(nombre)

juego.mostrar_jugadores()
print("\n--- Simulación de turnos ---")

# Simular 10 turnos, con Reverse en los turnos 4 y 8
juego.simular_juego(pasos=20, reverse_en=[4, 8, 15])
