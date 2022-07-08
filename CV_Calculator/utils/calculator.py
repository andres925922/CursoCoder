
import math


def diff_pressure(p1,p2):
    return p2-p1

def cv_calculator(Q,p1,p2,grav_esp):
    """
    * Q : caudal que recorre la válvula en GPM (Galones por minuto)
    * p1 : corresponde a la presión a la entrada de la válvula
    * p2 : corresponde a la presión a la salida de la válvula
    * grav_esp : gravedad específica del fluido

    La función devuelve el valor del CV calculado
    """
    delta_P = diff_pressure(p1,p2)

    return Q * math.sqrt(grav_esp / delta_P)