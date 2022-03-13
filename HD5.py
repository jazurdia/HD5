import simpy
import random

def procesos(env, espera_inicio, nombre, cantidad_ram, cantidad_insutrcciones, instrucciones_ciclo, operaciones_ciclo):
    yield env.timeout(espera_inicio)
    tiempo_espera = env.now

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
capacidad_ram = 100 #capacidad de la RAM
cantidad_nucleos = 1 #cantidad de nucleos
cantidad_procesos = 25 #cantidad de procesos
intervalos = 10
tiempo_total = 0 #empieza por 0, despues se sumara
instrucciones_ciclo = 3
operaciones_ciclo = 1


env = simpy.Environment() #Creando el ambiente de simulación
ram_inicial = simpy.Container(env, capacidad_ram, capacidad_ram)
nucleos = simpy.Resource(env, capacity=cantidad_nucleos)

for i in range(cantidad_procesos):
    espera_inicio = random.expovariate(1.0/10)
    cantidad_instrucciones = random.randint(1, 10)
    cantidad_ram = random.randint(1, 10)
    env.process(procesos(env=env, espera_inicio=espera_inicio, nombre=i, cantidad_ram=cantidad_ram, cantidad_insutrcciones=cantidad_instrucciones, instrucciones_ciclo=instrucciones_ciclo, operaciones_ciclo=operaciones_ciclo))

env.run()
tiempo_promedio = tiempo_total/cantidad_procesos
print("tiempo promedio: " + tiempo_promedio)