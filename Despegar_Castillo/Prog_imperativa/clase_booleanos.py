#ejercicio 1 
"""
Crear una función puede_ver_pelicula que tome como argumentos un número edad y un booleano tiene_autorizacion, y
devuelva si la persona está habilitada para ver la película.
Sólo puede ver la película si: tiene 15 años o más, o tiene autorización de sus padres.
"""
def puede_ver_pelicula(edad,tiene_autorizacion):
    return edad >= 15 or tiene_autorizacion
    print (puede_ver_pelicula(16,False))

    """
    Crear una función puede_avanzar que tome como argumento un string con el color del semáforo y 
    devuelva si puede avanzar.

puede_avanzar('verde')     # True
puede_avanzar('amarillo')  # False
puede_avanzar('rojo') 
"""
def puede_avanzar(color):
    if color= "verde"
        return puede avanzar
    if color = amarillo

# ejercicio alternativa condicional (clase)
    """
En nuestro curso nos acompañan docentes distintos los distintos dias.
Para darle una mano al equipo de logistica vamos a crear un programa que 
nos digaa nombre de quien debemos reservar el aula. 

Defini una funcion a_quien_le_toca que tomando un dia como parametro,
de vuelva el nombre del docente a cargo. 

PISTA: recordá que el lunes el equipo es el Fran y Ro y el jueves el de Ana y Dani

"""


def a_quien_le_toca (dia):
    if dia == "lunes"
        return "le toca a Ana y Dani"
    elif dia == "jueves"
        return "le toca a Fran y Ro"
    else:
        return "no hay clases"
    
    print(a_quien_le_toca("lunes"))


global delegado_por_anio = 0 
    def registrar_delegado_del_anio(delegado,año):
        list.appent(delegado_por_anio(registrar_delegado_del_anio(delegado,año)))
