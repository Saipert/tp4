superheroes = [
    {
        'nombre': 'Linterna Verde',
        'anio_aparicion': 1940,
        'casa_comic': 'DC',
        'biografia': 'Hal Jordan, un piloto de pruebas, es elegido por el anillo del moribundo alienígena Abin Sur, para convertirse en el primer humano seleccionado para el Cuerpo de Linternas Verdes, y el enfrentamiento con sus nuevos poderes, contra Parallax, quién amenaza con destruir el universo.',
    },
    {
        'nombre': 'Wolverine',
        'anio_aparicion': 1974,
        'casa_comic': 'Marvel',
        'biografia': 'Es un mutante que posee sentidos afinados a los animales, capacidades físicas mejoradas, poderosa capacidad de regeneración conocida como un factor de curación, y tres garras retráctiles en cada mano.',
    },
    {
        'nombre': 'Superman',
        'anio_aparicion': 1938,
        'casa_comic': 'DC',
        'biografia': 'Superman es un hombre alto, musculoso, hombre de raza blanca con ojos azules y pelo negro corto con un rizo. Superman, siempre lleva su traje azul con su famoso rojo y amarillo escudo de S en el pecho, un cinturón amarillo, botas rojas y una capa roja.',
    },
    {
        'nombre': 'Spider-Man',
        'anio_aparicion': 1962,
        'casa_comic': 'Marvel',
        'biografia': 'Sus características eran principalmente azul oscuro con guantes, botas, sección media, y máscara color rojo. Peter diseñó un patrón de telaraña que cubrirá las porciones rojas del traje, empezando desde la máscara.',
    },
    {
        'nombre': 'Wonder Woman',
        'anio_aparicion': 1941,
        'casa_comic': 'DC',
        'biografia': 'Tiene un título avanzado en ingeniería eléctrica, es un especialista con experiencia y un talentoso actor. También es excepcionalmente rico, siendo el dueño de su propia compañía de armas privada y una exitosa estrella de cine.',
    },
    {
        'nombre': 'Iron Man',
        'anio_aparicion': 1963,
        'casa_comic': 'Marvel',
        'biografia': 'Iron Man es uno de los superhéroes más icónicos de Marvel Comics. Su alter ego, Tony Stark, es un multimillonario industrial que crea una armadura sofisticada para luchar contra el crimen y salvar al mundo. Una de las hazañas más destacadas de Iron Man es su capacidad para volar a altas velocidades gracias a su traje.',
    },
    {
        'nombre': 'Flash',
        'anio_aparicion': 1940,
        'casa_comic': 'DC',
        'biografia': 'Jay Garrick era un estudiante universitario en 1938 que accidentalmente inhaló vapores de agua pesada después de tomar un descanso para fumar dentro de su laboratorio donde había estado trabajando.​ Como resultado, descubrió que podía correr a una velocidad sobrehumana y que tenía reflejos igualmente rápidos.',
    },
    {
        'nombre': 'Thor',
        'anio_aparicion': 1962,
        'casa_comic': 'Marvel',
        'biografia': 'Thor era uno de los dioses nórdicos más conocidos. Era el más fuerte de los dioses, protegía a la juventud, al rayo, al fuego y a la arquitectura.',
    },
]

def eliminar_superheroe(nombre):
    for superheroe in superheroes:
        if superheroe['nombre'] == nombre:
            superheroes.remove(superheroe)
            break

def anio_aparicion(nombre):
    for superheroe in superheroes:
        if superheroe['nombre'] == nombre:
            return superheroe['anio_aparicion']
    return None

def cambiar_casa(nombre, nueva_casa):
    for superheroe in superheroes:
        if superheroe['nombre'] == nombre:
            superheroe['casa_comic'] = nueva_casa
            break


def superheroes_con_palabra_en_biografia(palabra):
    nombres = []
    for superheroe in superheroes:
        if palabra in superheroe['biografia'].lower(): 
            nombres.append(superheroe['nombre'])
    return nombres


def superhéroes_anteriores_a(anio):
    superheroes_anteriores = []
    for superheroe in superheroes:
        if superheroe['anio_aparicion'] < anio:
            superheroes_anteriores.append((superheroe['nombre'], superheroe['casa_comic']))
    return superheroes_anteriores


def casa_de_superheroes(nombres):
    casas = {}
    for superheroe in superheroes:
        if superheroe['nombre'] in nombres:
            casas[superheroe['nombre']] = superheroe['casa_comic']
    return casas


def informacion_superheroes(nombres):
    informacion = {}
    for superheroe in superheroes:
        if superheroe['nombre'] in nombres:
            informacion[superheroe['nombre']] = superheroe
    return informacion


def superheroes_por_letra(letras):
    nombres = []
    for superheroe in superheroes:
        if superheroe['nombre'][0].upper() in letras:  
            nombres.append(superheroe['nombre'])
    return nombres


def contar_superheroes_por_casa():
    conteo = {'Marvel': 0, 'DC': 0}
    for superheroe in superheroes:
        casa = superheroe['casa_comic']
        conteo[casa] += 1
    return conteo

eliminar_superheroe('Linterna Verde')
print("Año de aparición de Wolverine:", anio_aparicion('Wolverine'))
cambiar_casa('Dr. Strange', 'Marvel')
print("Superhéroes con 'traje' o 'armadura' en su biografía:", superheroes_con_palabra_en_biografia('traje'))
print("Superhéroes anteriores a 1963:", superhéroes_anteriores_a(1963))
print("Casa de Capitana Marvel y Mujer Maravilla:", casa_de_superheroes(['Capitana Marvel', 'Mujer Maravilla']))
print("Información de Flash y Star-Lord:")
for nombre, info in informacion_superheroes(['Flash', 'Star-Lord']).items():
    print(nombre, ":", info)
print("Superhéroes que comienzan con B, M y S:", superheroes_por_letra(['B', 'M', 'S']))
casa_count = contar_superheroes_por_casa()
print("Cantidad de superhéroes de Marvel:", casa_count['Marvel'])
print("Cantidad de superhéroes de DC:", casa_count['DC'])

