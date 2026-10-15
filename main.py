from dispositivo import DispositivoRede
from conectividade import testar_ping

def iniciar_monitoramento():
    print("=== SISTEMA NETMONITOR PRO v1.0 ===")
    dispositivos = [
        DispositivoRede("Roteador-Core", "192.168.1.1", "roteador"),
        DispositivoRede("Switch-01", "10.0.0.1", "switch")
    ]
    for dev in dispositivos:
        status = testar_ping(dev.ip)
        dev.status = "Ativo" if status else "Inativo"
        print(dev)

if __name__ == "__main__":
    iniciar_monitoramento()
