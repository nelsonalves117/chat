import socket
import threading

def get_host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

TCP_IP = get_host_ip()
TCP_PORTA = 24000
TAMANHO_BUFFER = 1024

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((TCP_IP, TCP_PORTA))
servidor.listen(2)

print(f"Servidor disponível na porta {TCP_PORTA} e escutando.....")

def receberMensagens(conn):
    while True:
        data = conn.recv(TAMANHO_BUFFER)
        if data:
            print("\nResposta:", data.decode())
            if 'Quit' in data.decode():
                print("Encerrando a conexão")
                conn.close()
                break

def enviarMensagens(conn):
    while True:
        resposta = input("\n")
        conn.send(resposta.encode())
        if resposta == "Quit":
            print("Encerrando a conexão")
            conn.close()
            break

conn, addr = servidor.accept()
print('Endereço conectado:', addr)

receber_thread = threading.Thread(target=receberMensagens, args=(conn,))
enviar_thread = threading.Thread(target=enviarMensagens, args=(conn,))

receber_thread.start()
enviar_thread.start()
