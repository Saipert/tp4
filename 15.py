entrenadores_pokemon = [
    ["Azul", 6, 4, 12,  [
        ["Pidgeotto", 18, "Normal", "Volador"],
        ["Raticate", 17, "Normal", ""],
        ["Kadabra", 18, "Psíquico", ""],
        ["Wartortle", 20, "Agua", ""],
    ]],
    ["Lance", 13, 2, 39, [
        ["Charizard", 64, "Fuego", "Volador"],
        ["Gyarados", 64, "Agua", "Volador"],
        ["Tyrantrum", 66, "Roca", "Dragón"],
        ["Dragonite", 68, "Dragón", "Volador"],
        ["Dragonite", 70, "Dragón", "Volador"],
    ]],
    ["Máximo", 2, 2, 9, [
        ["Skarmory", 57, "Acero", "Volador"],
        ["Cradily", 56, "Roca", "Planta"],
        ["Armaldo", 56, "Roca", "Bicho"],
        ["Claydol", 58, "Tierra", "Psíquico"],
        ["Metagross", 61, "Acero", "Psíquico"],
        ]],
    ["Cintia", 15, 1, 54, [
        ["Roserade", 77, "Planta", "Veneno"],
        ["Spiritomb", 78, "Fantasma", "Siniestro"],
        ["Gastrodon", 76, "Agua", "Tierra"],
        ["Togekiss", 78, "Hada", "Volador"],
        ["Milotic", 79, "Agua", ""],
        ["Garchomp", 82, "Dragón", "Tierra"],
        ]],
    ["David", 8, 3, 27, [
        ["Scizor", 66, "Bicho", "Acero"],
        ["Rotom-Wash", 68, "Eléctrico", "Agua"],
        ["Weavile", 67, "Hielo", "Siniestro"],
        ["Colmilargo", 69, "Tierra", "Lucha"],
        ["Tapu Lele", 68, "Psíquico", "Hada"],
        ["Chandelure", 70, "Fantasma", "Fuego"],
        ]],
]


def cantidad_de_pokemons(entrenador):
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[0] == entrenador:
            return len(entrenador_pokemon[4])
    return 0


def entrenadores_mas_de_tres_torneos_ganados():
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[1] > 3:
            entrenadores.append(entrenador_pokemon[0])
    return entrenadores

def pokemon_mayor_nivel_del_mejor_entrenador():
    mejor_entrenador = None
    max_torneos_ganados = -1
    for entrenador_pokemon in entrenadores_pokemon:
        torneos_ganados = entrenador_pokemon[1]
        if torneos_ganados > max_torneos_ganados:
            max_torneos_ganados = torneos_ganados
            mejor_entrenador = entrenador_pokemon

    if mejor_entrenador:
        pokemon_mayor_nivel = max(mejor_entrenador[4], key=lambda x: x[1])
        return pokemon_mayor_nivel
    return None

def mostrar_entrenador_y_pokemons(entrenador):
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[0] == entrenador:
            return entrenador_pokemon
    return None

def entrenadores_con_porcentaje_de_batallas_ganadas():
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        total_batallas = entrenador_pokemon[2] + entrenador_pokemon[3]
        if total_batallas > 0:
            porcentaje_ganadas = (entrenador_pokemon[3] / total_batallas) * 100
            if porcentaje_ganadas > 79:
                entrenadores.append(entrenador_pokemon[0])
    return entrenadores

def entrenadores_con_pokemons_tipo_subtipo(tipo, subtipo):
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        for pokemon in entrenador_pokemon[4]:
            if (pokemon[2] == tipo and pokemon[3] == subtipo) or (pokemon[2] == "Agua" and pokemon[3] == "Volador"):
                entrenadores.append(entrenador_pokemon[0])
                break
    return entrenadores

def promedio_nivel_pokemons(entrenador):
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[0] == entrenador:
            pokemons = entrenador_pokemon[4]
            if len(pokemons) > 0:
                suma_niveles = sum([pokemon[1] for pokemon in pokemons])
                return suma_niveles / len(pokemons)
    return None

def cantidad_entrenadores_con_pokemon(pokemon_buscado):
    contador = 0
    for entrenador_pokemon in entrenadores_pokemon:
        for pokemon in entrenador_pokemon[4]:
            if pokemon[0] == pokemon_buscado:
                contador += 1
                break
    return contador

def entrenadores_con_pokemons_repetidos():
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        pokemons = entrenador_pokemon[4]
        nombres_pokemons = [pokemon[0] for pokemon in pokemons]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            entrenadores.append(entrenador_pokemon[0])
    return entrenadores

def entrenadores_con_pokemons_especificos(pokemons_buscados):
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        for pokemon in entrenador_pokemon[4]:
            if pokemon[0] in pokemons_buscados:
                entrenadores.append(entrenador_pokemon[0])
                break
    return entrenadores

def entrenador_tiene_pokemon(nombre_entrenador, nombre_pokemon):
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[0] == nombre_entrenador:
            for pokemon in entrenador_pokemon[4]:
                if pokemon[0] == nombre_pokemon:
                    return (entrenador_pokemon, pokemon)
    return None

print("a. Cantidad de Pokémons de Máximo:", cantidad_de_pokemons("Máximo"))
print("b. Entrenadores con más de tres torneos ganados:", entrenadores_mas_de_tres_torneos_ganados())
print("c. Pokémon de mayor nivel del mejor entrenador:", pokemon_mayor_nivel_del_mejor_entrenador())
print("d. Datos de David y sus Pokémons:", mostrar_entrenador_y_pokemons("David"))
print("e. Entrenadores con porcentaje de batallas ganadas mayor al 79%:", entrenadores_con_porcentaje_de_batallas_ganadas())
print("f. Entrenadores con Pokémons de tipo fuego y planta o agua/volador:")
print(entrenadores_con_pokemons_tipo_subtipo("Fuego", "Planta") + entrenadores_con_pokemons_tipo_subtipo("Agua", "Volador"))
print("g. Promedio de nivel de los Pokémons de Azul:", promedio_nivel_pokemons("Azul"))
print("h. Cantidad de entrenadores con el Pokémon 'Pikachu':", cantidad_entrenadores_con_pokemon("Pikachu"))
print("i. Entrenadores con Pokémons repetidos:", entrenadores_con_pokemons_repetidos())
print("j. Entrenadores con Tyrantrum, Terrakion o Wingull:", entrenadores_con_pokemons_especificos(["Tyrantrum", "Terrakion", "Wingull"]))

resultado = entrenador_tiene_pokemon("Cintia", "Togekiss")
if resultado:
    entrenador, pokemon = resultado
    print("k. Cintia tiene a 'Togekiss':")
    print("Nombre del entrenador:", entrenador[0])
    print("Cantidad de torneos ganados:", entrenador[1])
    print("Cantidad de batallas perdidas:", entrenador[2])
    print("Cantidad de batallas ganadas:", entrenador[3])
    print("Datos del Pokémon:")
    print("Nombre:", pokemon[0])
    print("Nivel:", pokemon[1])
    print("Tipo:", pokemon[2])
    print("Subtipo:", pokemon[3])
else:
    print("k. Cintia no tiene a 'Togekiss'.")
