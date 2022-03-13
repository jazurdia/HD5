import simpy
import random

def procesos(env, espera_inicio, nombre, cantidad_ram, cantidad_insutrcciones, instrucciones_ciclo, operaciones_ciclo, ram_inicial, nucleos):
    yield env.timeout(espera_inicio)
    tiempo_espera = env.now

    #print(nombre + " proceso en cola NEW. Tiempo: " + env.now + " cantidad de ram requerida: " + cantidad_ram + " cantidad disponible " + memoria.level)
    print("%s proceso en cola [NEW]. Tiempo: %d . Cantiadad de RAM requerida: %d . Cantidad de RAM disponible: %d" % (nombre, env.now, cantidad_ram, ram_inicial.level))
    yield ram_inicial.get(cantidad_ram)

    while cantidad_insutrcciones > 0:
        #print("%s proceso en cola [NEW] en %d cantidad de ram requerida %d, cantidad de ram disponible %d" % (nombre, env.now, cantidad_ram, memoria.level))
        #print('%s proceso en cola READY tiempo -> %d cantidad instrucciones pendientes %d' % (nombre, env.now, cantidad_instrucciones))
        print("%s proceso en cola [READY]. Tiempo: %d . Cantidad de instrucciones pendientes %d ." % (nombre, env.now, cantidad_insutrcciones))

        with nucleos.request() as req:
            yield req

            cantidad_insutrcciones -= instrucciones_ciclo
            yield env.timeout(operaciones_ciclo) #ciclos cada operacion

            #print(nombre + " proceso ne estado RUNNING ejecutado en tiempo: " + env.now + " usando " + cantidad_ram + " de RAM. Instrucciones pendientes: " + cantidad_insutrcciones + " RAM disponible: " + memoria.level)
            #print("%s proceso en cola ready, tiempo --> %d, cantidad de instrucciones pendientes %d" % (nombre, env.now, cantidad_instrucciones))
            print("%s proces en cola [READY] en tiempo %d. Cantidad de instrucciones pendientes %d" % (nombre, env.now, cantidad_insutrcciones))


    yield ram_inicial.put(cantidad_ram)

    global tiempo_total
    tiempo_total += env.now - tiempo_espera

    #print(nombre + " proceso terminado en tiempo: " + tiempo_total)
    #print("Cantidad de RAM devuelta: " + cantidad_ram)
    #print("Cantidad de memoria disponible: " + memoria.level) 

    print("%s proceso termiando en tiempo %d. Cantidad de RAM devuelta: %d. Cantidad de memoria disponible %d" & (nombre, env.now, cantidad_ram, ram_inicial.level))


#inicio Main
capacidad_ram = 100 #capacidad de la RAM
cantidad_procesos = 25 #cantidad de procesos
intervalos = 10
tiempo_total = 0 #empieza por 0, despues se sumara
instrucciones_ciclo = 3
operaciones_ciclo = 1


env = simpy.Environment() #Creando el ambiente de simulación
ram_inicial = simpy.Container(env, capacidad_ram, capacidad_ram)
nucleos = simpy.Resource(env, capacity=1)

for i in range(cantidad_procesos):
    espera_inicio = random.expovariate(1.0/10)
    cantidad_instrucciones = random.randint(1, 10)
    cantidad_ram = random.randint(1, 10)
    env.process(procesos(env=env, espera_inicio=espera_inicio, nombre="Proceso %d" % i, cantidad_ram=cantidad_ram, cantidad_insutrcciones=cantidad_instrucciones, instrucciones_ciclo=instrucciones_ciclo, operaciones_ciclo=operaciones_ciclo, ram_inicial=ram_inicial, nucleos=nucleos))

env.run()
tiempo_promedio = tiempo_total/cantidad_procesos
print("tiempo promedio: %d" % (tiempo_promedio))