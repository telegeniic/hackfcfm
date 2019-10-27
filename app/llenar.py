from app import db
from app.models import *

def llenar():
    nombres = [
        'REYNA CASTRO', 
        'VALENTIN GUZMAN',
        'GILBERTO TENORIO',
        'CONSUELO VAZQUEZ',
        'DIANA CASTANEDA',
        'FRANCISCO HERNANDEZ',
        'RENE SALINAS',
        'ADRIAN MENDOZA',
        'MARIO TAPIA',
        'ERNESTO SOLIS'
    ]
    materias = [

        'LAB DE FISICA',
        'LAD DE PROGRA', 
        'PROGRA ESTRUCT',
        'FISICA',
        'MATEMATICAS DISCRETAS',
        'TOPICOS DE ALGEBRA',
        'CALCULO INTEGRAL'
    ]
    L= Materia(id=0, Nombre=materias[0])
    j = Maestro.query.get(1)
    L.materia.append(j)
    db.session.add(L)
    db.session.commit()

    L= Materia(id=1, Nombre=materias[1])
    j = Maestro.query.get(0)
    L.materia.append(j)
    db.session.add(L)
    db.session.commit()

    L= Materia(id=2, Nombre=materias[2] )
    j = Maestro.query.get(4)
    L.materia.append(j)
    db.session.add(L)
    db.session.commit()

    L= Materia(id=3, Nombre=materias[3])
    j = Maestro.query.get(5)
    L.materia.append(j)
    db.session.add(L)
    db.session.commit()

    L= Materia(id=4, Nombre=materias[4])
    j = Maestro.query.get(7)
    L.materia.append(j)
    db.session.add(L)
    db.session.commit()

    L= Materia(id=5, Nombre=materias[5])
    j = Maestro.query.get(3)
    L.materia.append(j)
    db.session.add(L)
    db.session.commit()

    L= Materia(id=6, Nombre=materias[6])
    j = Maestro.query.get(8)
    L.materia.append(j)
    db.session.add(L)
    db.session.commit()
    

