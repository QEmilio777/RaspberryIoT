# import asyncio
# import time

# start = None
# end = None

# async def greet():
#     print("Comienza a contar")
#     # time.sleep(5)
#     await asyncio.sleep(5)
#     print("Termina de contar")
#     return "Hi"

# async def otra_cosa():
#     print("hago otra cosa")


# async def main():
#     start = time.time()
#     await asyncio.gather(greet(), otra_cosa())
#     end = time.time()
#     print(f"Tiempo: {end-start}")

# asyncio.run(main())


# import asyncio
# import time

# inicio = None
# fin = None

# async def task(n_task):
#     print(f"Starting task {n_task}")
#     print("Tree seconds started")
#     inicio = time.time()
#     await asyncio.sleep(3)
#     print(f"Waiting for task {n_task} to be completed")
#     print(f"Task {n_task} completed")
#     fin = time.time()
#     print(f"Task {n_task} completed in {fin-inicio}")

# async def main():
#     await asyncio.gather(task(1), task(2))
#     return "fin de la ejecucion"

# resultado = asyncio.run(main())
# print(resultado)



# async def one():
#     print("Aun no retorno la primera")
#     await asyncio.sleep(5)
#     print("retorno primera")
#     return ""

# async def two():
#     print("retorno segunda")
#     print("Espera de 3 segundos en la segunda")
#     await asyncio.sleep(3)
#     return "fin de la segunda"

# async def main():
#     a, b = await asyncio.gather(one(), two())
#     print(a, b)

# asyncio.run(main())




# import asyncio


# async def primero(n_task, segundos):
#     print(f"Tarea {n_task} iniciada")
#     print(f"Esperando {segundos} segundos de la tarea {n_task}")
#     await asyncio.sleep(segundos)
#     print(f"Tarea {n_task} finalizada")
    
# async def segundo(n_task, segundos):
#     print(f"Tarea {n_task} iniciada")
#     print(f"Esperando {segundos} segundos de la terea {n_task}")
#     await asyncio.sleep(segundos)
#     print(f"Tarea {n_task} finaliza")


# async def main():
#     await asyncio.gather(primero(1, 5), segundo(2, 3))

# asyncio.run(main())
