# Чат клієнт повідомлення з консолі
import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))

number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")
data = {'number_1': number_1, 'number_2': number_2}
sock.send(pickle.dumps(data))

data = sock.recv(1024)
result = pickle.loads(data)
print(result)

data = sock.recv(1024)
result = pickle.loads(data)
print(result)

data = sock.recv(1024)
result = pickle.loads(data)
print(result)

sock.close()
