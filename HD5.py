import simpy
import random

def procesos(env, espera_inicio, nombre, cantidad_ram, cantidad_insutrcciones, instrucciones_ciclo, operaciones_ciclo):
    yield env.timeout(espera_inicio)
    tiempo_espera = env.now()

    print(nombre + " proceso en cola NEW. Tiempo: " + env.now + " cantidad de ram requerida: " + cantidad_ram + " cantidad disponible " + memoria.level)
    yield memoria.get(cantidad_ram)

    while cantidad_insutrcciones > 0:
        print(nombre + " proceso en cola READY. Tiempo: " + env.now + " Cantidad de instrucciones pendientes: " + cantidad_insutrcciones)
        with cpu.request() as req:
            yield cpu

            cantidad_insutrcciones -= instrucciones_ciclo
            yield env.timeout(operaciones_ciclo) #ciclos cada operacion

            print(nombre + " proceso ne estado RUNNING ejecutado en tiempo: " + env.now + " usando " + cantidad_ram + " de RAM. Instrucciones pendientes: " + cantidad_insutrcciones + " RAM disponible: " + memoria.level)

    yield memoria.put(cantidad_ram)

    global tiempo_total
    tiempo_total += env.now - tiempo_espera

    print(nombre + " proceso terminado en tiempo: " + tiempo_total)
    print("Cantidad de RAM devuelta: " + cantidad_ram)
    print("Cantidad de memoria disponible: " + memoria.level) 


#inicio Main
