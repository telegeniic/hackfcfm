from app import models

class Generate():
    def entradasIguales(clases):
        if (clases.Horario.Lunes.entrada == \
            clases.Horario.Martes.entrada == \
            clases.Horario.Miercoles.entrada == \
            clases.Horario.Jueves.entrada == \
            clases.Horario.Viernes.entrada 
        ):
            return True
        else:
            return False

    def salidasIguales(clases):
        if (clases.Horario.Lunes.salida == \
            clases.Horario.Martes.salida == \
            clases.Horario.Miercoles.salida == \
            clases.Horario.Jueves.salida == \
            clases.Horario.Viernes.salida 
        ):
            return True
        else:
            return False