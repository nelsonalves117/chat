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

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((TCP_IP, TCP_PORTA))

print(f"Client disponível na porta {TCP_PORTA} e escutando.....")

def receberMensagens(cliente):
    while True:
        data = cliente.recv(TAMANHO_BUFFER)
        if data:
            print("\nResposta:", data.decode('UTF-8'))
            if 'Quit' in data.decode('UTF-8'):
                print("Encerrando a conexão")
                cliente.close()
                break

def enviarMensagens(cliente):
    while True:
        MENSAGEM = input("\n")
        cliente.send(MENSAGEM.encode('UTF-8'))
        if MENSAGEM == "Quit":
            print("Encerrando a conexão")
            cliente.close()
            break

receber_thread = threading.Thread(target=receberMensagens, args=(cliente,))
enviar_thread = threading.Thread(target=enviarMensagens, args=(cliente,))

receber_thread.start()
enviar_thread.start()
