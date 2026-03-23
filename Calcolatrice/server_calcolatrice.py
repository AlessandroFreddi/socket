import socket;
import json;
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024 

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((SERVER_IP,SERVER_PORT)) 
print("Pronto a ricevere i dati...")
while True:
    data, addr = sock.recvfrom (1024)
    if not data:
        break
    data = data.decode()
    data = json.loads(data)
    primoNumero = data["primoNumero"]
    operazione = data["operazione"]
    secondoNumero = data["secondoNumero"]
    risultato=eval(str(primoNumero)+(operazione)+str(secondoNumero))  
    sock.sendto(str(risultato).encode("UTF-8"), addr)
    print(risultato)