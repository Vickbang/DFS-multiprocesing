import threading
import time

# Definir el recurso compartido (zona critica)
recurso_compartido = 0

# Crear un mutex para controlar el acceso a la zona critca
mutex = threading.Lock()

# Crear un semaforo para limitar el acceso simultaneo a la zona critica
semaphore = threading.Semaphore(3) # Permitir hasta 3 procesos simultaneamente

# Funcion para simular el acceso a la zona critica
def proceso(id):
    global recurso_compartido
    print(f'Proceso {id} esperando para entrar a la zona critica')
    semaphore.acquire() # Intentar adquirir el semaforo
    print(f'Proceso {id} ha adquirido el semaforo')

    mutex.acquire() #Bloquear el mutex para acceder a la zona critica
    print(f'Proceso {id} ha adquirido el mutex')

    # Acceder a la zona critica
    recurso_compartido += 1
    print(f'Proceso {id} ha modificado el recurso compartido: {recurso_compartido}')
    time.sleep(1) # Simular una operacion en la zona critica

    mutex.release() # Liberar el mutex para permitir que otro proceso accede a la zona critica
    print(f'Proceso {id} ha liberado el mutex')

    semaphore.release() # Liberar el semaforo despues de salir de la zona critica
    print(f'Proceso {id} ha liberado el semaforo')

# Crear varios procesos para simular el acceso concurrente
num_procesos = 5
procesos = []
for i in range(num_procesos):
    proceso_actual = threading.Thread(target=proceso, args=(i,))
    procesos.append(proceso_actual)
    proceso_actual.start()

# Esperar a que todos los procesos
for proceso_actual in procesos:
    proceso_actual.join()

print('Todos los procesos han finalizado')