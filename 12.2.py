# Cервер з асинхронним підрахунком чисел
import socket
import pickle
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(10)
print('Server is running, please, press ctrl+c to stop')

conn, addr = sock.accept()
print('connected:', addr)
data = conn.recv(1024)
data = pickle.loads(data)
number_1 = int(data['number_1'])
number_2 = int(data['number_2'])

async def add():
    res1=number_1+number_2
    await asyncio.sleep(0)
    conn.send(pickle.dumps(f"Addition: {res1} "))

async def sub():
    res2=number_1-number_2
    await asyncio.sleep(0)
    conn.send(pickle.dumps(f"Subtraction: {res2} "))

async def mult():
    res3=number_1*number_2
    await asyncio.sleep(0)
    conn.send(pickle.dumps(f"Multiplication: {res3} "))


myloop = asyncio.new_event_loop()
tasks = [
    myloop.create_task(add()),
    myloop.create_task(sub()),
    myloop.create_task(mult())
]
myloop.run_until_complete(asyncio.wait(tasks))
myloop.close()

conn.close()