from Client1 import Client1
from Client2 import Client2

if __name__ == "__main__":
    client1 = Client1()
    client2 = Client2()

    if id(client1.singleton) == id(client2.singleton):
        print("Singleton funciona, ambos clientes contem a mesma instância do Singleton.")
        print(client1.singleton)
        print(client2.singleton)
    else:
        print("Singleton não funcionou, os clientes possuem instâncias diferentes do Singleton.")
