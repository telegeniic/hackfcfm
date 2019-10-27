from app import db
from app.models import *

class Contruir():
    clases = []
    grupos = []

    def construct(self, Hi, Hf):
        dH = Hf - Hi
        i = 0
        while len(clases) != dH :
            group = Grupo.query.get(i)
            
            if group.horario.lunes.empieza() > Hi:
                grupos.append(group.id)
                clases.append(Materia.query.get(group.materia()))
                i += 1
        return clases

