persona_1 = {
    'nombre': 'Sara',
    'edad': 29,
    'cedula': '115820287'
}
persona_2 = {
    'nombre': 'Oscar',
    'edad': 15,
    'cedula': '112310501'
}
persona_3 = {
    'nombre': 'Mario',
    'edad': 28,
    'cedula': '111020253'
}
persona_4 = {
    'nombre': 'Joshi',
    'edad': 23,
    'cedula': '123456789'
}
personas = [persona_1, persona_2, persona_3, persona_4]

for p in personas:

    print(p['nombre'], ' tiene ', p['edad'], ' años y su cédula es ', p['cedula'])